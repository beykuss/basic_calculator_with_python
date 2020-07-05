from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import time

import sys

sonuc = 0
sonuclist = list()
class HesapMak(QMainWindow):
    def __init__(self):
        super().__init__()
       # self.setWindowIcon(QIcon(r'C:\Users\pc2\Desktop'))
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(200,100,248,300)
        self.setFixedSize(self.size())
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(),Qt.black)
        self.setPalette(self.p)




        self.setUI()

    def setUI(self):
################################Giriş Alanı #############


        self.giris = QLabel(self)
        self.giris.resize(215,30)
        self.giris.move(18,30)
        self.giris.setAlignment(Qt.AlignRight)
        self.giris.setStyleSheet("font:14pt Arial Bold;border:3px solid #908f8f;border-radius:5px;background-color:#cfcfcf")
        self.giris.setText("O")

        self.history = QLabel(self)
        self.history.resize(162,30)
        self.history.move(18,250)
        self.history.setStyleSheet("font:12pt Arial ;border:3px solid #908f8f;border-radius:5px;background-color:#cfcfcf")
        self.history.setText("Hist:")
        self.history.setAlignment(Qt.AlignTop)

        self.clearHistory = QPushButton(self)
        self.clearHistory.resize(50, 30)
        self.clearHistory.move(183, 250)
        self.clearHistory.setStyleSheet("font:12pt Arial ;border:3px solid #ff0000;border-radius:5px;background-color:#ff7f00")
        self.clearHistory.setText("CH")
        self.clearHistory.clicked.connect(self.CH)


        #self.clickSound = QMediaPlayer()
#        self.clickSound.setMedia(QMediaContent(QUrl.fromLocalFile(r"C:\Users\pc2\Desktop\PHYTON-DERSLERİ\Hesap Makinesi\MClick.mp3")))

        menu_bar = self.menuBar()


        view=menu_bar.addMenu("View")
        order = menu_bar.addMenu("Order")
        help = menu_bar.addMenu("Help")
        hakkimiz = menu_bar.addMenu("About Us")


        standart = QAction("Standart",self)
        kallavi = QAction("Soft",self)
        view.addAction(standart)
        view.addAction(kallavi)

        copy = QAction("Copy",self)
        copy.setShortcut("CTRL+C")
        paste = QAction("Paste",self)
        paste.setShortcut("CTRL+V")

        about1 = QAction("About the Calculator",self)
        hakkimiz.addAction(about1)
        hakkimiz.triggered[QAction].connect(self.About_Us)


        yardim = QAction("Show Help",self)
        yardim.setShortcut("F1")
        help.addAction(yardim)



        ### exist the button
        butons = []
        for i in range(1,10):
            i = QPushButton(str(i),self)
            i.setFont(QFont("Arial",14))
            i.resize(50,30)
            i.setStyleSheet("border:3px solid #ff0000;border-radius:5px;background-color:#ff7f00")
            i.clicked.connect(self.enterNumbers)
            butons.append(i)

        butonInt = 0
        for i in range(0,3):
            for j  in range(0,3):
                butons[butonInt].move(18+55*j,105+i*35)
                butonInt += 1
################### + - * / marks exist ################
        butonops = []
        for i in range(5):
            i = QPushButton(self)
            i.resize(50,30)
            i.setFont(QFont("Arial",14))
            i.setStyleSheet("border:3px solid #ff0000;border-radius:5px;background-color:#ff7f00")
            i.clicked.connect(self.enterOperator)
            butonops.append(i)
        butonops[0].setText("-")
        butonops[1].setText("*")
        butonops[2].setText("/")
        butonops[3].setText("+")
        butonops[4].setText("=")

        butonops[0].clicked.connect(self.negativeNum)
        butonops[4].clicked.connect(self.equal)



        for i in range(5):
            butonops[i].move(183,70+i*35)
