import subprocess,os

def detect_boot_mode():
    return "UEFI" if os.path.exists("/sys/firmware/efi/efivars") else "BIOS"

def detect_secureboot():
    return subprocess.run(["mokutil", "--sb-state"], text=True, capture_output=True).stdout.strip().split()[-1]
