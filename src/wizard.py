from PyQt6.QtWidgets import QWizard

from .pages.welcome import WelcomePage
from .pages.locale import LocalePage
from .pages.keyboard import KeyboardPage
from .pages.usersetup import UserSetupPage
from .pages.partition import PartitionChoicePage
from .pages.partitiondetail import AdvancedPartitionPage

PAGE_WELCOME = 0
PAGE_LOCALE = 1
PAGE_KEYBOARD = 2
PAGE_USER = 3
PAGE_PART_CHOICE = 4
PAGE_PART_ADVANCED = 5
PAGE_SUMMARY = 6
PAGE_INSTALL = 7

class WizardInstaller(QWizard): 
    def __init__(self, style_file):
        super().__init__()
        self.setWindowTitle("ITEC-OS Installer")
        self.setWizardStyle(QWizard.WizardStyle.AeroStyle)
        self.setPage(PAGE_WELCOME, WelcomePage())
        self.setPage(PAGE_LOCALE, LocalePage())
        self.setPage(PAGE_KEYBOARD, KeyboardPage())
        self.setPage(PAGE_USER, UserSetupPage())
        self.setPage(PAGE_PART_CHOICE, PartitionChoicePage())
        self.setPage(PAGE_PART_ADVANCED, AdvancedPartitionPage())


        self.resize(500,500)
        self.setStyleSheet(open(style_file, "r").read())

