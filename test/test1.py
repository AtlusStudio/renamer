import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget
from test2 import add_column, clear_list


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Program")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.add_button = QPushButton("Add Column")
        self.add_button.clicked.connect(self.add_column_clicked)
        layout.addWidget(self.add_button)

        self.clear_button = QPushButton("Clear List")
        self.clear_button.clicked.connect(self.clear_list_clicked)
        layout.addWidget(self.clear_button)

    def add_column_clicked(self):
        add_column(self.list_widget)

    def clear_list_clicked(self):
        clear_list(self.list_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
