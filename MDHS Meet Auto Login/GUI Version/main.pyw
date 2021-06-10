from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from UI import Ui_MainWindow
from functools import partial
import sys
from for_google_UI import *
import os
import keyboard


class WorkThread(QThread):
    sig = pyqtSignal()

    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        self.sig.emit()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.auto_enter.clicked.connect(self.auto_clicked)
        self.ui.manual_enter.clicked.connect(self.manual_clicked)
        self.setWindowIcon(QtGui.QIcon('sticker.png'))  # icon

        self.login_failed = False
        self.success = False

        self.ui.wait1.hide()
        self.ui.auto_error.hide()

        self.day = [f"Day {i+1}" for i in range(5)]
        self.classes = [f"Class {i + 1}" for i in range(8)]

        self.ui.box_day.addItems(self.day)
        #self.ui.box_day.currentIndexChanged.connect(self.day)

        self.ui.box_class.addItems(self.classes)

        #self.work = WorkThread()
        #self.work1 = WorkThread()
        #self.work2 = WorkThread()

    def login(self, opt='y', day=0, time=0):
        sleep(1)
        print(opt, day, time)
        try:
            Login(opt, day, time)
            self.rev_auto_wait()
            self.ui.auto_error.setText('Meet 成功開啟')
            self.ui.auto_error.show()
        except:
            self.rev_auto_wait()
            self.ui.auto_error.show()
            self.rev_auto_wait()

    def auto_wait(self):
        self.ui.auto_enter.hide()
        self.ui.wait1.show()

    def rev_auto_wait(self):
        self.ui.wait1.hide()
        self.ui.auto_enter.show()

    def auto_clicked(self):
        #self.work = WorkThread()
        #self.work.start()
        #self.work.sig.connect(self.error_hide)
        self.error_hide()
        now = datetime.now()
        day = now.weekday() + 1
        time = now.hour * 60 + now.minute
        if time > 1030 or day > 5 or day < 1:
            self.rev_auto_wait()
            self.ui.auto_error.setText('現在不是上課時間 請使用手動加入會議')
            self.ui.auto_error.show()
            return
        self.work1 = WorkThread()
        self.work2 = WorkThread()
        self.work1.start()
        self.work1.sig.connect(self.auto_wait)
        self.work2.start()
        self.work2.sig.connect(self.login)

    def manual_wait(self):
        day = self.ui.box_day.currentText()
        time = self.ui.box_class.currentText()
        self.login('n', day, time)

    def error_hide(self):
        self.ui.auto_error.hide()
        self.ui.auto_error.setText('錯誤：開啟瀏覽器過程遇到未知錯誤')

    def manual_clicked(self):
        self.work3 = WorkThread()
        self.work3.start()
        self.work3.sig.connect(self.error_hide)
        self.work = WorkThread()
        self.work.start()
        self.work.sig.connect(self.manual_wait)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    # keyboard.add_hotkey('enter', window.click)
    window.show()
    sys.exit(app.exec_())
