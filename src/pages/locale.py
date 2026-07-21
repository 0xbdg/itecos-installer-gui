from PyQt6.QtWidgets import QFormLayout, QComboBox,QWizardPage
from config import LOCALE, TIMEZONE

class LocalePage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Lokalisasi")
        self.setSubTitle("Pilih bahasa dan zona waktu Anda.")
        
        layout = QFormLayout()
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Indonesia (id_ID)", "English (en_US)"])
        self.tz_combo = QComboBox()
        self.tz_combo.addItems(["Asia/Jakarta (WIB)", "Asia/Makassar (WITA)", "Asia/Jayapura (WIT)"])
        
        layout.addRow("Language:", self.lang_combo)
        layout.addRow("Time Zone:", self.tz_combo)
        self.registerField("language", self.lang_combo, "currentText")
        self.registerField("timezone", self.tz_combo, "currentText")
        self.setLayout(layout)

    def validatePage(self) ->bool:
        LOCALE=self.lang_combo.currentText()
        TIMEZONE=self.tz_combo.currentText()

        return True
