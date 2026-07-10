import sys
from PyQt6.QtWidgets import QApplication
from src.wizard import WizardInstaller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WizardInstaller()
    w.show()
    sys.exit(app.exec())
