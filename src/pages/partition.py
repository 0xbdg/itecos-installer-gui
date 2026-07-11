from wizard import PAGE_PART_ADVANCED, PAGE_SUMMARY
from PyQt6.QtWidgets import QWizardPage, QVBoxLayout, QRadioButton, QButtonGroup, QLabel

class PartitionChoicePage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Persiapan Disk")
        self.setSubTitle("Bagaimana Anda ingin menginstal ITEC-OS?")
        
        layout = QVBoxLayout()
        self.radio_group = QButtonGroup(self)
        
        self.radio_auto = QRadioButton("Hapus seluruh disk dan instal ITEC-OS")
        self.radio_auto.setChecked(True)
        auto_desc = QLabel("  Peringatan: Semua data di disk akan dihapus.")
        auto_desc.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        self.radio_manual = QRadioButton("Partisi Manual (Advanced)")
        manual_desc = QLabel("  Buat, hapus, atau atur ukuran partisi secara mandiri.")
        manual_desc.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        self.radio_group.addButton(self.radio_auto)
        self.radio_group.addButton(self.radio_manual)
        
        layout.addWidget(self.radio_auto)
        layout.addWidget(auto_desc)
        layout.addSpacing(10)
        layout.addWidget(self.radio_manual)
        layout.addWidget(manual_desc)
        self.setLayout(layout)
        
        self.registerField("part_auto", self.radio_auto)
        self.registerField("part_manual", self.radio_manual)

    def nextId(self):
        if self.radio_manual.isChecked():
            return PAGE_PART_ADVANCED
        return PAGE_SUMMARY
