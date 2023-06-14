from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, Qt
from PySide6.QtCore import Qt, QSize

app = QApplication([])

# 加载图片
pixmap = QPixmap("image/empty.png")

# 创建一个具有圆角的遮罩
rounded_pixmap = QPixmap(pixmap.size())
rounded_pixmap.fill(Qt.transparent)

mask = QPainterPath()
mask.addRoundedRect(rounded_pixmap.rect(), 8, 8)

painter = QPainter(rounded_pixmap)
painter.setRenderHint(QPainter.Antialiasing)
painter.setClipPath(mask)
painter.drawPixmap(0, 0, pixmap)

# 创建一个显示图片的标签
label = QLabel()
label.setPixmap(rounded_pixmap)

# 创建一个窗口并显示标签
window = QWidget()
window.setWindowTitle("Rounded Image")
window.setLayout(QVBoxLayout())
window.layout().addWidget(label)
window.show()

app.exec()
