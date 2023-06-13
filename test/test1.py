import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from test2 import Calculator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Result: ", self)
        self.label.setGeometry(20, 20, 260, 30)

        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(20, 60, 180, 30)

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.setGeometry(20, 100, 80, 30)

        self.calculator = Calculator(self.input_box)
        self.calculator.result_calculated.connect(self.update_label)

        self.calculate_button.clicked.connect(self.calculator.calculate)

    def update_label(self, result):
        self.label.setText(f"Result: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
