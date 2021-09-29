# User Generated Classes
from PyQt5 import QtWidgets


class WhButton(QtWidgets.QPushButton):
    def __init__(self, id: str, parent=None):
        super(WhButton, self).__init__(parent=parent)
        self.id = id


class WhTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(WhTableWidget, self).__init__(parent=parent)
        # super().setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Move to individual item
        # super().horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


class WhVerticalScrollbar(QtWidgets.QScrollBar):
    def __init__(self, tbl: QtWidgets.QTableWidget, parent=None):
        super(WhVerticalScrollbar, self).__init__(parent=parent)
        self.tbl = tbl


class WhHorizontalScrollbar(QtWidgets.QScrollBar):
    def __init__(self, tbl: QtWidgets.QTableWidget, parent=None):
        super(WhHorizontalScrollbar, self).__init__(parent=parent)
        self.tbl = tbl
