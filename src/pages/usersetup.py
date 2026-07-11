from PyQt6.QtWidgets import QWizardPage, QFormLayout, QLineEdit

class UserSetupPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Informasi Pengguna")
        self.setSubTitle("Buat akun untuk komputer ini.")
        
        layout = QFormLayout()
        self.name_edit = QLineEdit()
        self.comp_edit = QLineEdit()
        self.user_edit = QLineEdit()
        self.pass_edit = QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.registerField("fullname*", self.name_edit)
        self.registerField("computername*", self.comp_edit)
        self.registerField("username*", self.user_edit)
        self.registerField("password*", self.pass_edit)
        
        layout.addRow("Nama Lengkap:", self.name_edit)
        layout.addRow("Nama Komputer:", self.comp_edit)
        layout.addRow("Username:", self.user_edit)
        layout.addRow("Password:", self.pass_edit)
        self.setLayout(layout)
