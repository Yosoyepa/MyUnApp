# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_Correo_Rec_Contra.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_Correo_Rec_Contra(object):
    def setupUi(self, Ventana_Correo_Rec_Contra):
        Ventana_Correo_Rec_Contra.setObjectName("Ventana_Correo_Rec_Contra")
        Ventana_Correo_Rec_Contra.resize(810, 523)
        Ventana_Correo_Rec_Contra.setMinimumSize(QtCore.QSize(810, 523))
        Ventana_Correo_Rec_Contra.setMaximumSize(QtCore.QSize(810, 523))
        self.centralwidget = QtWidgets.QWidget(Ventana_Correo_Rec_Contra)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Correo_Rec_Contra = QtWidgets.QLabel(self.centralwidget)
        self.Label_Correo_Rec_Contra.setGeometry(QtCore.QRect(150, 90, 521, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Correo_Rec_Contra.setFont(font)
        self.Label_Correo_Rec_Contra.setScaledContents(False)
        self.Label_Correo_Rec_Contra.setObjectName("Label_Correo_Rec_Contra")
        self.Line_Correo_Rec = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_Correo_Rec.setGeometry(QtCore.QRect(220, 190, 361, 31))
        self.Line_Correo_Rec.setObjectName("Line_Correo_Rec")
        self.Label_Fondo_Correo_Rec_Contra = QtWidgets.QLabel(self.centralwidget)
        self.Label_Fondo_Correo_Rec_Contra.setGeometry(QtCore.QRect(-20, -20, 851, 531))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Label_Fondo_Correo_Rec_Contra.setFont(font)
        self.Label_Fondo_Correo_Rec_Contra.setText("")
        self.Label_Fondo_Correo_Rec_Contra.setObjectName("Label_Fondo_Correo_Rec_Contra")
        self.Boton_Regresar_Correo_Rec_Contra1 = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Regresar_Correo_Rec_Contra1.setGeometry(QtCore.QRect(210, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Boton_Regresar_Correo_Rec_Contra1.setFont(font)
        self.Boton_Regresar_Correo_Rec_Contra1.setObjectName("Boton_Regresar_Correo_Rec_Contra1")
        self.Boton_Continuar_Correo_Rec_Contra = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Continuar_Correo_Rec_Contra.setGeometry(QtCore.QRect(450, 310, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Boton_Continuar_Correo_Rec_Contra.setFont(font)
        self.Boton_Continuar_Correo_Rec_Contra.setObjectName("Boton_Continuar_Correo_Rec_Contra")
        self.Label_Fondo_Correo_Rec_Contra.raise_()
        self.Label_Correo_Rec_Contra.raise_()
        self.Line_Correo_Rec.raise_()
        self.Boton_Regresar_Correo_Rec_Contra1.raise_()
        self.Boton_Continuar_Correo_Rec_Contra.raise_()
        Ventana_Correo_Rec_Contra.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_Correo_Rec_Contra)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        Ventana_Correo_Rec_Contra.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_Correo_Rec_Contra)
        self.statusbar.setObjectName("statusbar")
        Ventana_Correo_Rec_Contra.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Correo_Rec_Contra)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Correo_Rec_Contra)

    def retranslateUi(self, Ventana_Correo_Rec_Contra):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Correo_Rec_Contra.setWindowTitle(_translate("Ventana_Correo_Rec_Contra", "MainWindow"))
        self.Label_Correo_Rec_Contra.setText(_translate("Ventana_Correo_Rec_Contra", "Ingrese el correo al cual esta asociado la cuenta"))
        self.Boton_Regresar_Correo_Rec_Contra1.setText(_translate("Ventana_Correo_Rec_Contra", "Regresar"))
        self.Boton_Continuar_Correo_Rec_Contra.setText(_translate("Ventana_Correo_Rec_Contra", "Continuar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Correo_Rec_Contra = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Correo_Rec_Contra()
    ui.setupUi(Ventana_Correo_Rec_Contra)
    Ventana_Correo_Rec_Contra.show()
    sys.exit(app.exec_())
