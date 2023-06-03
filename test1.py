# wx实现了拖放显示内容的效果
# 仅显示文件夹

import wx
import os


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="renamer", size=(1000, 600))
        self.Center()
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        # 创建 ListView 表格
        list_styles = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_EDIT_LABELS
        self.list_ctrl = wx.ListView(self, style=list_styles)
        self.list_ctrl.SetMaxSize((-1, 400))
        self.list_ctrl.InsertColumn(0, "文件名")
        self.list_ctrl.InsertColumn(1, "中文名")
        self.list_ctrl.InsertColumn(2, "格式化名")
        self.list_ctrl.SetColumnWidth(0, 260)
        self.list_ctrl.SetColumnWidth(1, 280)
        self.list_ctrl.SetColumnWidth(2, 390)
        
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_item_selected)
        
        self.list_ctrl.Bind(wx.EVT_LIST_BEGIN_DRAG, self.on_begin_drag)
        self.list_ctrl.Bind(wx.EVT_LIST_BEGIN_RDRAG, self.on_begin_drag)
        
        self.list_ctrl.SetDropTarget(FolderDropTarget(self.list_ctrl))
        
        self.clear_button = wx.Button(self, label="Clear List")
        self.clear_button.Bind(wx.EVT_BUTTON, self.on_clear_list)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=25)
        sizer.Add(self.clear_button, 0, wx.ALIGN_CENTER)
        self.SetSizer(sizer)
    
    def on_item_selected(self, event):
        selected_item = event.GetItem()
        folder_name = self.list_ctrl.GetItemText(selected_item.GetId(), 0)
        print(f"Selected Folder: {folder_name}")
    
    def on_begin_drag(self, event):
        selected_item = self.list_ctrl.GetFirstSelected()
        folder_name = self.list_ctrl.GetItemText(selected_item, 0)
        folder_path = os.path.join(os.getcwd(), folder_name)
        
        data = wx.FileDataObject()
        data.AddFile(folder_path)
        
        drop_source = wx.DropSource(self.list_ctrl)
        drop_source.SetData(data)
        
        drop_source.DoDragDrop()
    
    def on_clear_list(self, event):
        self.list_ctrl.DeleteAllItems()


class FolderDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        
    def OnDropFiles(self, x, y, filenames):
        for file_path in filenames:
            if os.path.isdir(file_path):  # 仅处理文件夹
                folder_name = os.path.basename(file_path)
                index = self.window.InsertItem(self.window.GetItemCount(), folder_name)
                
                # 调整第一列宽度以适应内容
                self.window.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        
        return True



app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()

