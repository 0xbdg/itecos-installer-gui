import sys
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class WelcomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = QUiLoader().load("ui/welcome.ui")
        self.load = ui

        self.setWindowTitle("ITEC-OS Installer (0xbdg)")
