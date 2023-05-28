import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="进度条示例")
        
        self.panel = wx.Panel(self)
        
        self.progress_bar = wx.Gauge(self.panel, range=100)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_progress, self.timer)
        self.timer.Start(100)  # 每100毫秒更新一次进度条
        
        self.Show()

    def update_progress(self, event):
        value = self.progress_bar.GetValue()
        if value < 100:
            value += 1
            self.progress_bar.SetValue(value)
        else:
            self.timer.Stop()

app = wx.App()
frame = MyFrame()
app.MainLoop()