from PySide6 import QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bangumi Renamer")
        self.resize(1000, 670)
        self.setFixedSize(self.size())
        self.setup_ui()

    def setup_ui(self) -> None:
        icon = QtGui.QIcon("../../../Resources/Icons/Python_128px.png")
        # 1. 单个参数
        # button = QtWidgets.QPushButton()
        # button.setParent(self)  # 创建时父对象为None,可用setParent方法指定
        # button.setText("普通按钮")  # 设置按钮上的文字
        # button.setIcon(icon)  # 设置按钮上的图标

        # 2. 两个参数
        # button = QtWidgets.QPushButton("普通按钮", self)

        # 3. 三个参数
        button = QtWidgets.QPushButton(icon, "普通按钮", self)

        model = QtWidgets.QTreeView()
