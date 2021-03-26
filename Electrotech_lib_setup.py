import subprocess
import sys
import os


def main():
    downpath = ""
    url = "https://github.com/qerty123/electrotech_lib/archive/refs/heads/main.zip"
    extractpath = ""

    try:
        import getpass
    except:
        print("Installing getpass lib")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "getpass"])
        import getpass

    if os.name == "nt":
        downpath = "C:/Users/" + getpass.getuser() + "/Downloads/temp.zip"
        extractpath = "C:/Users/" + getpass.getuser() + "/Documents/"
    else:
        downpath = "/home/" + getpass.getuser() + "/Downloads/temp.zip"
        extractpath = "/home/" + getpass.getuser() + "/"

    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            print("This setup script will install electrotech lib on your computer")
            print("Use -p or --path to set installation folder")
            sys.exit(0)
        if sys.argv[i] == "-p" or sys.argv[i] == "--path":
            i += 1
            extractpath = sys.argv[i].replace('"', '')

    try:
        import requests
    except:
        print("Installing requests lib")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests

    try:
        import zipfile
    except:
        print("Installing zipfile lib")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "zipfile"])
        import zipfile

    print("Installing matplotlib lib")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    print("Installing pyqt lib")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])

    print("Downloading archive")
    r = requests.get(url)
    open(downpath, "wb").write(r.content)
    print("Extracting files")
    with zipfile.ZipFile(downpath, 'r') as zip:
        zip.extractall(path=extractpath)

    if os.name == "nt" and False: # Temorary not use it
        print("Creating shortcut")
        f = open(extractpath + "Electrotech_lib/start.bat", "w+")
        f.write("@echo off")
        f.write("python " + extractpath + "Electrotech_lib/launcher.py")
        f.close()
        try:
            import win32com
        except:
            print("Installing win32com lib")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "win32com"])
            import win32com
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut("C:/Users/" + getpass.getuser() + "/Desktop/Electrotech")
        shortcut.Targetpath = extractpath + "Electrotech_lib/launcher.py"
        shortcut.WorkingDirectory = extractpath + "Electrotech_lib/"
        shortcut.IconLocation = extractpath + "Electrotech_lib/Icon.ico"
        shortcut.save()


if __name__ == "__main__":
    main()
