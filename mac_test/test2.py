# wx创建了mac原生样式的表格

import wx
import os
import wx.dataview

class MyFrame(wx.Frame):
    def __init__(self):
        # 应该是wx用来定义窗口的语句
        super().__init__(None, title="Table View Demo", size=(500, 300))
        
        panel = wx.Panel(self)
        
        # 创建表格
        dataview = wx.dataview.DataViewCtrl(panel, style=wx.dataview.DV_ROW_LINES)
        datamodel = wx.dataview.DataViewListStore()
        dataview.AssociateModel(datamodel)
        
        # 添加列
        dataview.AppendToggleColumn("", 0, width=20).SetSortable(False)
        dataview.AppendTextColumn("Items", 1, width=200)
        dataview.AppendTextColumn("Items2", 2, width=200)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(dataview, 1, wx.EXPAND)
        
        panel.SetSizer(sizer)
        
        # 添加示例数据
        datamodel.AppendItem(["Item 1"])
        datamodel.AppendItem(["Item 2"])
        datamodel.AppendItem(["Item 3"])
    
    def on_item_selected(self, event):
        selected_item = dataview.GetSelection()
        item_text = dataview.GetTextValue(selected_item, 0)
        print("Selected Item:", item_text)




app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
