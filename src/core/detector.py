import os, socket, subprocess

check_internet = lambda: socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(("8.8.8.8", 53))

def detect_boot_mode():
    return "UEFI" if os.path.exists("/sys/firmware/efi/efivars") else "BIOS"

def detect_secureboot():
    return subprocess.run(["mokutil", "--sb-state"], text=True, capture_output=True).stdout.strip().split()[-1]
