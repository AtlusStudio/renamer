from PySide6 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bangumi Renamer")
        self.resize(1000, 670)
        self.setFixedSize(self.size())
        self.setup_ui()

    def setup_ui(self) -> None:
        # icon = QtGui.QIcon("../../../Resources/Icons/Python_128px.png")
        # button = QtWidgets.QPushButton(icon, "普通按钮", self)

        tree = QtWidgets.QTreeWidget(self)
        tree.setGeometry(15, 15, 970, 260)
        tree.setColumnCount(5)
        tree.setHeaderLabels(["ID", "文件名", "动画名（本季）", "动画名（首季）", "重命名"])
        tree.setColumnWidth(0, 20)
        tree.setColumnWidth(1, 280)
        tree.setColumnWidth(2, 170)
        tree.setColumnWidth(3, 170)
        tree.setColumnWidth(4, 320)
        tree.setRootIsDecorated(False)  # 禁止展开树








        column1 = QtWidgets.QTreeWidgetItem(["1", "Column 2", "Column 3", "Column 4"])
        tree.addTopLevelItem(column1)

        column2 = QtWidgets.QTreeWidgetItem(["2", "Column 2", "Column 3", "Column 4"])
        tree.addTopLevelItem(column2)

        tree.topLevelItem(1).setText(4, "MainWindow")  # 更改内容用的


