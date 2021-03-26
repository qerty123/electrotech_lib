#!/usr/bin/python3

import sys
import os
from PyQt5 import QtWidgets, QtCore
import design
import requests
import time

apps = []
path = ""
updatable = False
curversion = ""
avversion = ""

class SubWindow(QtWidgets.QWidget):
    def __init__(self, filename):
        super().__init__()
        f = open(path + filename)
        text = f.readline()
        f.close()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle(filename)


class VisualApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Size policy
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.list.addItems(apps)
        self.list.doubleClicked.connect(self.launch)
        self.button_license.clicked.connect(self.show_license)
        self.button_about.clicked.connect(self.show_about)
        self.button_update.clicked.connect(self.update)
        self.label_version.setText("Текущая версия " + curversion)
        self.label_avaluable.setText("Актуальная версия " + avversion)
        if updatable:
            self.button_update.setEnabled(True)

    def launch(self):
        way = path + apps[self.list.currentRow()] + "/" + apps[self.list.currentRow()] + ".py"
        # os.system("python " + way)
        self.p = QtCore.QProcess()
        self.p.start("python", [way])
        self.hide()
        self.p.finished.connect(self.show)

    def show_license(self):
        lwindow = SubWindow("LICENSE")
        lwindow.show()

    def show_about(self):
        awindow = SubWindow("README.md")
        awindow.show()

    def update(self):
        way = path + "Electrotech_lib_setup.py"
        os.system("python " + way + " -p " + path)
        sys.exit(0)


def main():
    global path
    global updatable
    global avversion
    global curversion

    try:
        r = requests.get("https://raw.githubusercontent.com/qerty123/electrotech_lib/main/VERSION")
        avversion = r.content.decode(encoding="utf-8")
    except:
        pass
    try:
        f = open("VERSION", "r")
        curversion = f.readline()
        f.close()
    except:
        pass
    if avversion != curversion:
        updatable = True

    spath = []
    if os.name == "nt":
        spath = os.path.realpath(__file__).split("\\")
    else:
        spath = os.path.realpath(__file__).split("/")
    path = os.path.realpath(__file__).replace(spath[len(spath) - 1], "")
    dirnames = os.listdir(path)
    for i in dirnames:
        if os.path.isdir(os.path.join(path, i)) and i[0].isalpha():
            apps.append(i)
    app = QtWidgets.QApplication(sys.argv)
    window = VisualApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
