# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(368, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calculator_14445.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Window)
        # self.centralwidget.setMaximumSize(QtCore.QSize(508, 498))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.display = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(55)
        self.display.setFont(font)
        self.display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.verticalLayout.addWidget(self.display)
        self.keyboard = QtWidgets.QGridLayout()
        self.keyboard.setObjectName("keyboard")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setObjectName("button_1")
        self.keyboard.addWidget(self.button_1, 1, 0, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setObjectName("button_2")
        self.keyboard.addWidget(self.button_2, 1, 1, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setObjectName("button_3")
        self.keyboard.addWidget(self.button_3, 1, 2, 1, 1)
        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        self.button_div.setObjectName("button_div")
        self.keyboard.addWidget(self.button_div, 1, 3, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setObjectName("button_4")
        self.keyboard.addWidget(self.button_4, 2, 0, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setObjectName("button_5")
        self.keyboard.addWidget(self.button_5, 2, 1, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setObjectName("button_6")
        self.keyboard.addWidget(self.button_6, 2, 2, 1, 1)
        self.button_mul = QtWidgets.QPushButton(self.centralwidget)
        self.button_mul.setObjectName("button_mul")
        self.keyboard.addWidget(self.button_mul, 2, 3, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setObjectName("button_7")
        self.keyboard.addWidget(self.button_7, 3, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setObjectName("button_8")
        self.keyboard.addWidget(self.button_8, 3, 1, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setObjectName("button_9")
        self.keyboard.addWidget(self.button_9, 3, 2, 1, 1)
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setObjectName("button_minus")
        self.keyboard.addWidget(self.button_minus, 3, 3, 1, 1)
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setObjectName("button_clear")
        self.keyboard.addWidget(self.button_clear, 4, 0, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setObjectName("button_0")
        self.keyboard.addWidget(self.button_0, 4, 1, 1, 1)
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setObjectName("point")
        self.keyboard.addWidget(self.point, 4, 2, 1, 1)
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setObjectName("button_plus")
        self.keyboard.addWidget(self.button_plus, 4, 3, 1, 1)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("delete.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setCheckable(False)
        self.back.setObjectName("back")
        self.keyboard.addWidget(self.back, 5, 0, 1, 1)
        self.button_eq = QtWidgets.QPushButton(self.centralwidget)
        self.button_eq.setObjectName("button_eq")
        self.keyboard.addWidget(self.button_eq, 5, 2, 1, 2)
        self.verticalLayout.addLayout(self.keyboard)
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Calculator"))
        self.display.setText(_translate("Window", "0"))
        self.button_4.setText(_translate("Window", "4"))
        self.button_7.setText(_translate("Window", "7"))
        self.button_2.setText(_translate("Window", "2"))
        self.button_3.setText(_translate("Window", "3"))
        self.button_5.setText(_translate("Window", "5"))
        self.button_9.setText(_translate("Window", "9"))
        self.button_8.setText(_translate("Window", "8"))
        self.button_1.setText(_translate("Window", "1"))
        self.button_0.setText(_translate("Window", "0"))
        self.button_6.setText(_translate("Window", "6"))
        self.button_plus.setText(_translate("Window", "+"))
        self.button_minus.setText(_translate("Window", "-"))
        self.button_mul.setText(_translate("Window", "*"))
        self.button_div.setText(_translate("Window", "/"))
        self.button_eq.setText(_translate("Window", "="))
        self.button_clear.setText(_translate("Window", "C"))
        self.back.setText(_translate("Window", ""))
        self.point.setText(_translate("Window", "."))
