import wx
import ssl
import urllib.request


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="插入网络图片", size=(400, 300))
        panel = wx.Panel(self)

        ssl._create_default_https_context = ssl._create_unverified_context

        # 网络图片的URL
        image_url = "https://lain.bgm.tv/pic/cover/l/21/a1/292238_u43yn.jpg"

        # 下载图片并创建wx.Image对象
        image_data = urllib.request.urlopen(image_url).read()
        image = wx.Image(1, 1)  # 创建一个空的wx.Image对象
        image.LoadFile(wx.InputStream(image_data))

        # 调整图片大小
        image.Rescale(200, 200)

        # 创建wx.Bitmap对象
        bitmap = wx.Bitmap(image)

        # 创建显示图片的静态位图控件
        bitmap_ctrl = wx.StaticBitmap(panel, bitmap=bitmap)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(bitmap_ctrl, 0, wx.ALL, 10)
        panel.SetSizerAndFit(sizer)


app = wx.App()
frame = MyFrame(None)
frame.Show()
app.MainLoop()
