# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from dotenv import load_dotenv

from PyQt5 import QtCore, QtGui, QtWidgets
from db_config import main, db_insert_main_data

load_dotenv()
test_img_file = os.getenv('test_img_file')


class Ui_WeaponRecognition(object):
    def setupUi(self, WeaponRecognition):
        WeaponRecognition.setObjectName("WeaponRecognition")
        WeaponRecognition.resize(510, 555)
        self.centralwidget = QtWidgets.QWidget(WeaponRecognition)
        self.centralwidget.setObjectName("centralwidget")
        self.tButton = QtWidgets.QRadioButton(self.centralwidget)
        self.tButton.setGeometry(QtCore.QRect(30, 70, 82, 17))
        self.tButton.setObjectName("tButton")
        self.tButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.tButton_2.setGeometry(QtCore.QRect(30, 50, 82, 17))
        self.tButton_2.setObjectName("tButton_2")
        self.tButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.tButton_3.setGeometry(QtCore.QRect(30, 30, 82, 17))
        self.tButton_3.setObjectName("tButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(210, 510, 75, 23))
        self.submit.setObjectName("submit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 271, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 161, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 271, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 320, 281, 181))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(test_img_file))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 300, 161, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.location = QtWidgets.QTextEdit(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(30, 220, 461, 71))
        self.location.setObjectName("location")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 170, 461, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.official = QtWidgets.QTextEdit(self.centralwidget)
        self.official.setGeometry(QtCore.QRect(30, 120, 461, 21))
        self.official.setObjectName("official")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 30, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        WeaponRecognition.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WeaponRecognition)
        self.statusbar.setObjectName("statusbar")
        WeaponRecognition.setStatusBar(self.statusbar)

        self.retranslateUi(WeaponRecognition)
        QtCore.QMetaObject.connectSlotsByName(WeaponRecognition)
        
        self.submit.clicked.connect(self.clicked)

    def retranslateUi(self, WeaponRecognition):
        _translate = QtCore.QCoreApplication.translate
        WeaponRecognition.setWindowTitle(_translate("WeaponRecognition", "MainWindow"))
        self.tButton.setText(_translate("WeaponRecognition", "Terrestre"))
        self.tButton_2.setText(_translate("WeaponRecognition", "Aereo"))
        self.tButton_3.setText(_translate("WeaponRecognition", "Maritimo"))
        self.label.setText(_translate("WeaponRecognition", "Tipo de transporte"))
        self.label_2.setText(_translate("WeaponRecognition", "Institucion a cargo"))
        self.submit.setText(_translate("WeaponRecognition", "Procesar"))
        self.label_3.setText(_translate("WeaponRecognition", "Nombre del Oficial a Cargo del Operativo"))
        self.label_4.setText(_translate("WeaponRecognition", "Localidad del Operativo"))
        self.label_5.setText(_translate("WeaponRecognition", "Cedula ID del Oficial a Cargo"))
        self.label_7.setText(_translate("WeaponRecognition", "Imagen del Operativo"))
        self.comboBox.setItemText(0, _translate("WeaponRecognition", "DGM"))
        self.comboBox.setItemText(1, _translate("WeaponRecognition", "DGA"))
        self.comboBox.setItemText(2, _translate("WeaponRecognition", "DNCD"))
        self.comboBox.setItemText(3, _translate("WeaponRecognition", "CESFRONT"))
        self.comboBox.setItemText(4, _translate("WeaponRecognition", "DICRIM"))    

    def clicked(self):        
        location = self.location.toPlainText()
        official = self.official.toPlainText()
        transportation = self.transportation()
        institution = self.institution()
        
        db, mycursor, weapon_id = main()
        
        db_insert_main_data(db, mycursor, weapon_id, official, location, transportation, institution)
        
        self.label_6.setPixmap(QtGui.QPixmap("object_detection_img.jpg"))
        
    def transportation(self):
        if self.tButton.isChecked():
            return 1
        elif self.tButton_2.isChecked():
            return 2
        elif self.tButton_3.isChecked():
            return 3
        
    def institution(self):
        return self.comboBox.currentIndex() + 1 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WeaponRecognition = QtWidgets.QMainWindow()
    ui = Ui_WeaponRecognition()
    ui.setupUi(WeaponRecognition)
    WeaponRecognition.show()
    sys.exit(app.exec_())