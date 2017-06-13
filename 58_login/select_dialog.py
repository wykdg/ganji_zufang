# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
#
# Created: Mon Jun 12 10:47:04 2017
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
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(920, 644)
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(90, 40, 711, 351))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.accept = QtGui.QPushButton(Dialog)
        self.accept.setGeometry(QtCore.QRect(450, 500, 75, 23))
        self.accept.setObjectName(_fromUtf8("accept"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 440, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 500, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.account_col = QtGui.QLineEdit(Dialog)
        self.account_col.setGeometry(QtCore.QRect(170, 440, 113, 20))
        self.account_col.setObjectName(_fromUtf8("account_col"))
        self.password_col = QtGui.QLineEdit(Dialog)
        self.password_col.setGeometry(QtCore.QRect(170, 500, 113, 20))
        self.password_col.setObjectName(_fromUtf8("password_col"))
        self.cancle = QtGui.QPushButton(Dialog)
        self.cancle.setGeometry(QtCore.QRect(560, 500, 75, 23))
        self.cancle.setObjectName(_fromUtf8("cancle"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.accept.setText(_translate("Dialog", "确定", None))
        self.label.setText(_translate("Dialog", "账号：", None))
        self.label_2.setText(_translate("Dialog", "密码：", None))
        self.cancle.setText(_translate("Dialog", "取消", None))

