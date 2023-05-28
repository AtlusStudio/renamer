import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="固定尺寸的StaticBox示例")

        panel = wx.Panel(self)

        # 创建一个静态框
        static_box = wx.StaticBox(panel, label="固定尺寸的框", size=(2000, 1500))
        
        # 创建一个静态框尺寸器，将静态框添加到其中
        sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)
        
        # 在静态框尺寸器中添加其他控件
        label = wx.StaticText(panel, label="这是一个静态框尺寸器示例")
        sizer.Add(label, 0, wx.ALL, 10)
        
        # 设置主面板的布局管理器为静态框尺寸器
        panel.SetSizer(sizer)
        
        # 自适应布局
        sizer.Fit(self)
        
        self.Show()


app = wx.App()
frame = MyFrame(None)
app.MainLoop()
