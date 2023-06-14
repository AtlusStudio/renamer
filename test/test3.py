from PySide6.QtWidgets import QLabel, QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QPainter, QBitmap, QPainterPath, QColor
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 加载图片
        pixmap = QPixmap("image/01.jpg")

        # 创建标签并设置图片
        self.image = QLabel()
        self.image.setMinimumSize(150, 210)
        self.image.setMaximumSize(150, 210)
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)

        # 设置圆角
        rounded_pixmap = self.rounded_pixmap(pixmap)
        self.image.setPixmap(rounded_pixmap)

        # 将标签添加到主窗口
        self.setCentralWidget(self.image)

    def rounded_pixmap(self, pixmap):
        # 创建与图片大小相同的位图
        rounded_bitmap = QBitmap(pixmap.size())
        rounded_bitmap.fill(Qt.transparent)

        # 创建绘图设备
        painter = QPainter(rounded_bitmap)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿

        # 创建圆角矩形路径
        path = QPainterPath()
        path.addRoundedRect(rounded_bitmap.rect(), 10, 10)

        # 使用路径绘制圆角矩形
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)

        painter.end()

        # 创建圆角图片
        rounded_pixmap = pixmap.copy()
        rounded_pixmap.setMask(rounded_bitmap)

        return rounded_pixmap

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
