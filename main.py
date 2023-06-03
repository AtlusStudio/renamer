import wx
from PyQt6.QtWidgets import QApplication, QMainWindow

from module import gui
from module.app import Ui_MainWindow


# if __name__ == "__main__":
#     app = wx.App()
#     frame = gui.MyFrame()
#     frame.Show()
#     app.MainLoop()








if __name__ == '__main__':
    # 创建一个 QApplication 实例和一个 QMainWindow 实例
    app = QApplication([])
    window = QMainWindow()

    # 实例化 UI 类，并将其设置为主窗口的内容
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # 显示主窗口并运行应用程序
    window.show()
    app.exec()