import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Spacing Example')

        layout = QVBoxLayout()

        label1 = QLabel('Label 1')
        label2 = QLabel('Label 2')
        label3 = QLabel('Label 3')

        # 设置上方间距
        layout.addWidget(label1)
        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
