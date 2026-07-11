from PyQt6.QtWidgets import QWizardPage,QWizard, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtCore import QTimer

class InstallProgressPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Menginstal CustomOS")
        self.setSubTitle("Mohon tunggu, sistem sedang dipasang ke disk Anda...")
        
        layout = QVBoxLayout()
        self.progress_label = QLabel("Menyiapkan file system...")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

    def initializePage(self):
        self.wizard().button(QWizard.WizardButton.BackButton).setEnabled(False)
        self.progress_bar.setValue(0)
        self.timer.start(80) 

    def update_progress(self):
        val = self.progress_bar.value()
        if val < 100:
            self.progress_bar.setValue(val + 1)
            if val == 30: self.progress_label.setText("Mengekstrak root filesystem (squashfs)...")
            elif val == 70: self.progress_label.setText("Menginstal bootloader (GRUB)...")
        else:
            self.timer.stop()
            self.progress_label.setText("Instalasi Selesai! Silakan mulai ulang komputer Anda.")
            self.wizard().button(QWizard.WizardButton.NextButton).setEnabled(True)

    def isComplete(self):
        return self.progress_bar.value() == 100
