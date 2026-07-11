from PyQt6.QtWidgets import QWizardPage, QVBoxLayout, QLabel,QWizard
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class WelcomePage(QWizardPage):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        welcome_label = QLabel(
            "Terima kasih telah memilih ITEC-OS.\n\n"
            "Wizard ini akan memandu Anda melalui langkah-langkah yang diperlukan "
            "untuk memasang sistem operasi ini di komputer Anda.\n\n"
            "Pastikan komputer Anda terhubung ke sumber daya listrik dan internet "
            "sebelum melanjutkan untuk pengalaman instalasi yang optimal."
        )
        welcome_label.setWordWrap(True)
        welcome_label.setStyleSheet("font-size: 15px; line-height: 1.5;")
        
        layout.addStretch()
        layout.addWidget(welcome_label)
        layout.addStretch()
        self.setLayout(layout)
