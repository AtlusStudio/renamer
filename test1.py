from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QTreeView, QStyledItemDelegate

class CheckBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        value = index.data(Qt.CheckStateRole)
        if value == Qt.Checked:
            checkbox_state = Qt.Checked
        else:
            checkbox_state = Qt.Unchecked

        style = QApplication.style()
        style.drawControl(QApplication.style().CE_CheckBox, option, painter)
        checkbox_rect = style.subElementRect(QApplication.style().SE_CheckBoxContents, option)
        checkbox_rect.moveCenter(option.rect.center())
        painter.drawControl(QApplication.style().CE_CheckBox, option)

    def editorEvent(self, event, model, option, index):
        if event.type() == event.MouseButtonRelease:
            model.setData(index, not index.data(Qt.CheckStateRole), Qt.CheckStateRole)
            return True
        return super().editorEvent(event, model, option, index)

if __name__ == '__main__':
    app = QApplication([])

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['Items'])

    tree_view = QTreeView()
    tree_view.setModel(model)
    tree_view.setItemDelegateForColumn(0, CheckBoxDelegate())

    # 添加示例数据
    for i in range(5):
        item = QStandardItem(f'Item {i+1}')
        item.setCheckable(True)
        item.setCheckState(Qt.Unchecked)
        model.appendRow(item)

    tree_view.show()

    app.exec()
