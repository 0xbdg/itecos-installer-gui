import sys, pathlib
from PyQt6.QtWidgets import QApplication
from src.wizard import WizardInstaller

if __name__ == "__main__":
    qss_file = pathlib.Path(__file__).parent / "assets/style.qss"
    app = QApplication(sys.argv)
    w = WizardInstaller(qss_file)
    w.show()
    sys.exit(app.exec())
