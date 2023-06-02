import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "ListCtrl Example", size=(400, 300))

        panel = wx.Panel(self, wx.ID_ANY)
        self.list_ctrl = wx.ListCtrl(panel, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_SINGLE_SEL)

        self.list_ctrl.InsertColumn(0, "Name")
        self.list_ctrl.InsertColumn(1, "Age")
        self.list_ctrl.InsertItem(0, "John Doe")
        self.list_ctrl.SetItem(0, 1, "25")
        self.list_ctrl.InsertItem(1, "Jane Smith")
        self.list_ctrl.SetItem(1, 1, "30")

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected, self.list_ctrl)

    def on_item_selected(self, event):
        selected_index = self.list_ctrl.GetFirstSelected()
        print("Selected Row: ", selected_index)

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
