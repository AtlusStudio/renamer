import wx
import asyncio

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 200))
        panel = wx.Panel(self)
        self.button = wx.Button(panel, label="执行异步操作")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, event):
        asyncio.create_task(self.async_operation())

    async def async_operation(self):
        # 模拟一个耗时的异步操作
        await asyncio.sleep(2)
        print("异步操作完成")

app = wx.App()
frame = MyFrame(None, title="异步操作示例")
frame.Show()
asyncio.get_event_loop().run_forever()
