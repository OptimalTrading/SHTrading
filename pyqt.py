import _mactowin, _admin, _update
import sys, time, os
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    #GUI code  
        self.setWindowTitle("PyStock")
        self.setGeometry(500, 250, 300, 600)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)



        btn1 = QPushButton("Check account", self)
        btn1.move(20, 30)
        btn1.clicked.connect(self.btn1_clicked)
        self.status_text=QLineEdit(self)
        self.status_text.setText("로그인 시도중!!!")
        self.status_text.move(120, 30)
        self.status_text.setEnabled(False)

        label = QLabel('종목코드: ', self)
        label.move(20, 60)
        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 60)
        btn2 = QPushButton("search", self)
        btn2.move(20, 90)
        btn2.clicked.connect(self.btn2_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 120, 260, 120)

        btn3 = QPushButton("list", self)
        btn3.move(20, 240)
        btn3.clicked.connect(self.btn3_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(20, 270, 260, 120)



    #status
    def btn1_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            self.statusBar().showMessage("Not connected")
            QMessageBox.about(self, "message", "foooooooooo!")
        else:
            self.statusBar().showMessage("Connected")
            account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
            self.status_text.setText(account_num.rstrip(';'))
    #search
    def btn2_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)
        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        # CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")
    #list
    def btn3_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []
        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
            kospi_code_name_list.append(x + " : " + name)
        self.listWidget.addItems(kospi_code_name_list)

    def event_connect(self, err_code):
        if err_code == 0:
            self.status_text.setText("로그인 성공")
            self.code_edit.setText("039490")
        else: self.status_text.setText("로그인 실패")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            rate_ = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "등락율")
            max_ = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "상한가")
            min_ = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "하한가")
            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())
            self.text_edit.append("등락율: " + rate_.strip())
            self.text_edit.append("상한가: " + max_.strip())
            self.text_edit.append("하한가: " + min_.strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
