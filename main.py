import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from module import gui


if __name__ == "__main__":
    app = QApplication([])
    window = gui.MyWidget()
    icon = QIcon("image/icon.png")
    window.setWindowIcon(icon)
    window.show()
    sys.exit(app.exec())
