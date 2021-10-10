# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywarehouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import WHLib as Wl
import sqlite3
import locale

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


class Ui_frm_mywh(object):
    def setupUi(self, frm_mywh):
        self.dbpath = "mywh_db.sqlite3"
        frm_mywh.setObjectName("frm_mywh")
        frm_mywh.resize(1000, 770)
        frm_mywh.setMinimumSize(QtCore.QSize(1000, 770))
        frm_mywh.setMaximumSize(QtCore.QSize(1000, 770))
        self.tbl_items = Wl.WhTableWidget(frm_mywh)
        self.tbl_items.setGeometry(QtCore.QRect(20, 153, 961, 561))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.tbl_items.setFont(font)
        self.tbl_items.setObjectName("tbl_items")
        self.tbl_items.setColumnCount(10)
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
        self.tbl_items.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setHorizontalHeaderItem(9, item)
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
        item = QtWidgets.QTableWidgetItem()
        self.tbl_items.setItem(0, 7, item)
        self.txt_search = QtWidgets.QLineEdit(frm_mywh)
        self.txt_search.setGeometry(QtCore.QRect(670, 114, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.txt_search.setFont(font)
        self.txt_search.setObjectName("txt_search")
        self.btn_search = QtWidgets.QPushButton(frm_mywh)
        self.btn_search.setGeometry(QtCore.QRect(890, 114, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.btn_export = QtWidgets.QPushButton(frm_mywh)
        self.btn_export.setGeometry(QtCore.QRect(890, 723, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_export.setFont(font)
        self.btn_export.setObjectName("btn_export")
        self.btn_save = QtWidgets.QPushButton(frm_mywh)
        self.btn_save.setGeometry(QtCore.QRect(790, 723, 91, 31))
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
        self.lbl_found.setGeometry(QtCore.QRect(20, 713, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(14)
        self.lbl_found.setFont(font)
        self.lbl_found.setObjectName("lbl_found")
        self.btn_insert = QtWidgets.QPushButton(frm_mywh)
        self.btn_insert.setGeometry(QtCore.QRect(690, 723, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(12)
        self.btn_insert.setFont(font)
        self.btn_insert.setObjectName("btn_insert")
        self.cmb_order = QtWidgets.QComboBox(frm_mywh)
        self.cmb_order.setGeometry(QtCore.QRect(540, 114, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(11)
        self.cmb_order.setFont(font)
        self.cmb_order.setObjectName("cmb_order")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_order.addItem("")
        self.cmb_cat = QtWidgets.QComboBox(frm_mywh)
        self.cmb_cat.setGeometry(QtCore.QRect(320, 114, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(11)
        self.cmb_cat.setFont(font)
        self.cmb_cat.setObjectName("cmb_cat")
        self.cmb_cat.addItem("")
        self.cmb_vendor = QtWidgets.QComboBox(frm_mywh)
        self.cmb_vendor.setGeometry(QtCore.QRect(20, 114, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(11)
        self.cmb_vendor.setFont(font)
        self.cmb_vendor.setObjectName("cmb_vendor")
        self.cmb_vendor.addItem("")
        self.lbl_found_2 = QtWidgets.QLabel(frm_mywh)
        self.lbl_found_2.setGeometry(QtCore.QRect(21, 95, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.lbl_found_2.setFont(font)
        self.lbl_found_2.setObjectName("lbl_found_2")
        self.lbl_found_3 = QtWidgets.QLabel(frm_mywh)
        self.lbl_found_3.setGeometry(QtCore.QRect(321, 95, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.lbl_found_3.setFont(font)
        self.lbl_found_3.setObjectName("lbl_found_3")
        self.lbl_found_4 = QtWidgets.QLabel(frm_mywh)
        self.lbl_found_4.setGeometry(QtCore.QRect(543, 94, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setPointSize(10)
        self.lbl_found_4.setFont(font)
        self.lbl_found_4.setObjectName("lbl_found_4")

        self.retranslateUi(frm_mywh)
        QtCore.QMetaObject.connectSlotsByName(frm_mywh)
        frm_mywh.setTabOrder(self.txt_search, self.btn_search)
        frm_mywh.setTabOrder(self.btn_search, self.tbl_items)
        frm_mywh.setTabOrder(self.tbl_items, self.btn_insert)
        frm_mywh.setTabOrder(self.btn_insert, self.btn_save)
        frm_mywh.setTabOrder(self.btn_save, self.btn_export)

        # Event-Driven
        self.tbl_sort_column: int = 2
        self.tbl_sort_order: int = QtCore.Qt.AscendingOrder
        self.btn_save.setEnabled(False)
        self.searchDB()
        self.btn_search.clicked.connect(self.searchDB)
        self.btn_save.clicked.connect(self.saveUpdate)
        self.btn_insert.clicked.connect(self.cellInsert)

    def clear_table(self):
        for i in range(self.tbl_items.rowCount()):
            self.tbl_items.removeRow(0)

    def saveUpdate(self):
        if self.btn_save.isEnabled():
            # Save stuff
            self.btn_save.setEnabled(False)

    def saveInsert(self, x):
        self.btn_insert.setEnabled(True)

        c2 = self.tbl_items.item(0, 2)
        c3 = self.tbl_items.item(0, 3)
        c4 = self.tbl_items.item(0, 4)
        c5 = self.tbl_items.item(0, 5)

    def cellInsert(self):
        self.btn_insert.setEnabled(False)
        self.btn_save.setEnabled(True)
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                            select * 
                            from products
                            ORDER BY Prod_id DESC
                            LIMIT 1;
                            """
            result = conn.execute(sql_command).fetchall()
        n_id = result[0]["prod_id"] + 1
        self.tbl_items.insertRow(0)
        tempbtn = Wl.WhButton(n_id, self.tbl_items)
        tempbtn.clicked.connect(lambda state, x=tempbtn.id: self.saveInsert(x))
        self.afterRetranslateUi(tempbtn, "Save")
        self.tbl_items.setCellWidget(0, 0, tempbtn)
        c2 = QtWidgets.QTableWidgetItem("{}".format(n_id))
        c2.setFlags(c2.flags() & ~QtCore.Qt.ItemIsEditable)
        c2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.tbl_items.setItem(0, 1, c2)
        self.tbl_items.setItem(0, 2, QtWidgets.QTableWidgetItem(""))
        self.tbl_items.setItem(0, 3, QtWidgets.QTableWidgetItem(""))
        self.tbl_items.setItem(0, 4, QtWidgets.QTableWidgetItem(""))
        self.tbl_items.setItem(0, 5, QtWidgets.QTableWidgetItem(""))
        c6 = QtWidgets.QTableWidgetItem("")
        c6.setFlags(c6.flags() & ~QtCore.Qt.ItemIsEditable)
        self.tbl_items.setItem(0, 6, c6)

    def searchDB(self):
        self.clear_table()
        search_text = '%' + self.txt_search.text() + '%'
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                                select * 
                                from products p join categories c 
                                on p.cat_id = c.cat_id
                                join vendors v 
                                on p.vd_id = v.vd_id
                                where prod_id like ?
                                or prod_name like ?
                                or prod_desc like ?;
                                """
            result = conn.execute(sql_command, [search_text, search_text, search_text]).fetchall()
        self.tbl_items.setRowCount(len(result))
        self.lbl_found.setText("พบ {} รายการ".format(len(result)))
        row = 0
        for i in result:
            tempbtn = Wl.WhButton(i["prod_id"], self.tbl_items)
            tempbtn.clicked.connect(lambda state, x=tempbtn.id: self.updaterow(x))
            self.afterRetranslateUi(tempbtn, "Update")
            self.tbl_items.setCellWidget(row, 0, tempbtn)  # Update Button Column
            tempbtn = Wl.WhButton(i["prod_id"], self.tbl_items)
            tempbtn.clicked.connect(lambda state, x=tempbtn.id: self.deleteRow(x))
            self.afterRetranslateUi(tempbtn, "Delete")
            self.tbl_items.setCellWidget(row, 1, tempbtn)  # Delete Button Column
            item = QtWidgets.QTableWidgetItem(str(i["prod_id"]))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.tbl_items.setItem(row, 2, item)  # Product ID Column
            item = QtWidgets.QTableWidgetItem(i["prod_name"])
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.tbl_items.setItem(row, 3, item)  # Product Name Column
            item = QtWidgets.QTableWidgetItem(i["prod_desc"])
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.tbl_items.setItem(row, 4, item)  # Product Description Column
            item = QtWidgets.QTableWidgetItem("{:,.2f}".format(i["prod_price"]))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tbl_items.setItem(row, 5, item)  # Product Price Column
            item = QtWidgets.QTableWidgetItem("{:,.0f}".format(i["prod_qty"]))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tbl_items.setItem(row, 6, item)  # Product Quantity Column
            item = QtWidgets.QTableWidgetItem("{:,.2f}฿".format(float(i["prod_price"]) * float(i["prod_qty"])))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tbl_items.setItem(row, 7, item)  # Total Product Value Column
            item = QtWidgets.QTableWidgetItem(i["cat_name"])
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tbl_items.setItem(row, 8, item)  # Product Quantity Column
            item = QtWidgets.QTableWidgetItem(i["vd_name"])
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tbl_items.setItem(row, 9, item)  # Product Quantity Column
            row += 1
        self.tbl_items.resizeColumnsToContents()
        self.tbl_items.resizeRowsToContents()
        self.tbl_items.sortItems(self.tbl_sort_column, self.tbl_sort_order)
        self.tbl_items.setColumnWidth(0, 60)
        self.tbl_items.setColumnWidth(1, 60)
        self.tbl_items.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

    def updaterow(self, prod_id: str):
        for i in range(self.tbl_items.rowCount()):
            if self.tbl_items.item(i, 1).text() == str(prod_id):
                self.row = i
            btn = self.tbl_items.cellWidget(i, 0)
            btn.disconnect()
            btn.clicked.connect(self.nonesubmiterror)
        c0 = self.tbl_items.cellWidget(self.row, 0)
        self.afterRetranslateUi(c0, "Submit")
        c0.disconnect()
        c0.clicked.connect(lambda state, x=self.row: self.submitrow(x))
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setBold(True)
        font.setPointSize(12)
        c1 = self.tbl_items.item(self.row, 1)
        c1.setFont(font)
        c2 = self.tbl_items.item(self.row, 2)
        c2.setFlags(c2.flags() | QtCore.Qt.ItemIsEditable)
        c3 = self.tbl_items.item(self.row, 3)
        c3.setFlags(c3.flags() | QtCore.Qt.ItemIsEditable)
        c4 = self.tbl_items.item(self.row, 4)
        c4.setFlags(c4.flags() | QtCore.Qt.ItemIsEditable)
        c5 = self.tbl_items.item(self.row, 5)
        c5.setFlags(c5.flags() | QtCore.Qt.ItemIsEditable)
        c6 = self.tbl_items.item(self.row, 6)
        c6.setFont(font)

    def deleteRow(self):
        pass

    def nonesubmiterror(self):
        QtWidgets.QMessageBox.about(None, "None Submit Row Detect",
                                    "Row: {} is still in update mode\nOnly one row can be update at a time".format(
                                        self.row + 1))

    def submitrow(self, row: int):
        response = QtWidgets.QMessageBox.question(None, "Submit Change",
                                                  "Change on row {}. Are you sure?".format(row + 1),
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if response == QtWidgets.QMessageBox.Yes:
            for i in range(self.tbl_items.rowCount()):
                btn = self.tbl_items.cellWidget(i, 0)
                btn.disconnect()
                btn.clicked.connect(lambda state, x=btn.id: self.updaterow(x))
                self.afterRetranslateUi(btn, "Update")
            font = QtGui.QFont()
            font.setFamily("Kanit Light")
            font.setBold(False)
            font.setPointSize(12)
            c1 = self.tbl_items.item(row, 1)
            c1.setFont(font)
            c2 = self.tbl_items.item(row, 2)
            c2.setFlags(c2.flags() & ~QtCore.Qt.ItemIsEditable)
            c3 = self.tbl_items.item(row, 3)
            c3.setFlags(c3.flags() & ~QtCore.Qt.ItemIsEditable)
            c4 = self.tbl_items.item(row, 4)
            c4.setFlags(c4.flags() & ~QtCore.Qt.ItemIsEditable)
            c5 = self.tbl_items.item(row, 5)
            c5.setFlags(c5.flags() & ~QtCore.Qt.ItemIsEditable)
            c6 = QtWidgets.QTableWidgetItem(
                "{:,.2f}฿".format(locale.atof(c4.text()) * locale.atof(c5.text())))
            c6.setFont(font)
            c6.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tbl_items.setItem(row, 6, c6)
            self.btn_save.setEnabled(True)
            self.tbl_items.resizeColumnsToContents()
            self.tbl_items.resizeRowsToContents()

    def afterRetranslateUi(self, btn: QtWidgets.QPushButton, text: str):
        _translate = QtCore.QCoreApplication.translate
        btn.setText(_translate("frm_mywh", text))

    def retranslateUi(self, frm_mywh):
        _translate = QtCore.QCoreApplication.translate
        frm_mywh.setWindowTitle(_translate("frm_mywh", "My Warehouse"))
        item = self.tbl_items.verticalHeaderItem(0)
        item.setText(_translate("frm_mywh", "1"))
        item = self.tbl_items.horizontalHeaderItem(2)
        item.setText(_translate("frm_mywh", "ID"))
        item = self.tbl_items.horizontalHeaderItem(3)
        item.setText(_translate("frm_mywh", "Name"))
        item = self.tbl_items.horizontalHeaderItem(4)
        item.setText(_translate("frm_mywh", "Description"))
        item = self.tbl_items.horizontalHeaderItem(5)
        item.setText(_translate("frm_mywh", "Unit Price"))
        item = self.tbl_items.horizontalHeaderItem(6)
        item.setText(_translate("frm_mywh", "QTY"))
        item = self.tbl_items.horizontalHeaderItem(7)
        item.setText(_translate("frm_mywh", "Total"))
        item = self.tbl_items.horizontalHeaderItem(8)
        item.setText(_translate("frm_mywh", "Category"))
        item = self.tbl_items.horizontalHeaderItem(9)
        item.setText(_translate("frm_mywh", "Vendor"))
        __sortingEnabled = self.tbl_items.isSortingEnabled()
        self.tbl_items.setSortingEnabled(False)
        item = self.tbl_items.item(0, 2)
        item.setText(_translate("frm_mywh", "21000001"))
        item = self.tbl_items.item(0, 3)
        item.setText(_translate("frm_mywh", "ปลากระพง"))
        item = self.tbl_items.item(0, 4)
        item.setText(_translate("frm_mywh", "ปลาสด ๆ ตกจากทะเล"))
        item = self.tbl_items.item(0, 5)
        item.setText(_translate("frm_mywh", "300"))
        item = self.tbl_items.item(0, 6)
        item.setText(_translate("frm_mywh", "3"))
        item = self.tbl_items.item(0, 7)
        item.setText(_translate("frm_mywh", "900"))
        self.tbl_items.setSortingEnabled(__sortingEnabled)
        self.txt_search.setToolTip(_translate("frm_mywh", "<html><head/><body><p>ค้นหาสินค้า</p></body></html>"))
        self.btn_search.setToolTip(_translate("frm_mywh", "<html><head/><body><p>ค้นหา</p></body></html>"))
        self.btn_search.setText(_translate("frm_mywh", "Search"))
        self.btn_export.setToolTip(
            _translate("frm_mywh", "<html><head/><body><p>ส่งออกรายการสินค้าเป็นไฟล์ CSV</p></body></html>"))
        self.btn_export.setText(_translate("frm_mywh", "Export"))
        self.btn_save.setText(_translate("frm_mywh", "Save"))
        self.lbl_header.setText(_translate("frm_mywh", "My Warehouse"))
        self.lbl_credit.setText(_translate("frm_mywh", "Developed by DidITired House Co., Ltd."))
        self.lbl_found.setText(_translate("frm_mywh", "พบ {0} รายการ"))
        self.btn_insert.setToolTip(_translate("frm_mywh", "<html><head/><body><p>เพิ่มรายการสินค้า</p></body></html>"))
        self.btn_insert.setText(_translate("frm_mywh", "Insert"))
        self.cmb_order.setToolTip(_translate("frm_mywh", "<html><head/><body><p>จัดเรียงตาม</p></body></html>"))
        self.cmb_order.setItemText(0, _translate("frm_mywh", "ID ▲"))
        self.cmb_order.setItemText(1, _translate("frm_mywh", "ID ▼"))
        self.cmb_order.setItemText(2, _translate("frm_mywh", "Name (A-Z)"))
        self.cmb_order.setItemText(3, _translate("frm_mywh", "Name (Z-A)"))
        self.cmb_order.setItemText(4, _translate("frm_mywh", "QTY ▲"))
        self.cmb_order.setItemText(5, _translate("frm_mywh", "QTY ▼"))
        self.cmb_order.setItemText(6, _translate("frm_mywh", "Unit Price ▲"))
        self.cmb_order.setItemText(7, _translate("frm_mywh", "Unit Price ▼"))
        self.cmb_order.setItemText(8, _translate("frm_mywh", "Total ▲"))
        self.cmb_order.setItemText(9, _translate("frm_mywh", "Total ▼"))
        self.cmb_order.setItemText(10, _translate("frm_mywh", "Vendor (A-Z)"))
        self.cmb_order.setItemText(11, _translate("frm_mywh", "Vendor (Z-A)"))
        self.cmb_cat.setToolTip(_translate("frm_mywh", "<html><head/><body><p>ประเภทสินค้า</p></body></html>"))
        self.cmb_cat.setItemText(0, _translate("frm_mywh", "Show All"))
        self.cmb_vendor.setToolTip(_translate("frm_mywh", "<html><head/><body><p>ประเภทสินค้า</p></body></html>"))
        self.cmb_vendor.setItemText(0, _translate("frm_mywh", "Show All"))
        self.lbl_found_2.setText(_translate("frm_mywh", "Vendor"))
        self.lbl_found_3.setText(_translate("frm_mywh", "Category"))
        self.lbl_found_4.setText(_translate("frm_mywh", "Order by"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.ico"))
    frm_mywh = QtWidgets.QWidget()
    ui = Ui_frm_mywh()
    ui.setupUi(frm_mywh)
    frm_mywh.show()
    sys.exit(app.exec_())
