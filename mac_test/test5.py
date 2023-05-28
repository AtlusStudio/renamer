import wx
import os
import ctypes

# ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="renamer", size=(1000, 600), 
            style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        self.Center()
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        
        # 修正窗口实际宽度
        win_width, win_height = self.GetClientSize()
        rule_width = win_width - 30

        # ListView 表格
        self.list_ctrl = wx.ListView(self, 
            style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_EDIT_LABELS)
        self.list_ctrl.SetMinSize((rule_width, 260))
        self.list_ctrl.InsertColumn(0, "文件名")
        self.list_ctrl.InsertColumn(1, "中文名")
        self.list_ctrl.InsertColumn(2, "格式化名")
        self.list_ctrl.SetColumnWidth(0, 280)
        self.list_ctrl.SetColumnWidth(1, 260)
        self.list_ctrl.SetColumnWidth(2, 390)
        
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_selected)
        self.list_ctrl.SetDropTarget(DropFolder(self.list_ctrl))
        
        # 标签容器
        self.edit_frame = wx.StaticBox(self, label="修改关联条目", size=(rule_width,0))

        # 占位
        self.lol = wx.Button(self, label="Clear List")

        # 进度条
        self.progress_bar = wx.Gauge(self, range=100)
        process_bar_width = rule_width - 345
        self.progress_bar.SetMinSize((process_bar_width, 20))

        # 清除按钮
        self.clear_button = wx.Button(self, label="清除全部")
        self.clear_button.SetMinSize((100, 32))
        self.clear_button.Bind(wx.EVT_BUTTON, self.on_clear_list)

        # 识别按钮
        self.analysis_button = wx.Button(self, label="开始识别")
        self.analysis_button.SetMinSize((100, 32))
        self.analysis_button.Bind(wx.EVT_BUTTON, self.start_analysis)

        # 重命名按钮
        self.rename_button = wx.Button(self, label="重命名全部")
        self.rename_button.SetMinSize((100, 32))
        
        # 排列窗口
        WINDOW = wx.BoxSizer(wx.VERTICAL)
        WINDOW.Add(self.list_ctrl, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=15)
        
        EDIT_FRAME = wx.StaticBoxSizer(self.edit_frame, wx.VERTICAL)
        EDIT_FRAME.Add(self.lol, 0, wx.ALIGN_CENTER)

        CTRL_FRAME = wx.BoxSizer(wx.HORIZONTAL)
        CTRL_FRAME.Add(self.progress_bar, 0, wx.CENTER)
        CTRL_FRAME.Add(self.clear_button, 0, wx.LEFT, border=15)
        CTRL_FRAME.Add(self.analysis_button, 0, wx.LEFT, border=15)
        CTRL_FRAME.Add(self.rename_button, 0, wx.LEFT, border=15)

        WINDOW.Add(EDIT_FRAME, 0, wx.ALIGN_CENTER)
        WINDOW.Add(CTRL_FRAME, 0, wx.TOP | wx.LEFT, border=15)

        self.SetSizer(WINDOW)
        print("窗口创建完成，实际宽度" + str(rule_width) + "像素")
    
    def list_selected(self, event):
        selected_item = event.GetItem()
        file_name = self.list_ctrl.GetItemText(selected_item.GetId(), 0)
        print(f"当前选择文件夹: {file_name}")

    def start_analysis(self, event):
    	print(file_path_exist)

    def on_clear_list(self, event):
        self.list_ctrl.DeleteAllItems()
        print("已清除所有文件夹")


class DropFolder(wx.FileDropTarget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.file_path_exist = set()
   
    def OnDropFiles(self, x, y, file_path_list):
        for file_path in file_path_list:
            # 判断是否为文件夹
            if os.path.isdir(file_path):
                file_name = os.path.basename(file_path)
                # 判断是否存在相同文件夹，并写入 file_path_exist 列表
                if file_path not in self.file_path_exist:
                    self.window.InsertItem(self.window.GetItemCount(), file_name)
                    self.file_path_exist.add(file_path)
                    print(f"新增了{file_name}")
                    print(f"总路径列表：{self.file_path_exist}")
                else:
                    print(f"{file_name}已存在")
            else:
                print(f"已过滤文件{file_path}")
        return True
用中文说一下，上述代码，如何在start_analysis函数中获取被OnDropFiles函数修改后的file_path_exist变量值