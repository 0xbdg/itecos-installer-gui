from PyQt6.QtWidgets import QWizardPage, QVBoxLayout, QLineEdit, QLabel, QComboBox

class KeyboardPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Susunan Keyboard")
        self.setSubTitle("Pilih tata letak keyboard yang Anda gunakan.")
        
        layout = QVBoxLayout()
        self.kb_combo = QComboBox()
        self.kb_combo.addItems(["English (US, Default)", "English (UK)", "Arabic", "Dvorak"])
        
        test_input = QLineEdit()
        test_input.setPlaceholderText("Ketik di sini untuk menguji keyboard Anda...")
        
        layout.addWidget(QLabel("Layout Keyboard:"))
        layout.addWidget(self.kb_combo)
        layout.addSpacing(20)
        layout.addWidget(QLabel("Uji Keyboard:"))
        layout.addWidget(test_input)
        self.setLayout(layout)
        
        self.registerField("keyboard", self.kb_combo, "currentText")
