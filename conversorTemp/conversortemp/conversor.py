# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_conversor(object):
    def setupUi(self, conversor):
        conversor.setObjectName("conversor")
        conversor.resize(597, 184)
        self.centralwidget = QtWidgets.QWidget(conversor)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_converter.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.botao_converter.setObjectName("botao_converter")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(340, 120, 75, 23))
        self.botao_sair.setObjectName("botao_sair")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 431, 31))
        self.label.setObjectName("label")
        self.entrada_temp = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_temp.setGeometry(QtCore.QRect(260, 70, 161, 21))
        self.entrada_temp.setObjectName("entrada_temp")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 141, 31))
        self.label_2.setObjectName("label_2")
        conversor.setCentralWidget(self.centralwidget)

        self.retranslateUi(conversor)
        self.botao_sair.clicked.connect(conversor.close)
        QtCore.QMetaObject.connectSlotsByName(conversor)
        self.botao_converter.clicked.connect(self.converte)

    def converte(self):
        temp = float(self.entrada_temp.text())
        temp = (temp-32) * 5/9

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Sucesso")
        msg.setText("Resultado: "+str(temp)+"°C")
        msg.exec()

    def retranslateUi(self, conversor):
        _translate = QtCore.QCoreApplication.translate
        conversor.setWindowTitle(_translate(
            "conversor", "Conversor F/C - versao 1.0 "))
        self.botao_converter.setText(_translate("conversor", "Converter"))
        self.botao_sair.setText(_translate("conversor", "Sair"))
        self.label.setText(_translate(
            "conversor", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">Conversor de Temperatura Fahrenheit(°F) para Celsius (°C)</span></p></body></html>"))
        self.entrada_temp.setToolTip(_translate(
            "conversor", "Digitar a temperatura em Fahrenheit"))
        self.label_2.setText(_translate(
            "conversor", "<html><head/><body><p><span style=\" font-size:16pt;\">Temperatura:</span></p></body></html>"))
