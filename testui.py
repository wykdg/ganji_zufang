# -*- coding: utf-8 -*-
import pymysql
from PyQt4 import QtGui,QtCore
from UI import Ui_Dialog

class MainWindow(QtGui.QDialog):

    def __init__(self,parent=None):

        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()# Ui_Dialog为.ui产生.py文件中窗体类名
        self.ui.setupUi(self)


        self.ui.treeWidget.setVisible(False)
        self.ui.treeWidget.setColumnCount(8)
        self.ui.treeWidget.setHeaderHidden(True)
        self.ui.treeWidget.setRootIsDecorated(False)
        self.ui.treeWidget.setColumnWidth(2,200)
        for i in range(8):
            self.ui.treeWidget.setColumnHidden(i, True)
        self.ui.treeWidget.setColumnHidden(2,False)
        self.ui.treeWidget.setColumnHidden(3,False)

        self.ui.lineEdit.textChanged.connect(self.tip)
        self.ui.treeWidget.itemClicked.connect(self.auto_complete)






        self.xiaoqu=[]
        completer_list = QtCore.QStringList()
        
        for line in open('xiaoqu.csv','r').readlines():
            data=line.strip().split('\t')
            data=map(lambda x:x.decode('utf8'),data)
            self.xiaoqu.append(data)
            # completer_list.append(data[2])

            
        # completer = QtGui.QCompleter(completer_list)
        # self.ui.lineEdit_2.setCompleter(completer)

    @QtCore.pyqtSlot()
    def hidden_lineEdit(self ):
        self.ui.treeWidget.setVisible(False)

    @QtCore.pyqtSlot(QtCore.QString)
    def tip(self,x):
        # print x
        text=x.__str__()

        self.ui.treeWidget.clear()
        for item in self.xiaoqu:
            if text in item[2]:
                it=QtGui.QTreeWidgetItem(item)
                self.ui.treeWidget.addTopLevelItem(it)
        self.ui.treeWidget.setVisible(True)

    @QtCore.pyqtSlot(QtGui.QTreeWidgetItem)
    def auto_complete(self, item):
        self.ui.lineEdit.setText(item.text(2))
        self.ui.treeWidget.setVisible(False)



if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()
    myapp.show()
    app.exec_()