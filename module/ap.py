import os
from PySide6 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bangumi Renamer")
        self.resize(1000, 670)
        self.setFixedSize(self.size())
        self.setup_ui()
        self.setAcceptDrops(True)

        self.anime_list = []        # 动画列表，存入所有数据
        self.file_path_exist = []   # 动画路径列表（仅用于对比是否存在相同项目）
        self.list_id = 1            # ID 计数器

    def setup_ui(self):
        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.setGeometry(15, 15, 970, 260)
        self.tree.setColumnCount(5)
        self.tree.setHeaderLabels(["ID", "文件名", "动画名（本季）", "动画名（首季）", "重命名"])
        self.tree.setColumnWidth(0, 20)
        self.tree.setColumnWidth(1, 280)
        self.tree.setColumnWidth(2, 170)
        self.tree.setColumnWidth(3, 170)
        self.tree.setColumnWidth(4, 320)
        self.tree.setRootIsDecorated(False)  # 禁止展开树

        # column1 = QtWidgets.QTreeWidgetItem(["1", "Column 2", "Column 3", "Column 4"])
        # self.tree.addTopLevelItem(column1)
        #
        # self.tree.topLevelItem(1).setText(4, "MainWindow")  # 更改内容

        # icon = QtGui.QIcon("../../../Resources/Icons/Python_128px.png")
        # button = QtWidgets.QPushButton(icon, "普通按钮", self)

    # 鼠标进入同时，检测对象是否为 URL 并允许拖放
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    # 鼠标松手以后，在 tree 中展示文件路径，并写入 file_path_exist 列表
    def dropEvent(self, event):
        raw_path_list = event.mimeData().urls()
        for raw_path in raw_path_list:
            # 转换原始格式到文件路径
            file_path = raw_path.toLocalFile()

            # 判断是文件夹还是文件
            if os.path.isdir(file_path):
                file_name = os.path.basename(file_path)
                # 是否存在相同文件夹
                if file_path not in self.file_path_exist:
                    # 写入动画路径列表,用于识别去重
                    self.file_path_exist.append(file_path)

                    # 为当前项目创建字典（第一次）
                    this_anime_list = dict()

                    # 写入刚创建的字典
                    this_anime_list["list_id"] = self.list_id
                    this_anime_list["file_name"] = file_name
                    this_anime_list["file_path"] = file_path

                    # 写入动画列表
                    self.anime_list.append(this_anime_list)

                    # 显示在 tree 中
                    this_column = QtWidgets.QTreeWidgetItem([str(self.list_id), file_name])
                    self.tree.addTopLevelItem(this_column)
                    self.list_id += 1
                    print(f"新增了{file_name}")
                else:
                    print(f"{file_name}已存在")
            else:
                print(f"已过滤文件{file_path}")
