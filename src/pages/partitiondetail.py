from PyQt6.QtWidgets import QWizardPage, QVBoxLayout, QDialog, QFormLayout, QLineEdit, QComboBox,QCheckBox, QHBoxLayout, QPushButton, QLabel, QFrame, QTableWidget, QHeaderView, QAbstractItemView, QWidget, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt

class PartitionDialog(QDialog):
    def __init__(self, parent=None, is_edit=False, current_data=None):
        super().__init__(parent)
        self.setWindowTitle("Ubah Partisi" if is_edit else "Tambah Partisi Baru")
        self.setFixedSize(350, 250)
        
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        self.size_input = QLineEdit()
        self.size_input.setPlaceholderText("Contoh: 50 GB atau 512 MB")
        
        self.fs_combo = QComboBox()
        self.fs_combo.addItems(["ext4", "btrfs", "xfs", "fat32", "swap", "Tanpa Format"])
        
        self.mount_combo = QComboBox()
        self.mount_combo.setEditable(True)
        self.mount_combo.addItems(["/", "/home", "/boot/efi", "/var", "[Swap]"])
        
        self.format_check = QCheckBox("Format partisi ini")
        self.format_check.setChecked(True)
        
        form_layout.addRow("Ukuran:", self.size_input)
        form_layout.addRow("File System:", self.fs_combo)
        form_layout.addRow("Mount Point:", self.mount_combo)
        form_layout.addRow("", self.format_check)
        
        layout.addLayout(form_layout)
        
        btn_layout = QHBoxLayout()
        self.btn_ok = QPushButton("OK")
        self.btn_cancel = QPushButton("Batal")
        self.btn_ok.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)
        
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_ok)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
        
        if is_edit and current_data:
            self.size_input.setText(current_data['size'])
            self.fs_combo.setCurrentText(current_data['fs'])
            self.mount_combo.setCurrentText(current_data['mount'])
            self.format_check.setChecked(current_data['format'] == "Ya")

    def get_data(self):
        return {
            "size": self.size_input.text(),
            "fs": self.fs_combo.currentText(),
            "mount": self.mount_combo.currentText(),
            "format": "Ya" if self.format_check.isChecked() else "Tidak"
        }

class AdvancedPartitionPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Partisi Manual")
        self.setSubTitle("Atur titik kait (mount points) dan ukuran partisi.")
        
        main_layout = QVBoxLayout()
        
        # Pilihan Disk
        disk_layout = QHBoxLayout()
        disk_layout.addWidget(QLabel("Pilih Penyimpanan:"))
        self.disk_combo = QComboBox()
        self.disk_combo.addItems(["/dev/nvme0n1 - 512.0 GB", "/dev/sda - 1.0 TB"])
        disk_layout.addWidget(self.disk_combo)
        disk_layout.addStretch()
        main_layout.addLayout(disk_layout)
        
        # Penambahan Label Judul Visualisasi
        visual_label = QLabel("Visualisasi Tata Letak Disk Saat Ini:")
        visual_label.setStyleSheet("color: #a6adc8; font-size: 13px; font-weight: bold; margin-top: 5px;")
        main_layout.addWidget(visual_label)
        
        # Visual Bar Container
        self.visual_bar = QFrame()
        self.visual_bar.setFixedHeight(40)
        self.visual_bar.setStyleSheet("border-radius: 4px; overflow: hidden; border: 1px solid #313244;")
        self.vis_layout = QHBoxLayout(self.visual_bar)
        self.vis_layout.setContentsMargins(0, 0, 0, 0)
        self.vis_layout.setSpacing(0)
        main_layout.addWidget(self.visual_bar)
        main_layout.addSpacing(10)
        
        # Tabel Partisi
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Device", "File System", "Mount Point", "Format", "Size"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        
        self.add_row_to_table("/dev/nvme0n1p1", "fat32", "/boot/efi", "Tidak", "512 MB")
        self.add_row_to_table("/dev/nvme0n1p2", "ext4", "/", "Ya", "230 GB")
        self.add_row_to_table("Free Space", "unallocated", "", "", "281.5 GB")
        main_layout.addWidget(self.table)
        
        # Tombol Aksi
        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("+ Tambah")
        self.btn_edit = QPushButton("✎ Ubah")
        self.btn_delete = QPushButton("- Hapus")
        
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_delete)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

        # Koneksi Tombol
        self.btn_add.clicked.connect(self.action_add)
        self.btn_edit.clicked.connect(self.action_edit)
        self.btn_delete.clicked.connect(self.action_delete)

        # Gambar visual bar awal
        self.update_visual_layout()

    # --- LOGIKA VISUALISASI ---
    def parse_size_to_mb(self, size_str):
        s = size_str.upper().replace(" ", "")
        try:
            if "GB" in s: return float(s.replace("GB", "")) * 1024
            if "MB" in s: return float(s.replace("MB", ""))
            if "TB" in s: return float(s.replace("TB", "")) * 1024 * 1024
            return float(s)
        except ValueError:
            return 1 

    def update_visual_layout(self):
        for i in reversed(range(self.vis_layout.count())): 
            widget_to_remove = self.vis_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

        for row in range(self.table.rowCount()):
            device = self.table.item(row, 0).text()
            fs = self.table.item(row, 1).text()
            mount = self.table.item(row, 2).text()
            size_str = self.table.item(row, 4).text()

            stretch = int(self.parse_size_to_mb(size_str))
            if stretch < 1: stretch = 1 

            if device == "Free Space": color = "#45475a" 
            elif "efi" in mount.lower() or fs == "fat32": color = "#f9e2af"
            elif fs == "swap": color = "#f38ba8" 
            else: color = "#89b4fa" 
            
            # Penentuan teks label dalam balok
            if device == "Free Space":
                label_text = "Free"
            elif mount.strip() != "":
                label_text = mount
            else:
                label_text = fs

            tooltip = f"{device} ({fs}) - {size_str}"
            block = self.create_color_block(color, stretch, label_text, tooltip)
            self.vis_layout.addWidget(block)

    def create_color_block(self, color, stretch, label_text, tooltip):
        block = QLabel(label_text)
        block.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        text_color = "#11111b" if color != "#45475a" else "#cdd6f4"
        
        block.setStyleSheet(f"""
            background-color: {color}; 
            color: {text_color}; 
            font-size: 12px; 
            font-weight: bold; 
            border-right: 1px solid #1e1e2e;
        """)
        
        block.setToolTip(tooltip)
        block.setSizePolicy(block.sizePolicy().Policy.Ignored, block.sizePolicy().Policy.Expanding)
        
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(block)
        container.setProperty("stretch", stretch)
        return container

    # --- FUNGSI TABEL ---
    def add_row_to_table(self, device, fs, mount, format_flag, size):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(device))
        self.table.setItem(row, 1, QTableWidgetItem(fs))
        self.table.setItem(row, 2, QTableWidgetItem(mount))
        self.table.setItem(row, 3, QTableWidgetItem(format_flag))
        self.table.setItem(row, 4, QTableWidgetItem(size))

    def action_add(self):
        dialog = PartitionDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            row_count = self.table.rowCount()
            device_name = f"/dev/nvme0n1p{row_count}"
            insert_pos = row_count - 1 if row_count > 0 else 0
            
            self.table.insertRow(insert_pos)
            self.table.setItem(insert_pos, 0, QTableWidgetItem(device_name))
            self.table.setItem(insert_pos, 1, QTableWidgetItem(data['fs']))
            self.table.setItem(insert_pos, 2, QTableWidgetItem(data['mount']))
            self.table.setItem(insert_pos, 3, QTableWidgetItem(data['format']))
            self.table.setItem(insert_pos, 4, QTableWidgetItem(data['size']))
            
            self.update_visual_layout()

    def action_edit(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih partisi yang ingin diubah.")
            return
        if self.table.item(selected_row, 0).text() == "Free Space":
            QMessageBox.information(self, "Info", "Tidak bisa mengedit Free Space.")
            return

        current_data = {
            "fs": self.table.item(selected_row, 1).text(),
            "mount": self.table.item(selected_row, 2).text(),
            "format": self.table.item(selected_row, 3).text(),
            "size": self.table.item(selected_row, 4).text(),
        }

        dialog = PartitionDialog(self, is_edit=True, current_data=current_data)
        if dialog.exec():
            new_data = dialog.get_data()
            self.table.setItem(selected_row, 1, QTableWidgetItem(new_data['fs']))
            self.table.setItem(selected_row, 2, QTableWidgetItem(new_data['mount']))
            self.table.setItem(selected_row, 3, QTableWidgetItem(new_data['format']))
            self.table.setItem(selected_row, 4, QTableWidgetItem(new_data['size']))
            
            self.update_visual_layout()

    def action_delete(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih partisi yang ingin dihapus.")
            return
        if self.table.item(selected_row, 0).text() == "Free Space":
            return
            
        reply = QMessageBox.question(self, 'Konfirmasi', 'Hapus partisi ini?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.table.removeRow(selected_row)
            self.update_visual_layout()

    def nextId(self):
        from ..wizard import PAGE_SUMMARY
        return PAGE_SUMMARY
