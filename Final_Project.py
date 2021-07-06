from pymongo import MongoClient
from PyQt5.QtWidgets import *
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from Final_Project_UI import Ui_MainWindow
from Final_Project_NewItem_UI import Ui_MainWindow as Ui_SubWindow
from Final_Project_UpdatePrice_UI import Ui_MainWindow as Ui_Subwindow_2
import sys
import re
import datetime

client = MongoClient("mongodb+srv://password:mongo123456@cluster0.1njut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.final
collection = db.item
collection2 = db.sells
document = [{"name":"冰拿鐵", "price":60}, 
            {"name":"卡布奇諾", "price":60},
            {"name":"黑咖啡", "price":50},
            {"name":"鴛鴦奶茶", "price":65},
            {"name":"義式濃縮", "price":55},
            {"name":"抹茶拿鐵", "price":65},
            {"name":"手工餅乾", "price":50},
            {"name":"法式吐司", "price":40},
]
#collection.insert_many(document)

#global value
item_price = 0
item_num = 0
total_price = 0
item_name = ''
item_dict = {}
refuse_chk = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.num0.clicked.connect(self.num0)
        self.ui.num1.clicked.connect(self.num1)
        self.ui.num2.clicked.connect(self.num2)
        self.ui.num3.clicked.connect(self.num3)
        self.ui.num4.clicked.connect(self.num4)
        self.ui.num5.clicked.connect(self.num5)
        self.ui.num6.clicked.connect(self.num6)
        self.ui.num7.clicked.connect(self.num7)
        self.ui.num8.clicked.connect(self.num8)
        self.ui.num9.clicked.connect(self.num9)
        self.ui.clearall.clicked.connect(self.clear)
        self.ui.itemlist.clicked.connect(self.itemlist)
        self.ui.itemnum.clicked.connect(self.itemunm)
        self.ui.check.clicked.connect(self.check)
        self.ui.cancel.clicked.connect(self.cancel)
        self.ui.refuse.clicked.connect(self.refuse)
        self.ui.sellnow.clicked.connect(self.sellnow)
        self.ui.sellall.clicked.connect(self.sellall)
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止修改表格內容
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)#根據內容一格可以多行
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#自動將表格水平標題平均分配
        self.ui.tableView.verticalHeader().setVisible(False)#隱藏縱向座標
    #數字鍵
    def num0(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('0')
        elif str_chk != None:
            str_new = str_chk + '0'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num1(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('1')
        elif str_chk != None:
            str_new = str_chk + '1'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num2(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('2')
        elif str_chk != None:
            str_new = str_chk + '2'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num3(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('3')
        elif str_chk != None:
            str_new = str_chk + '3'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num4(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('4')
        elif str_chk != None:
            str_new = str_chk + '4'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num5(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('5')
        elif str_chk != None:
            str_new = str_chk + '5'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num6(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('6')
        elif str_chk != None:
            str_new = str_chk + '6'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num7(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('7')
        elif str_chk != None:
            str_new = str_chk + '7'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num8(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('8')
        elif str_chk != None:
            str_new = str_chk + '8'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num9(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('9')
        elif str_chk != None:
            str_new = str_chk + '9'
            self.ui.plainTextEdit.setPlainText(str_new)
    #清除
    def clear(self):
        self.ui.plainTextEdit.clear()
    #商品清單
    def itemlist(self):
        global refuse_chk
        refuse_chk = 0
        result = list(collection.find({}, {"_id":0, "name":1, "price":1}))
        self.model = QStandardItemModel(len(result), 2)
        self.model.setHorizontalHeaderLabels(['品項', '價格'])
        for row in range(len(result)):
            for col in range(2):
                r_dict = dict(result[row])
                if col == 0:
                    item = QStandardItem(r_dict['name'])
                if col == 1:
                    item = QStandardItem(str(r_dict['price']))
                self.model.setItem(row, col, item)
        self.ui.tableView.setModel(self.model)
    #數量
    def itemunm(self):
        global refuse_chk
        refuse_chk = 0
        num = self.ui.plainTextEdit.toPlainText()
        if num == '':
            self.ui.Errorlabel.setText('商品數量錯誤')
        elif num != '':
            self.ui.Errorlabel.setText('')
            global item_num 
            item_num = int(num)
            item = self.ui.tableView.currentIndex().data()
            if item == None:
                self.ui.Errorlabel.setText('尚未選擇商品')
            elif item != None:
                #self.ui.Errorlabel.setText('')
                result = list(collection.find({"name":str(item)}, {"_id":0, "price":1}))
                p = dict(result[0])
                global item_price, item_name, total_price, item_dict
                item_price = p['price']
                item_name = item
                total_price += item_num*item_price
                item_dict[item] = 'x' + str(item_num)

                check = str(item_dict)
                check_list = re.sub(r'[\'{}:]', '', check)
                check_list = check_list.replace(' ', '')
                check_res = re.sub(',', '\n',check_list)

                self.ui.textBrowser.clear()
                self.ui.textBrowser.append(check_res + '\n\n金額累計:' + str(total_price))
                self.ui.plainTextEdit.clear()
                self.ui.tableView.setShowGrid(True)          
    #結帳
    def check(self):
        global refuse_chk
        refuse_chk = 0
        global item_dict, total_price
        check = str(item_dict)
        check_list = re.sub(r'[\'{}:]','',check)
        check_list = check_list.replace(' ', '')
        check_store = re.sub(',', '\n',check_list)
        check_msgbox = re.sub(',', '\n',check_list)
        check_msg = QMessageBox()
        check_msg.setStyleSheet('QMessageBox{font-size:25px;}\nQPushButton{font-size:20px;}')
        money = self.ui.plainTextEdit.toPlainText()
        if money == '':#避免忘記輸入付款金額
            self.ui.Errorlabel.setText('付款金額尚未輸入')
        elif money != '':
            self.ui.Errorlabel.setText('')
            money_int = int(money)
            cash = money_int - total_price
            check_msg.setWindowTitle('結帳')
            check_msg.setText('總金額:' + str(total_price) + '\n' + 
                            '找零:' + str(cash) + '\n\n' + 
                            '品項:' + '\n' + check_msgbox)
            check_msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            reValue = check_msg.exec()
            if reValue == QMessageBox.Ok:
                sell_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                collection2.insert_many([{"item":str(check_store), "Total":int(total_price), "time":str(sell_time)}])
                self.ui.Errorlabel.setText("找零：" + str(cash))
                self.ui.textBrowser.clear()
                self.ui.plainTextEdit.clear()
                total_price = 0
                item_dict = {}
            elif reValue == QMessageBox.Cancel:
                self.ui.plainTextEdit.clear()
            check_msg.show()
    #取消
    def cancel(self):
        global refuse_chk
        refuse_chk = 0
        self.ui.textBrowser.clear()
        global total_price, item_dict
        total_price = 0
        item_dict = {}
    #銷售狀況
    def sellnow(self):
        self.ui.Errorlabel.setText('')
        global refuse_chk
        refuse_chk = 1
        result = list(collection2.find({}, {"_id":0, "item":1, "Total":1, "time":1}))
        self.model = QStandardItemModel(len(result), 3)
        self.model.setHorizontalHeaderLabels(['品項', '價格', '時間'])
        for row in range(len(result)):
            for col in range(3):
                r_dict = dict(result[row])
                if col == 0:
                    item = QStandardItem(r_dict['item'])
                if col == 1:
                    item = QStandardItem(str(r_dict['Total']))
                if col == 2:
                    item = QStandardItem(r_dict['time'])
                self.model.setItem(row, col, item)
        self.ui.tableView.setModel(self.model)
    #退貨
    def refuse(self):
        global refuse_chk
        if refuse_chk != 1:
            self.ui.Errorlabel.setText('尚未進入銷售狀況頁面')
        else:
            target = self.ui.tableView.currentIndex().data()
            if target == None:
                self.ui.Errorlabel.setText('選擇日期欄位進行刪除')
            elif len(target) != 19:
                self.ui.Errorlabel.setText('選擇日期欄位進行刪除')
            elif len(target) == 19:
                self.ui.Errorlabel.clear()
                collection2.delete_one({"time":str(target)})
            result = list(collection2.find({}, {"_id":0, "item":1, "Total":1, "time":1}))
            self.model = QStandardItemModel(len(result), 3)
            self.model.setHorizontalHeaderLabels(['品項', '價格', '時間'])
            for row in range(len(result)):
                for col in range(3):
                    r_dict = dict(result[row])
                    if col == 0:
                        item = QStandardItem(r_dict['item'])
                    if col == 1:
                        item = QStandardItem(str(r_dict['Total']))
                    if col == 2:
                        item = QStandardItem(r_dict['time'])
                    self.model.setItem(row, col, item)
            self.ui.tableView.setModel(self.model)
    #銷售額
    def sellall(self):
        result = list(collection2.find({}, {"_id":0, "item":0, "time":0}))
        total = 0
        for i in range(len(result)):
            r_dict = dict(result[i])
            total += int(r_dict['Total'])
        revenue_msg = QMessageBox()
        revenue_msg.setStyleSheet('QMessageBox{font-size:25px;}\nQPushButton{font-size:20px;}')
        revenue_msg.setWindowTitle('總銷售額')
        revenue_msg.setText('總銷售額:' + str(total) + '元')
        revenue_msg.setStandardButtons(QMessageBox.Ok)
        reValue = revenue_msg.exec()
        if reValue == QMessageBox.Ok:
            self.ui.Errorlabel.setText('總銷售額:' + str(total) + '元')
        revenue_msg.show()
class New_Item(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_SubWindow()
        self.ui2.setupUi(self)
        self.ui2.ok.clicked.connect(self.ok)
        self.ui2.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止修改表格內容
        self.ui2.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)#根據內容一格可以多行
        self.ui2.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#自動將表格水平標題平均分配
        self.ui2.tableView.verticalHeader().setVisible(False)#隱藏縱向座標

        result = list(collection.find({}, {"_id":0, "name":1, "price":1}))
        self.model = QStandardItemModel(len(result), 2)
        self.model.setHorizontalHeaderLabels(['品項', '價格'])
        for row in range(len(result)):
            for col in range(2):
                r_dict = dict(result[row])
                if col == 0:
                    item = QStandardItem(r_dict['name'])
                if col == 1:
                    item = QStandardItem(str(r_dict['price']))
                self.model.setItem(row, col, item)
        self.ui2.tableView.setModel(self.model)

    def ok(self):
        item_new = self.ui2.itemTextEdit.toPlainText()
        price_new = self.ui2.priceTextEdit.toPlainText()
        collection.insert_many([{"name":str(item_new), "price":int(price_new)}])
        result = list(collection.find({}, {"_id":0, "name":1, "price":1}))
        self.model = QStandardItemModel(len(result), 2)
        self.model.setHorizontalHeaderLabels(['品項', '價格'])
        for row in range(len(result)):
            for col in range(2):
                r_dict = dict(result[row])
                if col == 0:
                    item = QStandardItem(r_dict['name'])
                if col == 1:
                    item = QStandardItem(str(r_dict['price']))
                self.model.setItem(row, col, item)
        self.ui2.priceTextEdit.setPlainText('')
        self.ui2.itemTextEdit.setPlainText('')
        self.ui2.tableView.setModel(self.model)
class Update_Price(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui3 = Ui_Subwindow_2()
        self.ui3.setupUi(self)
        self.ui3.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止修改表格內容
        self.ui3.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)#根據內容一格可以多行
        self.ui3.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#自動將表格水平標題平均分配
        self.ui3.tableView.verticalHeader().setVisible(False)#隱藏縱向座標
        self.ui3.update.clicked.connect(self.update)

        result = list(collection.find({}, {"_id":0, "name":1, "price":1}))
        self.model = QStandardItemModel(len(result), 2)
        self.model.setHorizontalHeaderLabels(['品項', '價格'])
        for row in range(len(result)):
            for col in range(2):
                r_dict = dict(result[row])
                if col == 0:
                    item = QStandardItem(r_dict['name'])
                if col == 1:
                    item = QStandardItem(str(r_dict['price']))
                self.model.setItem(row, col, item)
        self.ui3.tableView.setModel(self.model)

    def update(self):
        target = self.ui3.tableView.currentIndex().data()
        new_price = self.ui3.priceTextEdit.toPlainText()
        update_target = list(collection.find({"name":str(target)}, {"_id":0}))
        new_price_dict = {}
        new_price_dict['name'] = str(target)
        new_price_dict['price'] = int(new_price)
        
        collection.update_one(update_target[0], {"$set":new_price_dict})

        result = list(collection.find({}, {"_id":0, "name":1, "price":1}))
        self.model = QStandardItemModel(len(result), 2)
        self.model.setHorizontalHeaderLabels(['品項', '價格'])
        for row in range(len(result)):
            for col in range(2):
                r_dict = dict(result[row])
                if col == 0:
                    item = QStandardItem(r_dict['name'])
                if col == 1:
                    item = QStandardItem(str(r_dict['price']))
                self.model.setItem(row, col, item)
        self.ui3.tableView.setModel(self.model)
        self.ui3.priceTextEdit.clear()

qApp = QApplication(sys.argv)

form = MainWindow()
form2 = New_Item()
form3 = Update_Price()

form.ui.newitem.clicked.connect(form2.show)
form.ui.updateprice.clicked.connect(form3.show)

form.show()
sys.exit(qApp.exec_())
