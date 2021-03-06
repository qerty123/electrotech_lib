# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './diod/design.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.menu_layout = QtWidgets.QVBoxLayout()
        self.menu_layout.setObjectName("menu_layout")
        self.label_source = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_source.sizePolicy().hasHeightForWidth())
        self.label_source.setSizePolicy(sizePolicy)
        self.label_source.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_source.setObjectName("label_source")
        self.menu_layout.addWidget(self.label_source)
        self.voltage_source = QtWidgets.QSlider(self.centralwidget)
        self.voltage_source.setMaximumSize(QtCore.QSize(400, 16777215))
        self.voltage_source.setMaximum(10)
        self.voltage_source.setOrientation(QtCore.Qt.Horizontal)
        self.voltage_source.setObjectName("voltage_source")
        self.menu_layout.addWidget(self.voltage_source)
        self.label_barrier = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_barrier.sizePolicy().hasHeightForWidth())
        self.label_barrier.setSizePolicy(sizePolicy)
        self.label_barrier.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_barrier.setObjectName("label_barrier")
        self.menu_layout.addWidget(self.label_barrier)
        self.voltage_barrier = QtWidgets.QSlider(self.centralwidget)
        self.voltage_barrier.setMaximumSize(QtCore.QSize(400, 16777215))
        self.voltage_barrier.setMinimum(1)
        self.voltage_barrier.setMaximum(100)
        self.voltage_barrier.setProperty("value", 10)
        self.voltage_barrier.setOrientation(QtCore.Qt.Horizontal)
        self.voltage_barrier.setObjectName("voltage_barrier")
        self.menu_layout.addWidget(self.voltage_barrier)
        self.is_alternating = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_alternating.sizePolicy().hasHeightForWidth())
        self.is_alternating.setSizePolicy(sizePolicy)
        self.is_alternating.setMaximumSize(QtCore.QSize(400, 16777215))
        self.is_alternating.setObjectName("is_alternating")
        self.menu_layout.addWidget(self.is_alternating)
        self.label_alternating = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_alternating.sizePolicy().hasHeightForWidth())
        self.label_alternating.setSizePolicy(sizePolicy)
        self.label_alternating.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_alternating.setObjectName("label_alternating")
        self.menu_layout.addWidget(self.label_alternating)
        self.alternating_frequency = QtWidgets.QSlider(self.centralwidget)
        self.alternating_frequency.setMaximumSize(QtCore.QSize(400, 16777215))
        self.alternating_frequency.setMinimum(1)
        self.alternating_frequency.setMaximum(30)
        self.alternating_frequency.setProperty("value", 10)
        self.alternating_frequency.setOrientation(QtCore.Qt.Horizontal)
        self.alternating_frequency.setObjectName("alternating_frequency")
        self.menu_layout.addWidget(self.alternating_frequency)
        self.is_back = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_back.sizePolicy().hasHeightForWidth())
        self.is_back.setSizePolicy(sizePolicy)
        self.is_back.setMaximumSize(QtCore.QSize(400, 16777215))
        self.is_back.setObjectName("is_back")
        self.menu_layout.addWidget(self.is_back)
        self.is_secondary = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_secondary.sizePolicy().hasHeightForWidth())
        self.is_secondary.setSizePolicy(sizePolicy)
        self.is_secondary.setMaximumSize(QtCore.QSize(400, 16777215))
        self.is_secondary.setObjectName("is_secondary")
        self.menu_layout.addWidget(self.is_secondary)
        self.error_msg = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_msg.sizePolicy().hasHeightForWidth())
        self.error_msg.setSizePolicy(sizePolicy)
        self.error_msg.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.error_msg.setFont(font)
        self.error_msg.setText("")
        self.error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.error_msg.setObjectName("error_msg")
        self.menu_layout.addWidget(self.error_msg)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_layout.addItem(spacerItem)
        self.horizontal_layout.addLayout(self.menu_layout)
        self.canvas_layout = QtWidgets.QVBoxLayout()
        self.canvas_layout.setObjectName("canvas_layout")
        self.horizontal_layout.addLayout(self.canvas_layout)
        self.verticalLayout_3.addLayout(self.horizontal_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUpdate_settings = QtWidgets.QAction(MainWindow)
        self.actionUpdate_settings.setObjectName("actionUpdate_settings")
        self.actionSet_defaults = QtWidgets.QAction(MainWindow)
        self.actionSet_defaults.setObjectName("actionSet_defaults")
        self.actionMinimaize = QtWidgets.QAction(MainWindow)
        self.actionMinimaize.setObjectName("actionMinimaize")
        self.actionMaximaize = QtWidgets.QAction(MainWindow)
        self.actionMaximaize.setObjectName("actionMaximaize")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUpdate_settings)
        self.menuEdit.addAction(self.actionSet_defaults)
        self.menuWindow.addAction(self.actionMinimaize)
        self.menuWindow.addAction(self.actionMaximaize)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????????????? P-N ????????????????"))
        self.label_source.setText(_translate("MainWindow", "???????????????????? ???? ??????????????????, ??:"))
        self.label_barrier.setText(_translate("MainWindow", "???????????????????? ????????????????????, ??:"))
        self.is_alternating.setText(_translate("MainWindow", "???????????????????? ??????"))
        self.label_alternating.setText(_translate("MainWindow", "?????????????? ?????????????????????? ????????, ????:"))
        self.is_back.setText(_translate("MainWindow", "???????????????? ?????????????????????? ????????"))
        self.is_secondary.setText(_translate("MainWindow", "?????????????????? ???????????????? ??????????????"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUpdate_settings.setText(_translate("MainWindow", "Update settings"))
        self.actionSet_defaults.setText(_translate("MainWindow", "Set defaults"))
        self.actionMinimaize.setText(_translate("MainWindow", "Minimaize"))
        self.actionMaximaize.setText(_translate("MainWindow", "Maximaize"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLicense.setText(_translate("MainWindow", "License"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
