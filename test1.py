import wx
import sys

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Print to StatusBar Example')
        self.panel = wx.Panel(self)
        self.status_bar = self.CreateStatusBar()

        # 重定向输出到状态栏
        sys.stdout = StatusBarPrint(self.status_bar)

        # 测试输出
        print("Hello, World!")

        self.Show()

class StatusBarPrint:
    def __init__(self, status_bar):
        self.status_bar = status_bar

    def write(self, text):
        self.status_bar.SetStatusText(text.strip())

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
