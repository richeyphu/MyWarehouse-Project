# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywarehouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_mywh(object):
    def setupUi(self, frm_mywh):
        frm_mywh.setObjectName("frm_mywh")
        frm_mywh.resize(1000, 770)
        frm_mywh.setMinimumSize(QtCore.QSize(1000, 770))
        frm_mywh.setMaximumSize(QtCore.QSize(1000, 770))
        self.tbl_items = QtWidgets.QTableWidget(frm_mywh)
        self.tbl_items.setGeometry(QtCore.QRect(20, 150, 961, 561))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.tbl_items.setFont(font)
        self.tbl_items.setObjectName("tbl_items")
        self.tbl_items.setColumnCount(7)
        self.tbl_items.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setItem(0, 6, item)
        self.txt_search = QtWidgets.QLineEdit(frm_mywh)
        self.txt_search.setGeometry(QtCore.QRect(570, 110, 310, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.txt_search.setFont(font)
        self.txt_search.setObjectName("txt_search")
        self.btn_search = QtWidgets.QPushButton(frm_mywh)
        self.btn_search.setGeometry(QtCore.QRect(890, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.btn_export = QtWidgets.QPushButton(frm_mywh)
        self.btn_export.setGeometry(QtCore.QRect(890, 720, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_export.setFont(font)
        self.btn_export.setObjectName("btn_export")
        self.btn_save = QtWidgets.QPushButton(frm_mywh)
        self.btn_save.setGeometry(QtCore.QRect(790, 720, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.lbl_header = QtWidgets.QLabel(frm_mywh)
        self.lbl_header.setGeometry(QtCore.QRect(0, 0, 1001, 91))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(30)
        self.lbl_header.setFont(font)
        self.lbl_header.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.lbl_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header.setObjectName("lbl_header")
        self.lbl_credit = QtWidgets.QLabel(frm_mywh)
        self.lbl_credit.setGeometry(QtCore.QRect(10, 740, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.lbl_credit.setFont(font)
        self.lbl_credit.setObjectName("lbl_credit")
        self.lbl_found = QtWidgets.QLabel(frm_mywh)
        self.lbl_found.setGeometry(QtCore.QRect(20, 110, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit")
        font.setPointSize(16)
        self.lbl_found.setFont(font)
        self.lbl_found.setObjectName("lbl_found")
        self.btn_insert = QtWidgets.QPushButton(frm_mywh)
        self.btn_insert.setGeometry(QtCore.QRect(590, 720, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_insert.setFont(font)
        self.btn_insert.setObjectName("btn_insert")
        self.btn_edit = QtWidgets.QPushButton(frm_mywh)
        self.btn_edit.setGeometry(QtCore.QRect(690, 720, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")

        self.retranslateUi(frm_mywh)
        QtCore.QMetaObject.connectSlotsByName(frm_mywh)
        frm_mywh.setTabOrder(self.txt_search, self.btn_search)
        frm_mywh.setTabOrder(self.btn_search, self.tbl_items)
        frm_mywh.setTabOrder(self.tbl_items, self.btn_insert)
        frm_mywh.setTabOrder(self.btn_insert, self.btn_edit)
        frm_mywh.setTabOrder(self.btn_edit, self.btn_save)
        frm_mywh.setTabOrder(self.btn_save, self.btn_export)

    def retranslateUi(self, frm_mywh):
        _translate = QtCore.QCoreApplication.translate
        frm_mywh.setWindowTitle(_translate("frm_mywh", "My Warehouse"))
        item = self.tbl_items.verticalHeaderItem(0)
        item.setText(_translate("frm_mywh", "1"))
        item = self.tbl_items.horizontalHeaderItem(1)
        item.setText(_translate("frm_mywh", "ID"))
        item = self.tbl_items.horizontalHeaderItem(2)
        item.setText(_translate("frm_mywh", "Name"))
        item = self.tbl_items.horizontalHeaderItem(3)
        item.setText(_translate("frm_mywh", "Description"))
        item = self.tbl_items.horizontalHeaderItem(4)
        item.setText(_translate("frm_mywh", "Unit Price"))
        item = self.tbl_items.horizontalHeaderItem(5)
        item.setText(_translate("frm_mywh", "QTY"))
        item = self.tbl_items.horizontalHeaderItem(6)
        item.setText(_translate("frm_mywh", "Total"))
        __sortingEnabled = self.tbl_items.isSortingEnabled()
        self.tbl_items.setSortingEnabled(False)
        item = self.tbl_items.item(0, 1)
        item.setText(_translate("frm_mywh", "21000001"))
        item = self.tbl_items.item(0, 2)
        item.setText(_translate("frm_mywh", "ปลากระพง"))
        item = self.tbl_items.item(0, 3)
        item.setText(_translate("frm_mywh", "ปลาสด ๆ ตกจากทะเล"))
        item = self.tbl_items.item(0, 4)
        item.setText(_translate("frm_mywh", "300"))
        item = self.tbl_items.item(0, 5)
        item.setText(_translate("frm_mywh", "3"))
        item = self.tbl_items.item(0, 6)
        item.setText(_translate("frm_mywh", "900"))
        self.tbl_items.setSortingEnabled(__sortingEnabled)
        self.btn_search.setText(_translate("frm_mywh", "Search"))
        self.btn_export.setText(_translate("frm_mywh", "Export"))
        self.btn_save.setText(_translate("frm_mywh", "Save"))
        self.lbl_header.setText(_translate("frm_mywh", "My Warehouse"))
        self.lbl_credit.setText(_translate("frm_mywh", "Developed by DidITired House Co., Ltd."))
        self.lbl_found.setText(_translate("frm_mywh", "พบ 1 รายการ"))
        self.btn_insert.setText(_translate("frm_mywh", "Insert"))
        self.btn_edit.setText(_translate("frm_mywh", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_mywh = QtWidgets.QWidget()
    ui = Ui_frm_mywh()
    ui.setupUi(frm_mywh)
    frm_mywh.show()
    sys.exit(app.exec_())
