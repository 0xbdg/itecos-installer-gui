from PyQt6.QtWidgets import QWizardPage, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class WelcomePage(QWizardPage):
    def __init__(self, assets_folder):
        super().__init__()

        image_layout = QHBoxLayout()
        layout = QVBoxLayout()
        image_label = QLabel()
        pixmap = QPixmap(str(assets_folder / "logo.png"))

        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label = QLabel(
            "Terima kasih telah memilih ITEC-OS.\n\n"
            "Wizard ini akan memandu Anda melalui langkah-langkah yang diperlukan "
            "untuk memasang sistem operasi ini di komputer Anda.\n\n"
            "Pastikan komputer Anda terhubung ke sumber daya listrik dan internet "
            "sebelum melanjutkan untuk pengalaman instalasi yang optimal."
        )
        welcome_label.setWordWrap(False)
        welcome_label.setStyleSheet("font-size: 15px; line-height: 1.5;")
        
        layout.addStretch()
        layout.addWidget(welcome_label)
        layout.addStretch()

        image_layout.addWidget(image_label)
        image_layout.addLayout(layout)
        self.setLayout(image_layout)
