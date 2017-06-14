# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Jun 14 17:18:04 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1084, 749)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(70, 80, 631, 501))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(760, 110, 241, 251))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.address = QtGui.QLineEdit(self.groupBox)
        self.address.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.address.setObjectName(_fromUtf8("address"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.username = QtGui.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(20, 180, 113, 20))
        self.password.setObjectName(_fromUtf8("password"))
        self.input = QtGui.QPushButton(Dialog)
        self.input.setGeometry(QtCore.QRect(420, 610, 75, 23))
        self.input.setObjectName(_fromUtf8("input"))
        self.output = QtGui.QPushButton(Dialog)
        self.output.setGeometry(QtCore.QRect(620, 610, 75, 23))
        self.output.setObjectName(_fromUtf8("output"))
        self.clear = QtGui.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(520, 610, 75, 23))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 610, 131, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 610, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.start = QtGui.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(790, 480, 181, 81))
        self.start.setObjectName(_fromUtf8("start"))
        self.stop = QtGui.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(790, 590, 181, 61))
        self.stop.setObjectName(_fromUtf8("stop"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "账号", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "密码", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "状态", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "实名", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "支付宝", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "企业", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "人脸", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "余额", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "改密码", None))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox", None))
        self.checkBox.setText(_translate("Dialog", "使用代理", None))
        self.input.setText(_translate("Dialog", "导入", None))
        self.output.setText(_translate("Dialog", "导出", None))
        self.clear.setText(_translate("Dialog", "清空", None))
        self.label.setText(_translate("Dialog", "登录成功后更改密码为：", None))
        self.start.setText(_translate("Dialog", "开始", None))
        self.stop.setText(_translate("Dialog", "停止", None))

