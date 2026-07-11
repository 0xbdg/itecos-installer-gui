import sys, pathlib
from PyQt6.QtWidgets import QApplication
from src.wizard import WizardInstaller

if __name__ == "__main__":
    assets_path = pathlib.Path(__file__).parent / "assets/"
    app = QApplication(sys.argv)
    w = WizardInstaller(assets_path)
    w.show()
    sys.exit(app.exec())
