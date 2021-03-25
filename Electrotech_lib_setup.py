import subprocess
import sys


def main():
    try:
        import requests
    except:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    try:
        import zipfile
    except:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "zipfile"])

    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])

    url = "https://github.com/qerty123/electrotech_lib/archive/refs/heads/main.zip"
    r = requests.get(url)
    filename = url.split("/")[-1]
    extractpath = "."
    with zipfile.ZipFile(filename, 'r') as zip:
        zip.extractall(path=extractpath)


if __name__ == "__main__":
    main()
