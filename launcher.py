#!/usr/bin/python3

import sys
import os
from PyQt5 import QtWidgets
import design

apps = []
path = ""


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

    def launch(self):
        way = path + apps[self.list.currentRow()] + "/" + apps[self.list.currentRow()] + ".py"
        os.system("python " + way)

    def show_license(self):
        lwindow = SubWindow("LICENSE")
        lwindow.show()

    def show_about(self):
        awindow = SubWindow("README.md")
        awindow.show()


def main():
    global path
    spath = os.path.realpath(__file__).split("/")
    path = os.path.realpath(__file__).replace(spath[len(spath) - 1], "")
    _, dirnames, _ = next(os.walk(path))
    for i in dirnames:
        if i[0].isalpha():
            apps.append(i)
    app = QtWidgets.QApplication(sys.argv)
    window = VisualApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
