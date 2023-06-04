import wx
import sys

from PySide6 import QtGui, QtWidgets

from module import gui
from module import gui_pyside


# if __name__ == "__main__":
#     app = wx.App()
#     frame = gui.MyFrame()
#     frame.Show()
#     app.MainLoop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = gui_pyside.MyWidget()
    window.show()
    sys.exit(app.exec())
