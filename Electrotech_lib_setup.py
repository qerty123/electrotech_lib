import subprocess
import sys
import os


def main():
    downpath = ""
    url = "https://github.com/qerty123/electrotech_lib/archive/refs/heads/main.zip"
    extractpath = ""

    if os.name == "nt":
        downpath = "C:/Users/" + os.environ.get('USER') + "/Downloads/temp.zip"
        extractpath = "C:/Users/" + os.environ.get('USER') + "/Documents/"
    else:
        downpath = "/home/" + os.environ.get('USER') + "/Downloads/temp.zip"
        extractpath = "/home/" + os.environ.get('USER') + "/"

    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == "-h" or "--help":
            print("This setup script will install electrotech lib on your computer")
            print("Use -p or --path to set installation folder")
            sys.exit(0)
        if sys.argv[i] == "-p" or "--path":
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


if __name__ == "__main__":
    main()
