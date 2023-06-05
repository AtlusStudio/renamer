from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap

app = QApplication([])

window = QWidget()

label = QLabel(window)

pixmap = QPixmap('img/default.jpg')

label.setFixedSize(pixmap.width(), pixmap.height())

# 设置QLabel的背景图片，并自适应大小
label.setPixmap(pixmap)
label.setScaledContents(True)

window.show()

app.exec()
