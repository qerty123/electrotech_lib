# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
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
        self.lable_type = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lable_type.sizePolicy().hasHeightForWidth())
        self.lable_type.setSizePolicy(sizePolicy)
        self.lable_type.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lable_type.setObjectName("lable_type")
        self.menu_layout.addWidget(self.lable_type)
        self.tr_type = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tr_type.sizePolicy().hasHeightForWidth())
        self.tr_type.setSizePolicy(sizePolicy)
        self.tr_type.setMaximumSize(QtCore.QSize(400, 16777215))
        self.tr_type.setObjectName("tr_type")
        self.tr_type.addItem("")
        self.tr_type.addItem("")
        self.tr_type.addItem("")
        self.tr_type.addItem("")
        self.tr_type.addItem("")
        self.tr_type.addItem("")
        self.tr_type.addItem("")
        self.tr_type.addItem("")
        self.menu_layout.addWidget(self.tr_type)
        self.label_base = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_base.sizePolicy().hasHeightForWidth())
        self.label_base.setSizePolicy(sizePolicy)
        self.label_base.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_base.setObjectName("label_base")
        self.menu_layout.addWidget(self.label_base)
        self.base = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base.sizePolicy().hasHeightForWidth())
        self.base.setSizePolicy(sizePolicy)
        self.base.setMaximumSize(QtCore.QSize(400, 16777215))
        self.base.setObjectName("base")
        self.base.addItem("")
        self.base.addItem("")
        self.base.addItem("")
        self.menu_layout.addWidget(self.base)
        self.label_con1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_con1.sizePolicy().hasHeightForWidth())
        self.label_con1.setSizePolicy(sizePolicy)
        self.label_con1.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_con1.setObjectName("label_con1")
        self.menu_layout.addWidget(self.label_con1)
        self.con1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.con1.sizePolicy().hasHeightForWidth())
        self.con1.setSizePolicy(sizePolicy)
        self.con1.setMaximumSize(QtCore.QSize(400, 16777215))
        self.con1.setObjectName("con1")
        self.con1.addItem("")
        self.con1.addItem("")
        self.con1.addItem("")
        self.menu_layout.addWidget(self.con1)
        self.label_con2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_con2.sizePolicy().hasHeightForWidth())
        self.label_con2.setSizePolicy(sizePolicy)
        self.label_con2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_con2.setObjectName("label_con2")
        self.menu_layout.addWidget(self.label_con2)
        self.con2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.con2.sizePolicy().hasHeightForWidth())
        self.con2.setSizePolicy(sizePolicy)
        self.con2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.con2.setObjectName("con2")
        self.con2.addItem("")
        self.con2.addItem("")
        self.con2.addItem("")
        self.menu_layout.addWidget(self.con2)
        self.button_update = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_update.sizePolicy().hasHeightForWidth())
        self.button_update.setSizePolicy(sizePolicy)
        self.button_update.setMaximumSize(QtCore.QSize(400, 16777215))
        self.button_update.setObjectName("button_update")
        self.menu_layout.addWidget(self.button_update)
        self.label_emitter_fr = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_emitter_fr.sizePolicy().hasHeightForWidth())
        self.label_emitter_fr.setSizePolicy(sizePolicy)
        self.label_emitter_fr.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_emitter_fr.setObjectName("label_emitter_fr")
        self.menu_layout.addWidget(self.label_emitter_fr)
        self.emitter_fr = QtWidgets.QSlider(self.centralwidget)
        self.emitter_fr.setMaximumSize(QtCore.QSize(400, 16777215))
        self.emitter_fr.setMaximum(5)
        self.emitter_fr.setOrientation(QtCore.Qt.Horizontal)
        self.emitter_fr.setObjectName("emitter_fr")
        self.menu_layout.addWidget(self.emitter_fr)
        self.label_base_fr = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_base_fr.sizePolicy().hasHeightForWidth())
        self.label_base_fr.setSizePolicy(sizePolicy)
        self.label_base_fr.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_base_fr.setObjectName("label_base_fr")
        self.menu_layout.addWidget(self.label_base_fr)
        self.base_fr = QtWidgets.QSlider(self.centralwidget)
        self.base_fr.setMaximumSize(QtCore.QSize(400, 16777215))
        self.base_fr.setMinimum(1)
        self.base_fr.setMaximum(5)
        self.base_fr.setOrientation(QtCore.Qt.Horizontal)
        self.base_fr.setInvertedAppearance(False)
        self.base_fr.setInvertedControls(False)
        self.base_fr.setObjectName("base_fr")
        self.menu_layout.addWidget(self.base_fr)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Визуализация работы транзистора"))
        self.lable_type.setText(_translate("MainWindow", "Тип транзистора:"))
        self.tr_type.setItemText(0, _translate("MainWindow", "Биполярный N-P-N транзистор"))
        self.tr_type.setItemText(1, _translate("MainWindow", "Биполярный P-N-P транзистор"))
        self.tr_type.setItemText(2, _translate("MainWindow", "Полевой транзистор с PN затвором и каналом N типа"))
        self.tr_type.setItemText(3, _translate("MainWindow", "Полевой транзистор с PN затвором и каналом P типа"))
        self.tr_type.setItemText(4, _translate("MainWindow", "Полевой транзистор с изолированным затвором и встроенным каналом N типа"))
        self.tr_type.setItemText(5, _translate("MainWindow", "Полевой транзистор с изолированным затвором и встроенным каналом P типа"))
        self.tr_type.setItemText(6, _translate("MainWindow", "Полевой транзистор с изолированным затвором и индуцированным каналом N типа"))
        self.tr_type.setItemText(7, _translate("MainWindow", "Полевой транзистор с изолированным затвором и индуцированным каналом P типа"))
        self.label_base.setText(_translate("MainWindow", "База:"))
        self.base.setItemText(0, _translate("MainWindow", "Нет подключения"))
        self.base.setItemText(1, _translate("MainWindow", "+ питания"))
        self.base.setItemText(2, _translate("MainWindow", "- питания"))
        self.label_con1.setText(_translate("MainWindow", "Контанкт 1:"))
        self.con1.setItemText(0, _translate("MainWindow", "Нет подключения"))
        self.con1.setItemText(1, _translate("MainWindow", "+ питания"))
        self.con1.setItemText(2, _translate("MainWindow", "- питания"))
        self.label_con2.setText(_translate("MainWindow", "Контакт 2:"))
        self.con2.setItemText(0, _translate("MainWindow", "Нет подключения"))
        self.con2.setItemText(1, _translate("MainWindow", "+ питания"))
        self.con2.setItemText(2, _translate("MainWindow", "- питания"))
        self.button_update.setText(_translate("MainWindow", "Установить параметры"))
        self.label_emitter_fr.setText(_translate("MainWindow", "Напряжние на эмиттере, В:"))
        self.label_base_fr.setText(_translate("MainWindow", "Напряжение на базе, В:"))
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