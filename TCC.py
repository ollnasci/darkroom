#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PIL import Image, ImageFilter, ImageEnhance
import shutil


class Ui_MainWindow(object):
    global image
    global ver
    global hor
    global btE
    global btD
    btD = 0
    btE = 0
    hor = 0
    ver = 0


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 429)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 571, 371))
        self.frame.setObjectName("frame")

        self.slExp = QtWidgets.QSlider(self.centralwidget)
        self.slExp.setGeometry(QtCore.QRect(600, 30, 181, 16))
        self.slExp.setOrientation(QtCore.Qt.Horizontal)
        self.slExp.setObjectName("slExp")

        self.slCon = QtWidgets.QSlider(self.centralwidget)
        self.slCon.setGeometry(QtCore.QRect(600, 300, 181, 16))
        self.slCon.setOrientation(QtCore.Qt.Horizontal)
        self.slCon.setObjectName("slCon")

        self.slSat = QtWidgets.QSlider(self.centralwidget)
        self.slSat.setGeometry(QtCore.QRect(600, 80, 181, 16))
        self.slSat.setOrientation(QtCore.Qt.Horizontal)
        self.slSat.setObjectName("slSat")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 10, 67, 17))
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 280, 67, 17))
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.btnAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrir.setGeometry(QtCore.QRect(600, 350, 89, 25))
        self.btnAbrir.setObjectName("btnAbrir")
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setGeometry(QtCore.QRect(700, 350, 89, 25))
        self.btnSalvar.setObjectName("btnSalvar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(600, 110, 128, 83))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbPB = QtWidgets.QCheckBox(self.widget)
        self.cbPB.setObjectName("cbPB")
        self.verticalLayout.addWidget(self.cbPB)
        self.cbB = QtWidgets.QCheckBox(self.widget)
        self.cbB.setObjectName("cbB")
        self.verticalLayout.addWidget(self.cbB)
        self.cbS = QtWidgets.QCheckBox(self.widget)
        self.cbS.setObjectName("cbS")
        self.verticalLayout.addWidget(self.cbS)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(600, 220, 181, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btnEsq = QtWidgets.QPushButton(self.splitter)
        self.btnEsq.setObjectName("btnEsq")
        self.btnVer = QtWidgets.QPushButton(self.splitter)
        self.btnVer.setObjectName("btnVer")
        self.btnHor = QtWidgets.QPushButton(self.splitter)
        self.btnHor.setObjectName("btnHor")
        self.btnDir = QtWidgets.QPushButton(self.splitter)
        self.btnDir.setObjectName("btnDir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ############################################
        self.btnAbrir.clicked.connect(self.abrir)
        self.btnSalvar.clicked.connect(self.salv)
        self.btnDir.clicked.connect(self.girarDireita)
        self.btnEsq.clicked.connect(self.girarEsquerda)
        self.cbPB.stateChanged.connect(self.preview)
        self.cbB.stateChanged.connect(self.preview)
        self.cbS.stateChanged.connect(self.preview)
        self.slCon.setMinimum(0)
        self.slCon.setMaximum(100)
        self.slCon.setValue(50)
        self.slCon.setTickInterval(25)
        self.slCon.setTickPosition(self.slCon.TicksBelow)
        self.slCon.valueChanged.connect(self.preview)

        self.slExp.setMinimum(0)
        self.slExp.setMaximum(100)
        self.slExp.setValue(50)
        self.slExp.setTickInterval(25)
        self.slExp.setTickPosition(self.slExp.TicksBelow)
        self.slExp.valueChanged.connect(self.preview)
        self.slSat.setMinimum(0)
        self.slSat.setMaximum(100)
        self.slSat.setValue(50)
        self.slSat.setTickInterval(25)
        self.slSat.setTickPosition(self.slSat.TicksBelow)
        self.slSat.valueChanged.connect(self.preview)
        self.btnHor.clicked.connect(self.Hor)
        self.btnVer.clicked.connect(self.Ver)
        self.btnHor.setEnabled(False)
        self.btnVer.setEnabled(False)
        self.slSat.setEnabled(False)
        self.slExp.setEnabled(False)
        self.cbPB.setEnabled(False)
        self.cbB.setEnabled(False)
        self.cbS.setEnabled(False)
        self.btnSalvar.setEnabled(False)
        self.btnDir.setEnabled(False)
        self.btnEsq.setEnabled(False)
        self.slCon.setEnabled(False)
        ############################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DarkRoom"))
        self.label.setText(_translate("MainWindow", "Exposição"))
        self.label_3.setText(_translate("MainWindow", "Contraste"))
        self.label_2.setText(_translate("MainWindow", "Saturação"))
        self.btnAbrir.setText(_translate("MainWindow", "Abrir"))
        self.btnSalvar.setText(_translate("MainWindow", "Salvar"))
        self.cbPB.setText(_translate("MainWindow", "Preto e Branco"))
        self.cbB.setText(_translate("MainWindow", "Blur"))
        self.cbS.setText(_translate("MainWindow", "Sharpen"))
        self.btnEsq.setText(_translate("MainWindow", "<"))
        self.btnVer.setText(_translate("MainWindow", "/\\"))
        self.btnHor.setText(_translate("MainWindow", "="))
        self.btnDir.setText(_translate("MainWindow", ">"))

########################################################################################
    def abrir(self):
        global arquivo
        global preview
        arquivo, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        image = Image.open(arquivo)
        if os.path.exists('.preview'):
           shutil.rmtree('.preview')
           os.mkdir('.preview')
        else:
            os.mkdir('.preview')
        preview = '.preview/preview.png'
        image.save(preview)
        if arquivo:
            self.salvar()
            self.btnSalvar.setEnabled(True)
            self.btnDir.setEnabled(True)
            self.btnEsq.setEnabled(True)
            self.btnHor.setEnabled(True)
            self.btnVer.setEnabled(True)
            self.slSat.setEnabled(True)
            self.slExp.setEnabled(True)
            self.cbPB.setEnabled(True)
            self.cbB.setEnabled(True)
            self.cbS.setEnabled(True)
            self.slCon.setEnabled(True)

    def salv(self):
        global salvarA
        salvarA, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        if salvarA:
            image = Image.open(preview)
            salvarA = salvarA + ".png"
            image.save(salvarA)
        shutil.rmtree('.preview')
        image.show()
        sys.exit(0)

    def preview(self):
        image = Image.open(arquivo)
        if self.cbB.isChecked():
            image = image.filter(ImageFilter.BLUR())
        if self.cbPB.isChecked():
            image = image.convert(mode = 'L')
        if self.cbS.isChecked():
            image = image.filter(ImageFilter.SHARPEN())
        for x in range(btE):
            image = image.transpose(Image.ROTATE_90)
        for x in range(btD):
            image = image.transpose(Image.ROTATE_270)
        if ver == 1:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        if hor == 1:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
        expo = self.slExp.value() / 50
        sat = self.slSat.value() / 50
        cont = self.slCon.value() / 50
        image = image.point(lambda x: x * float(expo))
        satt = ImageEnhance.Color(image)
        image = satt.enhance(sat)
        contt = ImageEnhance.Contrast(image)
        image = contt.enhance(cont)
        image.save(preview)
        self.salvar()

    def girarDireita(self):
     global btD
     if btD == 4:
         btD = 0
     btD = btD + 1
     self.preview()

    def girarEsquerda(self):
     global btE
     if btE == 4:
         btE = 0
     btE = btE + 1
     self.preview()

    def Ver(self):
     global ver
     if ver == 0:
            ver = 1
     else:
            ver = 0
     self.preview()

    def Hor(self):
     global hor
     if hor == 0:
         hor = 1
     else:
         hor = 0
     self.preview()

    def salvar(self):
     image = QtGui.QPixmap(preview)
     image = image.scaled(self.frame.width(), self.frame.height(), QtCore.Qt.KeepAspectRatio)
     self.frame.setPixmap(image)
     self.frame.setAlignment(QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
