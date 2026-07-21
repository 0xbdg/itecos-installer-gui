from PyQt6.QtWidgets import QFormLayout, QComboBox,QWizardPage
from zoneinfo import available_timezones
from config import LOCALE, TIMEZONE

import subprocess

class LocalePage(QWizardPage):
    def __init__(self):
        super().__init__()
        locales = subprocess.run(["grep \"^#[a-z]\" /etc/locale.gen | sed 's/^#//'"], shell=True,stdout=subprocess.PIPE, text=True).stdout.strip().split('\n')
        self.setTitle("Lokalisasi")
        self.setSubTitle("Pilih bahasa dan zona waktu Anda.")
        
        layout = QFormLayout()
        self.lang_combo = QComboBox()
        self.lang_combo.addItems([l for l in locales])
        self.tz_combo = QComboBox()
        self.tz_combo.addItems([tz for tz in sorted(available_timezones())])
        
        layout.addRow("Language:", self.lang_combo)
        layout.addRow("Time Zone:", self.tz_combo)
        self.registerField("language", self.lang_combo, "currentText")
        self.registerField("timezone", self.tz_combo, "currentText")
        self.setLayout(layout)

    def validatePage(self) ->bool:
        LOCALE=self.lang_combo.currentText()
        TIMEZONE=self.tz_combo.currentText()

        print(LOCALE, TIMEZONE)
        return True
