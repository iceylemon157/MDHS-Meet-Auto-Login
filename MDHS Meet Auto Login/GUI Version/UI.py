# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 522)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"border-image:url(background.jpg);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wait1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.wait1.setFont(font)
        self.wait1.setStyleSheet("QLabel {\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"")
        self.wait1.setAlignment(QtCore.Qt.AlignCenter)
        self.wait1.setObjectName("wait1")
        self.horizontalLayout.addWidget(self.wait1)
        self.auto_enter = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_enter.sizePolicy().hasHeightForWidth())
        self.auto_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setUnderline(False)
        self.auto_enter.setFont(font)
        self.auto_enter.setMouseTracking(False)
        self.auto_enter.setAcceptDrops(True)
        self.auto_enter.setAutoFillBackground(False)
        self.auto_enter.setStyleSheet("QPushButton#auto_enter {\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"")
        self.auto_enter.setObjectName("auto_enter")
        self.horizontalLayout.addWidget(self.auto_enter)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_day = QtWidgets.QLabel(self.centralwidget)
        self.label_day.setStyleSheet("QLabel {\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"")
        self.label_day.setAlignment(QtCore.Qt.AlignCenter)
        self.label_day.setObjectName("label_day")
        self.horizontalLayout_5.addWidget(self.label_day)
        self.box_day = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_day.sizePolicy().hasHeightForWidth())
        self.box_day.setSizePolicy(sizePolicy)
        self.box_day.setStyleSheet("QComboBox {\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"")
        self.box_day.setObjectName("box_day")
        self.horizontalLayout_5.addWidget(self.box_day)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labe_class = QtWidgets.QLabel(self.centralwidget)
        self.labe_class.setStyleSheet("QLabel {\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"")
        self.labe_class.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_class.setObjectName("labe_class")
        self.horizontalLayout_6.addWidget(self.labe_class)
        self.box_class = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_class.sizePolicy().hasHeightForWidth())
        self.box_class.setSizePolicy(sizePolicy)
        self.box_class.setStyleSheet("QComboBox {\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"")
        self.box_class.setObjectName("box_class")
        self.horizontalLayout_6.addWidget(self.box_class)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.manual_enter = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_enter.sizePolicy().hasHeightForWidth())
        self.manual_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.manual_enter.setFont(font)
        self.manual_enter.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255,255,255,200);\n"
"}\n"
"")
        self.manual_enter.setObjectName("manual_enter")
        self.verticalLayout.addWidget(self.manual_enter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.auto_error = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.auto_error.setFont(font)
        self.auto_error.setStyleSheet("QLabel{ color:red; background-color: rgba(255, 255, 255, 200); }")
        self.auto_error.setAlignment(QtCore.Qt.AlignCenter)
        self.auto_error.setObjectName("auto_error")
        self.horizontalLayout_2.addWidget(self.auto_error)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MDHS Auto Meet Login"))
        self.wait1.setText(_translate("MainWindow", "瀏覽器開啟中...\n"
"請耐心等待..."))
        self.auto_enter.setText(_translate("MainWindow", "自動加入課程"))
        self.label_day.setText(_translate("MainWindow", "星期"))
        self.labe_class.setText(_translate("MainWindow", "第幾節課"))
        self.manual_enter.setText(_translate("MainWindow", "手動加入課程"))
        self.label.setText(_translate("MainWindow", "明道 Meet 自動登入程式"))
        self.auto_error.setText(_translate("MainWindow", "錯誤：開啟瀏覽器過程遇到未知錯誤"))
