import wx
import os
import re
import ctypes

from module import function

# ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="renamer", size=(1000, 600), 
            style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        self.Center()
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        # 创建集合用于接收拖入的文件列表
        self.file_path_exist = set()
        
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
        self.list_ctrl.SetDropTarget(DropFolder(self.list_ctrl, self.file_path_exist))
        
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
        # 选择文件夹时输出当前选择的文件名
        selected_item = event.GetItem()
        file_name = self.list_ctrl.GetItemText(selected_item.GetId(), 0)
        print(f"当前选择文件夹: {file_name}")

    def start_analysis(self, event):
        # 调用获取到的文件路径列表
        file_path_exist = self.list_ctrl.GetDropTarget().file_path_exist

        # 加载文件名忽略列表
        ignored_strings = ["BD-BOX", "BD"]

        # 判断列表是否为空
        if file_path_exist == set():
            print("请先拖入文件夹")
            # 禁用按钮
            # self.analysis_button.Enable(False)
        else:
            # 输入忽略列表
            print(f"忽略文件名中的{ignored_strings}")

            # 循环开始：分析每个文件
            for file_path in file_path_exist:
                
                # 将文件路径转为文件名
                file_name = os.path.basename(file_path)
                print(f"正在处理{file_name}")

                # 从文件名提取动画罗马名
                romaji_name = function.get_romaji_name(file_name, ignored_strings)

                if romaji_name == False:
                    print(f"非标准的动画格式: {romaji_name}")
                else:
                    print(f"完成处理：当前动画罗马名为{romaji_name}")



                    
               


    def on_clear_list(self, event):
        self.list_ctrl.DeleteAllItems()
        file_path_exist = set()
        print("已清除所有文件夹")


class DropFolder(wx.FileDropTarget):
    def __init__(self, window, file_path_exist):
        super().__init__()
        self.window = window
        self.file_path_exist = file_path_exist

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
 
                # 调整第一列宽度以适应内容
                # width, height = self.window.GetTextExtent(file_name)
                # width = width + 20
                # if width > 280:
                #     self.window.SetColumnWidth(0, width)
        return True