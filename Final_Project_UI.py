# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final_Project_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 661, 501))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(670, 10, 281, 501))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.num1 = QtWidgets.QPushButton(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(670, 520, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QPushButton(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(760, 520, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num2.setFont(font)
        self.num2.setObjectName("num2")
        self.num3 = QtWidgets.QPushButton(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(850, 520, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num3.setFont(font)
        self.num3.setObjectName("num3")
        self.num4 = QtWidgets.QPushButton(self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(670, 600, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num4.setFont(font)
        self.num4.setObjectName("num4")
        self.num5 = QtWidgets.QPushButton(self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(760, 600, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num5.setFont(font)
        self.num5.setObjectName("num5")
        self.num6 = QtWidgets.QPushButton(self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(850, 600, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num6.setFont(font)
        self.num6.setObjectName("num6")
        self.num7 = QtWidgets.QPushButton(self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(670, 680, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num7.setFont(font)
        self.num7.setObjectName("num7")
        self.num8 = QtWidgets.QPushButton(self.centralwidget)
        self.num8.setGeometry(QtCore.QRect(760, 680, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num8.setFont(font)
        self.num8.setObjectName("num8")
        self.num9 = QtWidgets.QPushButton(self.centralwidget)
        self.num9.setGeometry(QtCore.QRect(850, 680, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num9.setFont(font)
        self.num9.setObjectName("num9")
        self.num0 = QtWidgets.QPushButton(self.centralwidget)
        self.num0.setGeometry(QtCore.QRect(760, 760, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.num0.setFont(font)
        self.num0.setObjectName("num0")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(140, 720, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.clearall = QtWidgets.QPushButton(self.centralwidget)
        self.clearall.setGeometry(QtCore.QRect(270, 720, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.clearall.setFont(font)
        self.clearall.setObjectName("clearall")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 520, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.itemlist = QtWidgets.QPushButton(self.centralwidget)
        self.itemlist.setGeometry(QtCore.QRect(10, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.itemlist.setFont(font)
        self.itemlist.setObjectName("itemlist")
        self.itemnum = QtWidgets.QPushButton(self.centralwidget)
        self.itemnum.setGeometry(QtCore.QRect(140, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.itemnum.setFont(font)
        self.itemnum.setObjectName("itemnum")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(270, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.newitem = QtWidgets.QPushButton(self.centralwidget)
        self.newitem.setGeometry(QtCore.QRect(10, 660, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.newitem.setFont(font)
        self.newitem.setObjectName("newitem")
        self.sellnow = QtWidgets.QPushButton(self.centralwidget)
        self.sellnow.setGeometry(QtCore.QRect(270, 660, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.sellnow.setFont(font)
        self.sellnow.setObjectName("sellnow")
        self.refuse = QtWidgets.QPushButton(self.centralwidget)
        self.refuse.setGeometry(QtCore.QRect(140, 780, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.refuse.setFont(font)
        self.refuse.setObjectName("refuse")
        self.sellall = QtWidgets.QPushButton(self.centralwidget)
        self.sellall.setGeometry(QtCore.QRect(140, 660, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.sellall.setFont(font)
        self.sellall.setObjectName("sellall")
        self.Errorlabel = QtWidgets.QLabel(self.centralwidget)
        self.Errorlabel.setGeometry(QtCore.QRect(410, 600, 231, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.Errorlabel.setFont(font)
        self.Errorlabel.setText("")
        self.Errorlabel.setObjectName("Errorlabel")
        self.updateprice = QtWidgets.QPushButton(self.centralwidget)
        self.updateprice.setGeometry(QtCore.QRect(10, 720, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.updateprice.setFont(font)
        self.updateprice.setObjectName("updateprice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Final_Project"))
        self.num1.setText(_translate("MainWindow", "1"))
        self.num2.setText(_translate("MainWindow", "2"))
        self.num3.setText(_translate("MainWindow", "3"))
        self.num4.setText(_translate("MainWindow", "4"))
        self.num5.setText(_translate("MainWindow", "5"))
        self.num6.setText(_translate("MainWindow", "6"))
        self.num7.setText(_translate("MainWindow", "7"))
        self.num8.setText(_translate("MainWindow", "8"))
        self.num9.setText(_translate("MainWindow", "9"))
        self.num0.setText(_translate("MainWindow", "0"))
        self.cancel.setText(_translate("MainWindow", "取消交易"))
        self.clearall.setText(_translate("MainWindow", "清除"))
        self.itemlist.setText(_translate("MainWindow", "商品清單"))
        self.itemnum.setText(_translate("MainWindow", "數量"))
        self.check.setText(_translate("MainWindow", "確定結帳"))
        self.newitem.setText(_translate("MainWindow", "登入新品項"))
        self.sellnow.setText(_translate("MainWindow", "銷售狀況"))
        self.refuse.setText(_translate("MainWindow", "退貨"))
        self.sellall.setText(_translate("MainWindow", "銷售額"))
        self.updateprice.setText(_translate("MainWindow", "更新售價"))
