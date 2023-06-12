from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

app = QApplication([])

# 创建主窗口
window = QMainWindow()

# 创建表格
table = QTableWidget(window)

# 添加数据和行列
table.setRowCount(3)
table.setColumnCount(2)

# 向表格添加内容
table.setItem(0, 0, QTableWidgetItem("行1列1"))
table.setItem(0, 1, QTableWidgetItem("行1列2"))
table.setItem(1, 0, QTableWidgetItem("行2列1"))
table.setItem(1, 1, QTableWidgetItem("行2列2"))
table.setItem(2, 0, QTableWidgetItem("行3列1"))
table.setItem(2, 1, QTableWidgetItem("行3列2"))

# 插入新行
table.insertRow(1)
table.setItem(1, 0, QTableWidgetItem("新行列1"))
table.setItem(1, 1, QTableWidgetItem("新行列2"))

window.setCentralWidget(table)
window.show()

app.exec()
