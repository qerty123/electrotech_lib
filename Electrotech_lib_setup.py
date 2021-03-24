import subprocess
import sys
import requests
import zipfile


def main():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])

    url = ""
    r = requests.get(url)
    filename = url.split("/")[-1]
    with zipfile.ZipFile(filename, 'r') as zip:
        zip.extractall()


if __name__ == "__main__":
    main()
