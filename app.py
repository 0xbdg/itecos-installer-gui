import sys
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class ITECInstaller(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = QUiLoader().load("ui/main.ui", None)
        self.load = ui

        self.setWindowTitle("ITEC-OS Installer")

    def show_gui(self):
        self.load.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ITECInstaller()
    gui.show_gui()
    app.exec()
