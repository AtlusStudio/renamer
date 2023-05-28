import wx
import os
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)



class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="renamer", size=(1000, 600))
        self.Center()
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        # ListView 表格
        list_styles = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_EDIT_LABELS
        self.list_ctrl = wx.ListView(self, style=list_styles)
        self.list_ctrl.SetMaxSize((-1, 260))
        self.list_ctrl.InsertColumn(0, "文件名")
        self.list_ctrl.InsertColumn(1, "中文名")
        self.list_ctrl.InsertColumn(2, "格式化名")
        self.list_ctrl.SetColumnWidth(0, 280)
        self.list_ctrl.SetColumnWidth(1, 260)
        self.list_ctrl.SetColumnWidth(2, 390)
        
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_selected)
        self.list_ctrl.SetDropTarget(DropFolder(self.list_ctrl))
        
        # 标签容器
        self.edit_frame = wx.StaticBox(self, label="修改关联条目", size=(960,100))

        # 清除按钮
        self.clear_button = wx.Button(self, label="Clear List")
        self.clear_button.Bind(wx.EVT_BUTTON, self.on_clear_list)
        
        # 排列窗口
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, border=12)
        
        stsizer = wx.StaticBoxSizer(self.edit_frame, wx.VERTICAL)
        stsizer.Add(self.clear_button, 1, wx.ALIGN_CENTER)

        sizer.Add(stsizer, 0, wx.ALIGN_CENTER)
        self.SetSizer(sizer)
        print("窗口创建完成")
        # print(f"类中的文件夹列表：{file_path_list}")
    
    def list_selected(self, event):
        selected_item = event.GetItem()
        file_name = self.list_ctrl.GetItemText(selected_item.GetId(), 0)
        print(f"当前选择文件夹: {file_name}")
    
    def on_clear_list(self, event):
        # print(DropFolder(MyFrame()).lol)
        self.list_ctrl.DeleteAllItems()


class DropFolder(wx.FileDropTarget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.file_path_exist = set()  # Track inserted folder names
        
    def OnDropFiles(self, x, y, file_path_list):
        print(f"类中的文件夹列表：{file_path_list}")
        for file_path in file_path_list:
            if os.path.isdir(file_path):
                file_name = os.path.basename(file_path)
                if file_path not in self.file_path_exist:  # Check for duplicates
                    self.window.InsertItem(self.window.GetItemCount(), file_name)
                    self.file_path_exist.add(file_path)  # Add inserted folder to set
                    print(f"新增了文件路径：{file_path}")
                    print(f"该文件夹为：{file_name}")
                    print(f"当前文件夹列表为{self.file_path_exist}")

                
                # 调整第一列宽度以适应内容
                # width, height = self.window.GetTextExtent(file_name)
                # width = width + 20
                # if width > 280:
                #     self.window.SetColumnWidth(0, width)
        return True