from PySide6.QtWidgets import QListWidgetItem


def add_column(list_widget):
    item = QListWidgetItem("lox")
    list_widget.addItem(item)


def clear_list(list_widget):
    list_widget.clear()
