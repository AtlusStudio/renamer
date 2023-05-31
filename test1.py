import wx

# 创建应用程序对象
app = wx.App()

# 创建顶级窗口
frame = wx.Frame(None, title="标识示例")

# 创建面板
panel = wx.Panel(frame)

# 创建标签
label = wx.StaticText(panel, label="这是一个很长的文本标签，将被截断显示")
label.Wrap(100)  # 设置换行宽度为100像素

# 显示窗口
frame.Show()

# 进入应用程序主循环
app.MainLoop()