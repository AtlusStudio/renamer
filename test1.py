import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDropEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(['序号', '文件夹名称'])
        self.tree_widget.setDragEnabled(True)
        self.tree_widget.setAcceptDrops(True)
        self.tree_widget.viewport().setAcceptDrops(True)
        self.tree_widget.setDropIndicatorShown(True)
        self.setCentralWidget(self.tree_widget)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            urls = mime_data.urls()
            for url in urls:
                path = url.toLocalFile()
                folder_name = QTreeWidgetItem([str(self.tree_widget.topLevelItemCount()), path])
                self.tree_widget.addTopLevelItem(folder_name)

            event.acceptProposedAction()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
