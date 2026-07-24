from PyQt6.QtWidgets import QWizardPage, QVBoxLayout, QLineEdit, QLabel, QComboBox
from src.core.config import KEYMAP, LOCALE, TIMEZONE
import subprocess

class KeyboardPage(QWizardPage):
    def __init__(self):
        super().__init__()
        keymaps = subprocess.run(["localectl", "list-keymaps"], stdout=subprocess.PIPE, text=True).stdout.strip().split('\n')
        self.setTitle("Susunan Keyboard")
        self.setSubTitle("Pilih tata letak keyboard yang Anda gunakan.")
        
        layout = QVBoxLayout()
        self.kb_combo = QComboBox()
        self.kb_combo.addItems([k for k in sorted(keymaps)])
        
        self.test_input = QLineEdit()
        self.test_input.setPlaceholderText("Ketik di sini untuk menguji keyboard Anda...")
        
        layout.addWidget(QLabel(f"Layout Keyboard:"))
        layout.addWidget(self.kb_combo)
        layout.addSpacing(20)
        layout.addWidget(QLabel("Uji Keyboard:"))
        layout.addWidget(self.test_input)
        self.setLayout(layout)
        
        self.registerField("keyboard", self.kb_combo, "currentText")

    def validatePage(self) -> bool:
        KEYMAP = self.kb_combo.currentText()
        print(LOCALE, TIMEZONE, KEYMAP)
        return True
