from PyQt6.QtWidgets import QWizardPage, QTextEdit,QVBoxLayout

class SummaryPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Siap Diinstal")
        self.setSubTitle("Periksa kembali pengaturan Anda sebelum proses instalasi dimulai.")
        
        layout = QVBoxLayout()
        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        self.summary_text.setStyleSheet("background-color: #181825; color: #cdd6f4; border: 1px solid #313244;")
        
        layout.addWidget(self.summary_text)
        self.setLayout(layout)

    def initializePage(self):
        lang = self.field("language")
        tz = self.field("timezone")
        user = self.field("username")
        part_mode = "Partisi Manual" if self.field("part_manual") else "Hapus Disk (Otomatis)"
        
        summary = f"""
        <b>PENGATURAN INSTALASI ITEC-OS</b><br><br>
        <b>Lokalisasi:</b><br> - Bahasa: {lang}<br> - Zona Waktu: {tz}<br><br>
        <b>Akun Pengguna:</b><br> - Username: {user}<br><br>
        <b>Konfigurasi Disk:</b><br> - Mode: {part_mode}<br><br>
        <i>Jika semua sudah benar, klik 'Next' untuk memulai instalasi.</i>
        """
        self.summary_text.setHtml(summary)

    def nextId(self):
        from ..wizard import PAGE_INSTALL
        return PAGE_INSTALL
