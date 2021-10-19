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
import csv
from datetime import datetime

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


class Ui_frm_mywh(object):
    def setupUi(self, frm_mywh):
        self.dbpath = "mywh_db.sqlite3"
        self.this = frm_mywh
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

        self.btn_insert.setGeometry(self.btn_save.geometry())
        self.btn_save.setVisible(False)

        self.retranslateUi(frm_mywh)
        QtCore.QMetaObject.connectSlotsByName(frm_mywh)
        frm_mywh.setTabOrder(self.txt_search, self.btn_search)
        frm_mywh.setTabOrder(self.btn_search, self.tbl_items)
        frm_mywh.setTabOrder(self.tbl_items, self.btn_insert)
        frm_mywh.setTabOrder(self.btn_insert, self.btn_save)
        frm_mywh.setTabOrder(self.btn_save, self.btn_export)

        # Event-Driven
        self.setupSearchOrder()
        self.searchDB()
        self.btn_search.clicked.connect(self.searchDB)
        self.btn_insert.clicked.connect(self.cellInsert)
        self.btn_export.clicked.connect(self.exportAsCVS)

    def setupSearchOrder(self):
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                                select * 
                                from vendors;
                                """
            result = conn.execute(sql_command).fetchall()
        self.cmb_vendor.clear()
        self.cmb_vendor.addItem("Show All", -1)
        for i in result:
            self.cmb_vendor.addItem(i["vd_name"], i["vd_id"])
        self.cmb_vendor.view().setMinimumWidth(self.cmb_vendor.minimumSizeHint().width())
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                                select * 
                                from categories;
                                """
            result = conn.execute(sql_command).fetchall()
        self.cmb_cat.clear()
        self.cmb_cat.addItem("Show All", -1)
        for i in result:
            self.cmb_cat.addItem(i["cat_name"], i["cat_id"])
        self.cmb_cat.view().setMinimumWidth(self.cmb_cat.minimumSizeHint().width())
        for i in range(self.cmb_order.count()):
            self.cmb_order.setItemData(i, i)
        # self.cmb_order.setItemText(0, _translate("frm_mywh", "ID ▲"))             2
        # self.cmb_order.setItemText(1, _translate("frm_mywh", "ID ▼"))             2
        # self.cmb_order.setItemText(2, _translate("frm_mywh", "Name (A-Z)"))       3
        # self.cmb_order.setItemText(3, _translate("frm_mywh", "Name (Z-A)"))       3
        # self.cmb_order.setItemText(4, _translate("frm_mywh", "QTY ▲"))            6
        # self.cmb_order.setItemText(5, _translate("frm_mywh", "QTY ▼"))            6
        # self.cmb_order.setItemText(6, _translate("frm_mywh", "Unit Price ▲"))     5
        # self.cmb_order.setItemText(7, _translate("frm_mywh", "Unit Price ▼"))     5
        # self.cmb_order.setItemText(8, _translate("frm_mywh", "Total ▲"))          7
        # self.cmb_order.setItemText(9, _translate("frm_mywh", "Total ▼"))          7
        # self.cmb_order.setItemText(10, _translate("frm_mywh", "Vendor (A-Z)"))    9
        # self.cmb_order.setItemText(11, _translate("frm_mywh", "Vendor (Z-A)"))    9

    def clear_table(self):
        for i in range(self.tbl_items.rowCount()):
            self.tbl_items.removeRow(0)

    # Insert into database
    def saveInsert(self, x):
        response = QtWidgets.QMessageBox.question(None, "Submit Insert",
                                                  "Insert new data. Are you sure?".format(self.selectedRow + 1),
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if response == QtWidgets.QMessageBox.Yes:
            c3 = self.tbl_items.item(self.selectedRow, 3)  # Product Name
            prod_name = c3.text()
            c4 = self.tbl_items.item(self.selectedRow, 4)  # Product Details
            prod_desc = c4.text()
            c5 = self.tbl_items.item(self.selectedRow, 5)  # Product Unit Price
            prod_upc = float(c5.text())
            c6 = self.tbl_items.item(self.selectedRow, 6)  # Product Qty
            prod_qty = int(c6.text())
            c8: QtWidgets.QComboBox = self.tbl_items.cellWidget(self.selectedRow, 8)  # Catagory ID
            cat_id = c8.itemData(c8.currentIndex())
            c9: QtWidgets.QComboBox = self.tbl_items.cellWidget(self.selectedRow, 9)  # Vendor ID
            vd_id = c9.itemData(c9.currentIndex())
            query_data = [prod_name, prod_desc, prod_upc, prod_qty, cat_id, vd_id, datetime.now()]
            column_name = "prod_name,prod_desc,prod_price,prod_qty,cat_id,vd_id,last_modified"
            sql_command = """
                            Insert into Products ({})
                            Values (?,?,?,?,?,?,?);
                            """.format(column_name)
            with sqlite3.connect(self.dbpath) as conn:
                conn.execute(sql_command, query_data)
            self.searchDB()

    # Insert into table
    def cellInsert(self):
        self.disableChange()
        self.selectedRow = 0
        for i in range(self.tbl_items.rowCount()):
            btn = self.tbl_items.cellWidget(i, 0)
            btn.disconnect()
            btn.clicked.connect(self.nonesubmiterror)
            self.tbl_items.cellWidget(i, 1).setEnabled(False)
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                            select *
                            from sqlite_sequence
                            where name = 'PRODUCTS';
                            """
            n_id = int(conn.execute(sql_command).fetchall()[0]["seq"]) + 1
        print("hi")
        self.tbl_items.insertRow(self.selectedRow)
        tempbtn = Wl.WhButton(n_id, self.tbl_items)
        tempbtn.clicked.connect(lambda state, x=tempbtn.id: self.saveInsert(x))
        self.afterRetranslateUi(tempbtn, "Save")
        self.tbl_items.setCellWidget(0, 0, tempbtn)
        c2 = QtWidgets.QTableWidgetItem("{}".format(n_id))
        c2.setFlags(c2.flags() & ~QtCore.Qt.ItemIsEditable)
        c2.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.tbl_items.setItem(self.selectedRow, 2, c2)
        self.tbl_items.setItem(self.selectedRow, 3, QtWidgets.QTableWidgetItem(""))
        self.tbl_items.setItem(self.selectedRow, 4, QtWidgets.QTableWidgetItem(""))
        self.tbl_items.setItem(self.selectedRow, 5, QtWidgets.QTableWidgetItem(""))
        self.tbl_items.setItem(self.selectedRow, 6, QtWidgets.QTableWidgetItem(""))
        c7 = QtWidgets.QTableWidgetItem("")
        c7.setFlags(c7.flags() & ~QtCore.Qt.ItemIsEditable)
        self.tbl_items.setItem(self.selectedRow, 7, c7)
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                                select * 
                                from categories;
                                """
            result = conn.execute(sql_command).fetchall()
        cbx_cat = QtWidgets.QComboBox(self.tbl_items)
        for i in result:
            cbx_cat.addItem(i["cat_name"], i["cat_id"])
        cbx_cat.view().setMinimumWidth(cbx_cat.minimumSizeHint().width())
        self.tbl_items.setCellWidget(self.selectedRow, 8, cbx_cat)
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                                select * 
                                from vendors;
                                """
            result = conn.execute(sql_command).fetchall()
        cbx_cat = QtWidgets.QComboBox(self.tbl_items)
        for i in result:
            cbx_cat.addItem(i["vd_name"], i["vd_id"])
        cbx_cat.view().setMinimumWidth(cbx_cat.minimumSizeHint().width())
        self.tbl_items.setCellWidget(self.selectedRow, 9, cbx_cat)

    def search_cat(self, cat):
        if self.s_cat == "Show All":
            return True
        if self.s_cat == cat:
            print(1)
            return True
        return False

    def search_vd(self, vd):
        if self.s_vd == "Show All":
            return True
        if self.s_vd == vd:
            print(2)
            return True
        return False

    def setSearchOrder(self):
        # Set Vendor
        self.s_vd = self.cmb_vendor.currentText()
        # Set Catagory
        self.s_cat = self.cmb_cat.currentText()
        # Set Order
        if self.cmb_order.currentData() == 0:
            self.tbl_sort_column = 2
            self.tbl_sort_order = QtCore.Qt.AscendingOrder
        if self.cmb_order.currentData() == 1:
            self.tbl_sort_column = 2
            self.tbl_sort_order = QtCore.Qt.DescendingOrder
        if self.cmb_order.currentData() == 2:
            self.tbl_sort_column = 3
            self.tbl_sort_order = QtCore.Qt.AscendingOrder
        if self.cmb_order.currentData() == 3:
            self.tbl_sort_column = 3
            self.tbl_sort_order = QtCore.Qt.DescendingOrder
        if self.cmb_order.currentData() == 4:
            self.tbl_sort_column = 6
            self.tbl_sort_order = QtCore.Qt.AscendingOrder
        if self.cmb_order.currentData() == 5:
            self.tbl_sort_column = 6
            self.tbl_sort_order = QtCore.Qt.DescendingOrder
        if self.cmb_order.currentData() == 6:
            self.tbl_sort_column = 5
            self.tbl_sort_order = QtCore.Qt.AscendingOrder
        if self.cmb_order.currentData() == 7:
            self.tbl_sort_column = 5
            self.tbl_sort_order = QtCore.Qt.DescendingOrder
        if self.cmb_order.currentData() == 8:
            self.tbl_sort_column = 7
            self.tbl_sort_order = QtCore.Qt.AscendingOrder
        if self.cmb_order.currentData() == 9:
            self.tbl_sort_column = 7
            self.tbl_sort_order = QtCore.Qt.DescendingOrder
        if self.cmb_order.currentData() == 10:
            self.tbl_sort_column = 9
            self.tbl_sort_order = QtCore.Qt.AscendingOrder
        if self.cmb_order.currentData() == 11:
            self.tbl_sort_column = 9
            self.tbl_sort_order = QtCore.Qt.DescendingOrder

    def disableChange(self):
        self.btn_search.setEnabled(False)
        self.txt_search.setEnabled(False)
        self.btn_insert.setEnabled(False)
        self.btn_export.setEnabled(False)

    def enableChange(self):
        self.btn_search.setEnabled(True)
        self.txt_search.setEnabled(True)
        self.btn_insert.setEnabled(True)
        self.btn_export.setEnabled(True)

    # Display data
    def searchDB(self):
        self.enableChange()
        self.clear_table()
        self.setSearchOrder()
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
        sort_role = QtCore.Qt.UserRole
        row = 0
        for i in result:
            if self.search_cat(i["cat_name"]) and self.search_vd(i["vd_name"]):
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
                item.setData(sort_role, i["prod_id"])
                self.tbl_items.setItem(row, 2, item)  # Product ID Column
                item = QtWidgets.QTableWidgetItem(i["prod_name"])
                item.setData(sort_role, i["prod_name"])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.tbl_items.setItem(row, 3, item)  # Product Name Column
                item = QtWidgets.QTableWidgetItem(i["prod_desc"])
                item.setData(sort_role, i["prod_desc"])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.tbl_items.setItem(row, 4, item)  # Product Description Column
                # item = QtWidgets.QTableWidgetItem("{:,.2f}".format(i["prod_price"]))
                item = Wl.WhTableNumberItem("{:,.2f}".format(i["prod_price"]))
                item.setData(sort_role, i["prod_price"])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                self.tbl_items.setItem(row, 5, item)  # Product Price Column
                item = Wl.WhTableNumberItem("{:,.0f}".format(i["prod_qty"]))
                item.setData(sort_role, i["prod_qty"])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbl_items.setItem(row, 6, item)  # Product Quantity Column
                item = QtWidgets.QTableWidgetItem("{:,.2f}฿".format(i["prod_price"] * float(i["prod_qty"])))
                item.setData(sort_role, i["prod_price"] * float(i["prod_qty"]))
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                self.tbl_items.setItem(row, 7, item)  # Total Product Value Column
                item = QtWidgets.QTableWidgetItem(i["cat_name"])
                item.setData(sort_role, i["cat_name"])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbl_items.setItem(row, 8, item)  # Product Catagory Column
                item = QtWidgets.QTableWidgetItem(i["vd_name"])
                item.setData(sort_role, i["vd_name"])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tbl_items.setItem(row, 9, item)  # Product Vendor Column
                row += 1
        self.tbl_items.setRowCount(row)
        self.lbl_found.setText("พบ {} รายการ".format(row))
        self.tbl_items.resizeColumnsToContents()
        self.tbl_items.resizeRowsToContents()
        self.tbl_items.sortItems(self.tbl_sort_column, self.tbl_sort_order)
        self.tbl_items.setColumnWidth(0, 60)
        self.tbl_items.setColumnWidth(1, 60)
        self.tbl_items.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

    # Freeze search, allow edit
    def updaterow(self, prod_id):
        self.disableChange()
        for i in range(self.tbl_items.rowCount()):
            if self.tbl_items.item(i, 2).text() == str(prod_id):
                self.selectedRow = i
            btn = self.tbl_items.cellWidget(i, 0)
            btn.disconnect()
            btn.clicked.connect(self.nonesubmiterror)
            self.tbl_items.cellWidget(i, 1).setEnabled(False)
        c0 = self.tbl_items.cellWidget(self.selectedRow, 0)
        self.afterRetranslateUi(c0, "Submit")
        c0.disconnect()
        c0.clicked.connect(lambda state, x=self.selectedRow: self.submitrow())
        font = QtGui.QFont()
        font.setFamily("Kanit Light")
        font.setBold(True)
        font.setPointSize(12)
        c2 = self.tbl_items.item(self.selectedRow, 2)
        c2.setFont(font)
        c3 = self.tbl_items.item(self.selectedRow, 3)
        c3.setFlags(c3.flags() | QtCore.Qt.ItemIsEditable)
        c4 = self.tbl_items.item(self.selectedRow, 4)
        c4.setFlags(c4.flags() | QtCore.Qt.ItemIsEditable)
        c5 = self.tbl_items.item(self.selectedRow, 5)
        c5.setFlags(c5.flags() | QtCore.Qt.ItemIsEditable)
        c6 = self.tbl_items.item(self.selectedRow, 6)
        c6.setFlags(c6.flags() | QtCore.Qt.ItemIsEditable)
        c7 = self.tbl_items.item(self.selectedRow, 7)
        c7.setFont(font)
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                                select * 
                                from categories;
                                """
            result = conn.execute(sql_command).fetchall()
        cbx_cat = QtWidgets.QComboBox(self.tbl_items)
        for i in result:
            cbx_cat.addItem(i["cat_name"], i["cat_id"])
        cbx_cat.view().setMinimumWidth(cbx_cat.minimumSizeHint().width())
        c8 = self.tbl_items.item(self.selectedRow, 8)
        index = cbx_cat.findText(c8.text())
        cbx_cat.setCurrentIndex(index)
        c8.setText("")
        self.tbl_items.setCellWidget(self.selectedRow, 8, cbx_cat)
        with sqlite3.connect(self.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            sql_command = """
                                select * 
                                from vendors;
                                """
            result = conn.execute(sql_command).fetchall()
        cbx_cat = QtWidgets.QComboBox(self.tbl_items)
        for i in result:
            cbx_cat.addItem(i["vd_name"], i["vd_id"])
        cbx_cat.view().setMinimumWidth(cbx_cat.minimumSizeHint().width())
        c9 = self.tbl_items.item(self.selectedRow, 9)
        index = cbx_cat.findText(c9.text())
        cbx_cat.setCurrentIndex(index)
        c9.setText("")
        self.tbl_items.setCellWidget(self.selectedRow, 9, cbx_cat)

    def deleteRow(self, prod_id):
        response = QtWidgets.QMessageBox.question(None, "Delete Row",
                                                  "Delete ID {}. Are you sure?".format(prod_id),
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if response == QtWidgets.QMessageBox.Yes:
            with sqlite3.connect(self.dbpath) as conn:
                sql_command = """
                                Delete From Products
                                Where prod_id = ?;
                                """
                conn.execute(sql_command, [prod_id])
                self.searchDB()

    def exportAsCVS(self):
        # fdl = Wl.WhFileDialog(self)
        save = Wl.WhFileDialog(self.this).getSaveFileName(self.this, "Save File", "Untitled.csv")
        if save[0]:
            with open(file=save[0], mode="w", encoding="utf-8", newline="") as fn:
                fcsv = csv.writer(fn, delimiter=",")
                wd = []
                header = ["Product_ID", "Product_Name", "Product_Description", "Product_Price", "Product_Quantity",
                          "Total_Price", "Category_Name", "Vendor_Name"]
                wd.append(header)
                for i in range(self.tbl_items.rowCount()):
                    data = [self.tbl_items.item(i, 2).text(), self.tbl_items.item(i, 3).text(),
                            self.tbl_items.item(i, 4).text(), self.tbl_items.item(i, 5).text(),
                            self.tbl_items.item(i, 6).text(), self.tbl_items.item(i, 7).text(),
                            self.tbl_items.item(i, 8).text(), self.tbl_items.item(i, 9).text()]
                    wd.append(data)
                fcsv.writerows(wd)

    def nonesubmiterror(self):
        QtWidgets.QMessageBox.about(None, "None Submit Row Detect",
                                    "Row: {} is still in update mode\nOnly one row can be update at a time".format(
                                        self.selectedRow + 1))

    def submitrow(self):
        response = QtWidgets.QMessageBox.question(None, "Submit Change",
                                                  "Change on row {}. Are you sure?".format(self.selectedRow + 1),
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if response == QtWidgets.QMessageBox.Yes:
            c2 = self.tbl_items.item(self.selectedRow, 2)  # Product ID
            prod_id = c2.text()
            c3 = self.tbl_items.item(self.selectedRow, 3)  # Product Name
            prod_name = c3.text()
            c4 = self.tbl_items.item(self.selectedRow, 4)  # Product Details
            prod_desc = c4.text()
            c5 = self.tbl_items.item(self.selectedRow, 5)  # Product Unit Price
            prod_upc = float(c5.text())
            c6 = self.tbl_items.item(self.selectedRow, 6)  # Product Qty
            prod_qty = int(c6.text())
            c8: QtWidgets.QComboBox = self.tbl_items.cellWidget(self.selectedRow, 8)  # Catagory ID
            cat_id = c8.itemData(c8.currentIndex())
            c9: QtWidgets.QComboBox = self.tbl_items.cellWidget(self.selectedRow, 9)  # Vendor ID
            vd_id = c9.itemData(c9.currentIndex())
            query_data = [prod_name, prod_desc, prod_upc, prod_qty, cat_id, vd_id, datetime.now(), prod_id]
            sql_command = """
                        Update Products
                        set prod_name = ?, prod_desc = ?, prod_price = ?, prod_qty = ?, cat_id = ?, vd_id = ?, last_modified = ?
                        where prod_id = ?;
                        """
            with sqlite3.connect(self.dbpath) as conn:
                conn.execute(sql_command, query_data)
            self.searchDB()

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
        self.btn_insert.setToolTip(
            _translate("frm_mywh", "<html><head/><body><p>เพิ่มรายการสินค้า</p></body></html>"))
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
