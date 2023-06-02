import wx
import os
import ctypes  # 高分屏适配

from module import function


# ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="renamer", size=(1000, 670),
                         style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        self.Center()
        self.SetBackgroundColour(wx.Colour(245, 245, 245))

        # 创建列表储存所有路径
        self.file_path_exist = []

        # 修正窗口实际宽度
        win_width, win_height = self.GetClientSize()
        rule_width = win_width - 30

        # ListView 表格
        self.list_ctrl = wx.ListView(self, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_EDIT_LABELS)
        self.list_ctrl.SetMinSize((rule_width, 260))
        self.list_ctrl.InsertColumn(0, "文件名")
        self.list_ctrl.InsertColumn(1, "动画名（本季）")
        self.list_ctrl.InsertColumn(2, "动画名（首季）")
        self.list_ctrl.InsertColumn(3, "重命名")
        self.list_ctrl.SetColumnWidth(0, 280)
        self.list_ctrl.SetColumnWidth(1, 180)
        self.list_ctrl.SetColumnWidth(2, 180)
        self.list_ctrl.SetColumnWidth(3, 330)

        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_selected)
        self.list_ctrl.SetDropTarget(DropFolder(self.list_ctrl, self.file_path_exist))

        # 标签容器
        self.edit_frame = wx.StaticBox(self, label="详细信息", size=(rule_width, 0))

        # 图片
        self.image = wx.Image("img/default.jpg", wx.BITMAP_TYPE_ANY)
        self.scaled = self.image.Scale(142, 205, wx.IMAGE_QUALITY_HIGH)
        self.bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(self.scaled))

        # 分割线
        self.label_line1 = wx.StaticLine(self, style=wx.LI_HORIZONTAL)
        self.label_line2 = wx.StaticLine(self, style=wx.LI_HORIZONTAL)

        # 标签
        label_width = win_width - 230

        self.lb_b_jp_name = wx.StaticText(self, label="动画:", style=wx.ALIGN_LEFT)
        self.lb_b_jp_name.SetMinSize((label_width, -1))

        self.lb_b_cn_name = wx.StaticText(self, label="中文名:", style=wx.ALIGN_LEFT)
        self.lb_b_cn_name.SetMinSize((label_width, -1))

        self.lb_b_originate_name = wx.StaticText(self, label="动画系列:", style=wx.ALIGN_LEFT)
        self.lb_b_originate_name.SetMinSize((label_width, -1))

        self.lb_a_type = wx.StaticText(self, label="动画类型:", style=wx.ALIGN_LEFT)
        self.lb_a_type.SetMinSize((label_width, -1))

        self.lb_b_date = wx.StaticText(self, label="放送日期:", style=wx.ALIGN_LEFT)
        self.lb_b_date.SetMinSize((label_width, -1))

        self.lb_file_name = wx.StaticText(self, label="文件名:", style=wx.ALIGN_LEFT)
        self.lb_file_name.SetMinSize((label_width, -1))

        self.lbl_final_rename = wx.StaticText(self, label="重命名结果:", style=wx.ALIGN_LEFT)
        self.lbl_final_rename.SetMinSize((label_width, -1))

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

        # 状态栏
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("这是状态栏")

        # 排列窗口
        LABEL_FRAME = wx.BoxSizer(wx.VERTICAL)
        LABEL_FRAME.Add(self.lb_b_jp_name, 0, wx.TOP | wx.BOTTOM, border=5)
        LABEL_FRAME.Add(self.lb_b_cn_name, 0, wx.TOP | wx.BOTTOM, border=5)
        LABEL_FRAME.Add(self.lb_b_originate_name, 0, wx.TOP | wx.BOTTOM, border=5)
        LABEL_FRAME.Add(self.lb_a_type, 0, wx.TOP | wx.BOTTOM, border=5)
        LABEL_FRAME.Add(self.lb_b_date, 0, wx.TOP | wx.BOTTOM, border=5)
        LABEL_FRAME.Add(self.lb_file_name, 0, wx.TOP, border=15)
        LABEL_FRAME.Add(self.lbl_final_rename, 0, wx.TOP, border=10)

        EDIT_FRAME = wx.StaticBoxSizer(self.edit_frame, wx.HORIZONTAL)
        EDIT_FRAME.Add(self.bitmap, 0, wx.ALL, border=10)
        EDIT_FRAME.Add(LABEL_FRAME, 0, wx.TOP | wx.LEFT, border=10)

        CTRL_FRAME = wx.BoxSizer(wx.HORIZONTAL)
        CTRL_FRAME.Add(self.progress_bar, 0, wx.CENTER)
        CTRL_FRAME.Add(self.clear_button, 0, wx.LEFT, border=15)
        CTRL_FRAME.Add(self.analysis_button, 0, wx.LEFT, border=15)
        CTRL_FRAME.Add(self.rename_button, 0, wx.LEFT, border=15)

        WINDOW = wx.BoxSizer(wx.VERTICAL)
        WINDOW.Add(self.list_ctrl, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=15)
        WINDOW.Add(EDIT_FRAME, 0, wx.ALIGN_CENTER)
        WINDOW.Add(CTRL_FRAME, 0, wx.TOP | wx.LEFT, border=15)

        self.SetSizer(WINDOW)
        print("窗口创建完成，实际宽度" + str(rule_width) + "像素")

    def list_selected(self, event):
        # 获取选择的行数等同于 ID
        list_id = self.list_ctrl.GetFirstSelected()
        list_count = len(self.anime_list)
        list_count = list_count - 1

        # 选中的行是否已经分析过并写入列表
        if list_id <= list_count:
            b_jp_name = self.anime_list[list_id]["b_jp_name"]
            self.lb_b_jp_name.SetLabel(f"动画: {b_jp_name}")

            b_cn_name = self.anime_list[list_id]["b_cn_name"]
            self.lb_b_cn_name.SetLabel(f"中文名: {b_cn_name}")

            b_originate_name = self.anime_list[list_id]["b_originate_name"]
            self.lb_b_originate_name.SetLabel(f"动画系列: {b_originate_name}")

            a_type = self.anime_list[list_id]["a_type"]
            self.lb_a_type.SetLabel(f"动画类型: {a_type}")

            # b_date = self.anime_list[list_id]["b_date"]
            # self.lb_b_date.SetLabel(f"放送日期: {b_date}")

            file_name = self.anime_list[list_id]["file_name"]
            self.lb_file_name.SetLabel(f"文件名: {file_name}")

            final_rename = self.anime_list[list_id]["b_originate_name"]
            self.lbl_final_rename.SetLabel(f"重命名结果: {final_rename}/{final_rename}")

            b_image_path = self.anime_list[list_id]["b_image"]
            b_image_name = os.path.basename(b_image_path)

            self.image = wx.Image(f"img/{b_image_name}", wx.BITMAP_TYPE_ANY)
            self.scaled = self.image.Scale(142, 205, wx.IMAGE_QUALITY_HIGH)
            self.bitmap.SetBitmap(wx.Bitmap(self.scaled))


        else:
            self.lb_b_jp_name.SetLabel("动画:")
            self.lb_b_cn_name.SetLabel("中文名:")
            self.lb_b_originate_name.SetLabel("动画系列:")
            self.lb_a_type.SetLabel("动画类型:")
            # self.lb_b_date.SetLabel(f"放送日期: {b_date}")
            self.lb_file_name.SetLabel("文件名:")
            self.lbl_final_rename.SetLabel("重命名结果:")

    def start_analysis(self, event):
        # 创建列表，写入所有抓取的数据
        self.anime_list = []

        # 调用获取到的文件路径列表
        file_path_exist = self.list_ctrl.GetDropTarget().file_path_exist

        # 判断列表是否为空
        if file_path_exist == set():
            print("请先拖入文件夹")
            # 禁用按钮
            # self.analysis_button.Enable(False)
        else:
            # 循环开始：分析每个文件
            list_id = 0
            for file_path in file_path_exist:

                # 通过文件路径 file_path 获取数据，合并入列表 anime_list
                this_anime_dict = function.get_anime_info(list_id, file_path)
                self.anime_list.append(this_anime_dict)
                print(self.anime_list)

                # 写入listview
                # 如果没有 b_originate_name 说明没有执行到最后一步
                # 重写 file_file 并展示在 listview 避免错位
                this_anime = self.anime_list[list_id]
                if "b_originate_name" in this_anime:
                    file_name = self.anime_list[list_id]["file_name"]
                    b_cn_name = self.anime_list[list_id]["b_cn_name"]
                    b_originate_name = self.anime_list[list_id]["b_originate_name"]
                    self.list_ctrl.SetItem(list_id, 0, file_name)
                    self.list_ctrl.SetItem(list_id, 1, b_cn_name)
                    self.list_ctrl.SetItem(list_id, 2, b_originate_name)
                else:
                    print("该动画未获取到内容，已跳过")

                # 进入下一轮前修改 ID
                list_id += 1

    def on_clear_list(self, event):
        self.list_ctrl.DeleteAllItems()
        self.file_path_exist = []
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
                    self.file_path_exist.append(file_path)
                    print(f"新增了{file_name}")
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
