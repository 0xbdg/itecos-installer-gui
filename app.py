import sys, pathlib
from PyQt6.QtWidgets import QApplication, QMessageBox
from src.wizard import WizardInstaller
from src.core.detector import check_internet

if __name__ == "__main__":
    assets_path = pathlib.Path(__file__).parent / "assets/"
    app = QApplication(sys.argv)
    w = WizardInstaller(assets_path)

    if not check_internet:
        QMessageBox.warning(None, "Connection Error", "Please check you internet connection to continue!")

    else:
        w.show()
        sys.exit(app.exec())
