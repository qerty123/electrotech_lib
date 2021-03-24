#!/usr/bin/python3

import random
import sys
import os

from time import time
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

import design

tfps = 15
path = ""

tr_type = 0
con1 = 0
con2 = 0
base = 0
emitter_fr = 0
base_fr = 1

carriers = []
amperage = []


class Carrier:
    def __init__(self, posx, posy, based):
        self.posx = posx
        self.posy = posy
        self.based = based


class AmpermetrWidget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setScaledContents(True)
        self.pixmap = QtGui.QPixmap(path + 'amper.png')
        self.setPixmap(self.pixmap)

    def draw(self):
        self.pixmap = QtGui.QPixmap(path + 'amper.png')
        value = 0.1
        for i in range(len(amperage) - 1, len(amperage) - 10, -1):
            value += amperage[i]
        value /= 10
        x = round(400 * (value / 10)) + 40
        y = 100
        # y = round(75 * abs(sin(value * 18))) + 100
        if value > 5:
            y += round(7.5 * (value - 5))
        else:
            y += min(round(75 // value), 75)
        qp = QtGui.QPainter()
        qp.begin(self.pixmap)
        qp.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
        qp.drawLine(243, 370, x, y)
        self.setPixmap(self.pixmap)


class SchemaWidget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setScaledContents(True)
        self.pixmap = QtGui.QPixmap(path + 'transistor.png')
        self.setPixmap(self.pixmap)

    def draw(self):
        self.pixmap = QtGui.QPixmap(path + 'transistor.png')
        qp = QtGui.QPainter()
        qp.begin(self.pixmap)
        # Draw connections
        qp.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
        if con1 == 1:
            qp.drawLine(40, 475, 60, 475)
            qp.drawLine(50, 465, 50, 485)
        elif con1 == 2:
            qp.drawLine(40, 475, 60, 475)
        if con2 == 1:
            qp.drawLine(940, 475, 960, 475)
            qp.drawLine(950, 465, 950, 485)
        elif con2 == 2:
            qp.drawLine(940, 475, 960, 475)
        if base == 1:
            qp.drawLine(490, 475, 510, 475)
            qp.drawLine(500, 465, 500, 485)
        elif base == 2:
            qp.drawLine(490, 475, 510, 475)
        # Draw transistor
        if tr_type == 0:
            qp.setPen(QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine))
            qp.setBrush(QtCore.Qt.gray)
            qp.drawRect(150, 100, 250, 200)
            qp.drawRect(600, 100, 250, 200)
            qp.setBrush(QtCore.Qt.yellow)
            qp.drawRect(400, 100, 200, 200)
            qp.setPen(QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine))
            qp.setFont(QtGui.QFont('Decorative', 30))
            qp.drawText(275, 200, "N")
            qp.drawText(500, 200, "P")
            qp.drawText(725, 200, "N")
            if base == 0:
                qp.setPen(QtGui.QPen(QtCore.Qt.black, 0, QtCore.Qt.SolidLine))
                qp.setBrush(QtCore.Qt.green)
                if con1 == 1 and con2 == 2:
                    qp.drawRect(370, 100, 60, 200)
                if con1 == 2 and con2 == 1:
                    qp.drawRect(570, 100, 60, 200)
        # Draw carriers
        for i in carriers:
            qp.setBrush(QtCore.Qt.darkBlue)
            qp.drawEllipse(i.posx, i.posy, 15, 15)
        self.setPixmap(self.pixmap)


class PlotWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.navToolbar = NavigationToolbar2QT(self.canvas, self)
        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def draw(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')
        # ax.set_xlim([0, 60])
        ax.set_ylim([-1, max(amperage) + 2])
        ax.grid()
        ax.plot(amperage, linestyle='-', color='#008000')
        # ax.set(title='Осцилограф', xlable='t, сек', ylable='V, В')
        # ax.set_xlable('t, сек')
        ax.set_title('Оcцилограф')
        self.canvas.draw()


class VisualApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Size policy
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        # Plot widget
        self.PlotWidget = PlotWidget()
        self.PlotWidget.setSizePolicy(self.sizePolicy)
        self.PlotWidget.setMinimumSize(QtCore.QSize(500, 200))
        self.canvas_layout.addWidget(self.PlotWidget)
        self.PlotWidget.draw()
        # Canvas widget
        self.SchemaWidget = SchemaWidget()
        self.SchemaWidget.setSizePolicy(self.sizePolicy)
        self.SchemaWidget.setMinimumSize(QtCore.QSize(500, 200))
        self.canvas_layout.addWidget(self.SchemaWidget)
        self.SchemaWidget.draw()
        # Ampermetr widget
        self.AmpermetrWidget = AmpermetrWidget()
        self.AmpermetrWidget.setSizePolicy(self.sizePolicy)
        self.AmpermetrWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.AmpermetrWidget.setMaximumSize(QtCore.QSize(400, 300))
        self.menu_layout.addWidget(self.AmpermetrWidget)
        self.AmpermetrWidget.draw()
        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000 // tfps)
        # Bind changes
        self.button_update.clicked.connect(self.update_params)
        # self.base_fr.valueChanged.connect(self.update_params)
        # self.emitter_fr.valueChanged.connect(self.update_params)
        # Menu bar
        self.actionExit.triggered.connect(self.close)

    def tick(self):
        for i in carriers:
            move_carriers(i)
            if i.posy > 290 or i.posx > 840 or i.posx < 160:
                carriers.remove(i)
        if len(carriers) < 40:
            create_carriers()
        for i in range(len(amperage) - 1):
            amperage[i] = amperage[i+1]
        if base != 0 and ((con1 == 1 and con2 == 2) or (con1 == 2 and con2 == 1)):
            amperage[len(amperage) - 1] = self.emitter_fr.value() + self.base_fr.value() - 1
        else:
            amperage[len(amperage) - 1] = 0

        self.SchemaWidget.draw()
        self.PlotWidget.draw()
        self.AmpermetrWidget.draw()

    def update_params(self):
        global tr_type
        global con1
        global con2
        global base
        global carriers
        tr_type = self.tr_type.currentIndex()
        con1 = self.con1.currentIndex()
        con2 = self.con2.currentIndex()
        base = self.base.currentIndex()
        carriers = []


def create_carriers():
    if tr_type == 0:
        if base == 1:
            if con1 == 1 and con2 == 2:
                carriers.append(Carrier(830 + random.randint(-20, 20), 200 + random.randint(-50, 50), True))
                carriers.append(Carrier(830 + random.randint(-20, 20), 200 + random.randint(-50, 50), False))
            if con1 == 2 and con2 == 1:
                carriers.append(Carrier(170 + random.randint(-20, 20), 200 + random.randint(-50, 50), True))
                carriers.append(Carrier(170 + random.randint(-20, 20), 200 + random.randint(-50, 50), False))


def move_carriers(i):
    if tr_type == 0:
        if base == 1:
            if 450 < i.posx < 550 and i.based:
                i.posy += 10
            else:
                if con1 == 1 and con2 == 2:
                    i.posx -= 10
                if con1 == 2 and con2 == 1:
                    i.posx += 10


def main():
    global path
    spath = os.path.realpath(__file__).split("/")
    path = os.path.realpath(__file__).replace(spath[len(spath) - 1], "")
    for i in range(20 * tfps):
        amperage.append(0)
    app = QtWidgets.QApplication(sys.argv)
    window = VisualApp()
    window.showMaximized()
    app.exec()


if __name__ == '__main__':
    main()
