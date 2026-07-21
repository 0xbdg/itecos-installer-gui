from PyQt6.QtWidgets import QWizard

from .pages.install import InstallProgressPage
from .pages.welcome import WelcomePage
from .pages.locale import LocalePage
from .pages.keyboard import KeyboardPage
from .pages.account import UserSetupPage
from .pages.partition import PartitionChoicePage
from .pages.partitiondetail import AdvancedPartitionPage
from .pages.summary import SummaryPage

PAGE_WELCOME = 0
PAGE_LOCALE = 1
PAGE_KEYBOARD = 2
PAGE_USER = 3
PAGE_PART_CHOICE = 4
PAGE_PART_ADVANCED = 5
PAGE_SUMMARY = 6
PAGE_INSTALL = 7

class WizardInstaller(QWizard): 
    def __init__(self, assets_folder):
        super().__init__()
        self.setWindowTitle("ITEC-OS Installer")
        self.setWizardStyle(QWizard.WizardStyle.AeroStyle)
        self.setPage(PAGE_WELCOME, WelcomePage(assets_folder=assets_folder))
        self.setPage(PAGE_LOCALE, LocalePage())
        self.setPage(PAGE_KEYBOARD, KeyboardPage())
        self.setPage(PAGE_USER, UserSetupPage())
        self.setPage(PAGE_PART_CHOICE, PartitionChoicePage())
        self.setPage(PAGE_PART_ADVANCED, AdvancedPartitionPage())
        self.setPage(PAGE_SUMMARY, SummaryPage())
        self.setPage(PAGE_INSTALL, InstallProgressPage())


        self.resize(500,500)
        self.setStyleSheet(open(assets_folder / "style.qss", "r").read())