################### others operator ########
        otherbuttons = []
        for i in range(4):
            i = QPushButton(self)
            i.resize(80, 30)
            i.setFont(QFont("Arial", 14))
            i.setStyleSheet("border:3px solid #ff0000;border-radius:5px;background-color:#ff7f00")
            otherbuttons.append(i)
        for i in range(2):
            otherbuttons[i].move(18+i*82, 70)

        otherbuttons[2].move(18, 210)
        otherbuttons[3].move(100,210)

        otherbuttons[0].setText("C")
        otherbuttons[1].setText("←")
        otherbuttons[2].setText("0")
        otherbuttons[3].setText(".")

        otherbuttons[0].clicked.connect(self.clearEntry)
        otherbuttons[1].clicked.connect(self.deleteObje)
        otherbuttons[2].clicked.connect(self.enterNumbers)
        otherbuttons[3].clicked.connect(self.enterOperator)








        self.show()

    ############ Functions ##################

    def negativeNum(self):
        buton_text = self.sender().text()
        if self.giris.text() == "O":
            self.giris.setText(buton_text)




    def enterNumbers(self):
#        self.clickSound.setVolume(20)
#        self.clickSound.play()

        buton_text = self.sender().text()
        if self.giris.text() != "0":
            if self.giris.text() == "O":
                self.giris.setText("")
                self.giris.setText(buton_text)

            else:
                self.giris.setText(self.giris.text()+buton_text)

    def enterOperator(self):
        #self.clickSound.setVolume(20)
        #self.clickSound.play()

        buton_text =self.sender().text()

        if self.giris.text() != "O" :
            self.giris.setText(self.giris.text() + buton_text)

    def clearEntry(self):
        #self.clickSound.setVolume(20)
        #self.clickSound.play()

        self.giris.setText("O")

    def deleteObje(self):
        #self.clickSound.setVolume(20)
        #self.clickSound.play()

        a = self.giris.text()
        a= a[:-1]
        self.giris.setText(a)
        if len(a) == 0:
            self.giris.setText("O")

    def equal(self):
        try:
            #self.clickSound.setVolume(20)
           # self.clickSound.play()
            if self.giris.text() !="O":
                cont = self.giris.text()
                cont=cont[:-1]

                self.sonuc = eval(cont)
                if self.sonuc == int(self.sonuc):
                    sonuc = int(self.sonuc)
                    self.giris.setText(str(sonuc))
                else:
                    sonuc = float(self.sonuc)
                    self.giris.setText(str(sonuc))
                sonuclist.append(cont)
                sonuclist.reverse()
                self.history.setText("Hist: {}".format(sonuclist))
            else:
                pass
            if len(sonuclist) > 3 :
                sonuclist.clear()
        except:
            self.error()

            self.giris.setText("O")

    def CH(self): # Clear History
        #self.clickSound.setVolume(20)
        #self.clickSound.play()

        sonuclist.clear()
        self.history.setText("Hist:")

    def About_Us(self):
        info = QDialog()
        info.setWindowTitle("About the Calculator")
        info.setGeometry(300,100,500,400)
        info.setFixedSize(500,400)
        #info.setWindowIcon(QIcon(r"C:\Users\pc2\Desktop")) #optionaly add info icon

        about = QLabel(info)
        about.resize(450,100)
        about.move(35,100)
        about.setText("Küçük Mühendislik\nSürüm 14.3 (Yapım No 1433)\n© 2020 Küçük Corporation. Tüm Hakları saklidır.")

        img = QLabel(info)
        #img.setPixmap(QPixmap(r"C:\Users\pc2\Desktop")) ##optionaly
        img.move(35,30)

        closed = QPushButton(info)
        closed.resize(65,25)
        closed.move(380,340)
        closed.setText("Ok")
        closed.clicked.connect(info.close)
        info.exec()

    def error(self):
        eror = QDialog()
        eror.setWindowTitle("Warning Error")
        eror.setGeometry(300, 100, 270, 170)
        eror.setFixedSize(270, 170)
       # eror.setWindowIcon(QIcon(r"C:\Users\pc2\Desktop")) #optionaly

        erorinfo = QLabel(eror)
        erorinfo.resize(200,130)
        erorinfo.move(50,5)
        erorinfo.setText("You try wrong \nmatematical operation.\nPlease correct and try again.\n\n1) (-) mark cannot be to \nthe left of any mark!\n\n2) (-) mark cannot be to  \nside by side any mark!")

        closeror =QPushButton(eror)
        closeror.resize(65,25)
        closeror.setText("OK")
        closeror.move(200,140)

        closeror.clicked.connect(eror.close)
        eror.exec()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HesapMak()

    sys.exit(app.exec())
