from PySide6 import QtCore, QtGui
import sys
from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from function import Ui_MainWindow


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec_()
        QApplication.processEvents()


class ControlBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlBoard, self).__init__()
        self.setupUi(self)
        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)

        self.pushButton.clicked.connect(self.bClicked)

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def bClicked(self):
        """Runs the main function."""
        print('Begin')

        self.printABCD()

        print("End")

    def printABCD(self):
        print("aaaaaaaaaaaaaaaa")
        print("bbbbbbbbbbbbbbbb")
        print("cccccccccccccccc")
        print("dddddddddddddddd")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ControlBoard()
    win.show()
    sys.exit(app.exec_())