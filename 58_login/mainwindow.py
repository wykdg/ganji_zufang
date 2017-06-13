# -*- coding: utf-8 -*-
import win32ras
import pymysql
from PyQt4 import QtGui,QtCore
from UI import Ui_Dialog
import select_dialog
from login_58 import Login_58
import threadpool
import urllib
import check_proxy
import threading
import Queue
import time

class MainWindow(QtGui.QDialog):

    def __init__(self,parent=None):

        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()# Ui_Dialog为.ui产生.py文件中窗体类名
        self.ui.setupUi(self)

        self.ui.input.clicked.connect(self.input)
        self.ui.output.clicked.connect(self.output)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.start.clicked.connect(self.start)
        self.ui.stop.clicked.connect(self.stop)
        self.queue=Queue.Queue()
        self.ip_lock=threading.Lock()
        self.pid=None
        # self.encrpy=vvv8.Enerypt_58()

    @QtCore.pyqtSlot()
    def start(self):
        threading.Thread(target=self.start1).start()
    def start1(self):

        pool=threadpool.ThreadPool(21)
        # if self.ui.checkBox.checkState() == 2:
        #     order=self.ui.order.text().__str__()
        #     self.apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order
        # else:
        #     self.apiUrl=None

        self.new_pwd=self.ui.lineEdit_6.text().__str__()
        # for i in range(self.ui.tableWidget.rowCount()):
        # threading.Thread(target=self.get_ip).start()
        reqs = threadpool.makeRequests(self.logining, range(self.ui.tableWidget.rowCount()))
        [pool.putRequest(req) for req in reqs]
        pool.wait()

    # def get_ip(self):
    #     while self.apiUrl:
    #
    #         res = urllib.urlopen(self.apiUrl).read().strip("\n")
    #                 # 按照\n分割获取到的IP
    #         ips = res.split("\n")
    #         # 随机选择一个IP
    #         proxy = ips[0]
    #         if check_proxy.proxy_check(proxy) is True:
    #             self.queue.put(proxy)

    def change_ip(self):
        while True:
            if self.change is True:
                self.ip_lock.acquire()


    def logining(self,i):
        account=self.ui.tableWidget.item(i,0).text().__str__()
        password = self.ui.tableWidget.item(i, 1).text().__str__()
        print account,password
        # time.sleep(5)
        proxy = None
        if self.pid is None:
            self.pid,ret=win32ras.Dial(None, None, ('vpn', 'zzzh.8866.org', "", 'a1365', '1', ""), None)
            print self.pid

        # if self.apiUrl:
        #     proxy=self.queue.get()

        # if proxy is None:
        #
        #     while self.apiUrl:
        #         res = urllib.urlopen(self.apiUrl).read().strip("\n")
        #         # 按照\n分割获取到的IP
        #         ips = res.split("\n")
        #         # 随机选择一个IP
        #         proxy = ips[0]
        #         if check_proxy.proxy_check(proxy) is True:
        #             break
        try:
            a=Login_58(account,password,proxy=proxy)
            login_re=a.login()
            if login_re['code']in (0,1,3):
                self.queue.put(proxy)
        except:
            login_re={'code':2}
        if login_re['code'] is 0:
            self.ui.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(u"登录成功"))

            auth=a.get_auth()
            if auth:
                if auth[3] is True:
                    self.ui.tableWidget.setItem(i,6,QtGui.QTableWidgetItem(u"已认证"))
                else:
                    self.ui.tableWidget.setItem(i, 6, QtGui.QTableWidgetItem(u"未认证"))

                if auth[0] is True:
                    self.ui.tableWidget.setItem(i,3,QtGui.QTableWidgetItem(u"已认证"))
                else:
                    self.ui.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(u"未认证"))

                if auth[2] is True:
                    self.ui.tableWidget.setItem(i,4,QtGui.QTableWidgetItem(u"已认证"))
                else:
                    self.ui.tableWidget.setItem(i, 4, QtGui.QTableWidgetItem(u"未认证"))

                if (auth[100] and auth[500] and auth[501]) is True:
                    self.ui.tableWidget.setItem(i,5,QtGui.QTableWidgetItem(u"已认证"))
                else:
                    self.ui.tableWidget.setItem(i, 5, QtGui.QTableWidgetItem(u"未认证"))


            print auth
            money=a.get_money()
            if money:
                self.ui.tableWidget.setItem(i, 7, QtGui.QTableWidgetItem(str(money)))
            if self.new_pwd:
                pwd_modify=a.modify_password(self.new_pwd)
                if pwd_modify is True:
                    self.ui.tableWidget.setItem(i, 8, QtGui.QTableWidgetItem(u"修改密码成功"))
                else:
                    self.ui.tableWidget.setItem(i, 8, QtGui.QTableWidgetItem(pwd_modify))
        else:
            if login_re["code"]==2 :
                win32ras.HangUp(self.pid)
                self.pid=None
                self.logining(i)
            self.ui.tableWidget.setItem(i,2,QtGui.QTableWidgetItem(login_re["msg"]))


    @QtCore.pyqtSlot()
    def stop(self):

        pass

    @QtCore.pyqtSlot()
    def input(self):
        dialog=QtGui.QDialog()
        ui=select_dialog.Ui_Dialog()
        ui.setupUi(dialog)
        ui.accept.clicked.connect(dialog.accept)
        ui.cancle.clicked.connect(dialog.reject)
        path=QtGui.QFileDialog().getOpenFileName()
        data=[]
        for line in open(path.__str__()).readlines():
            line=line.decode('utf-8')
            data.append(line.strip().split('----'))
        col_num=len(data[0])
        ui.treeWidget.setColumnCount(col_num)
        ui.treeWidget.setColumnWidth(0,200)
        for item in data:
            it = QtGui.QTreeWidgetItem(item)
            ui.treeWidget.addTopLevelItem(it)

        if dialog.exec_():
            # print ui.account_col
            account_col=int(ui.account_col.text().__str__())
            pwd_col=int(ui.password_col.text().__str__())
            print account_col,pwd_col

            for item in data:
                row=self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(item[account_col]))
                self.ui.tableWidget.setItem(row,1,QtGui.QTableWidgetItem(item[pwd_col]))
        dialog.destroy()


    @QtCore.pyqtSlot()
    def output(self):
        if self.ui.tableWidget.rowCount()==0:
            QtGui.QMessageBox.information(self, u"导出", u'没有数据')
            return
        path = QtGui.QFileDialog().getSaveFileName()
        try:
            with open(path,'wb') as ff:
                for i in range(self.ui.tableWidget.rowCount()):
                    for j in range(self.ui.tableWidget.columnCount()):
                        item=self.ui.tableWidget.item(i, j)
                        if item:
                            ff.write(item.text().__str__())
                        else:
                            ff.write('')
                        ff.write('----')

                    ff.write('\n')
        except:
            QtGui.QMessageBox.information(self, u"导出", u'导出失败')
            return
        QtGui.QMessageBox.information(self,u"导出",u'导出成功')
    @QtCore.pyqtSlot()
    def clear(self):
        while self.ui.tableWidget.rowCount()>0:
            self.ui.tableWidget.removeRow(0)


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()
    myapp.show()
    app.exec_()