# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_Ingreso.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window_Inicio(object):
    def setupUi(self, Window_Inicio):
        Window_Inicio.setObjectName("Window_Inicio")
        Window_Inicio.resize(810, 523)
        Window_Inicio.setMinimumSize(QtCore.QSize(810, 523))
        Window_Inicio.setMaximumSize(QtCore.QSize(810, 523))
        self.centralwidget = QtWidgets.QWidget(Window_Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.Line_Usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_Usuario.setGeometry(QtCore.QRect(220, 250, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Line_Usuario.setFont(font)
        self.Line_Usuario.setReadOnly(False)
        self.Line_Usuario.setObjectName("Line_Usuario")
        self.Line_Contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_Contrasena.setGeometry(QtCore.QRect(220, 300, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Line_Contrasena.setFont(font)
        self.Line_Contrasena.setReadOnly(False)
        self.Line_Contrasena.setObjectName("Line_Contrasena")
        self.Ingresar = QtWidgets.QPushButton(self.centralwidget)
        self.Ingresar.setGeometry(QtCore.QRect(340, 370, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Ingresar.setFont(font)
        self.Ingresar.setObjectName("Ingresar")
        self.Boton_Cracion_Usuario = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Cracion_Usuario.setGeometry(QtCore.QRect(360, 330, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Boton_Cracion_Usuario.setFont(font)
        self.Boton_Cracion_Usuario.setObjectName("Boton_Cracion_Usuario")
        self.Label_Imagen = QtWidgets.QLabel(self.centralwidget)
        self.Label_Imagen.setGeometry(QtCore.QRect(-10, -10, 831, 501))
        self.Label_Imagen.setAutoFillBackground(False)
        self.Label_Imagen.setText("")
        self.Label_Imagen.setPixmap(QtGui.QPixmap("resources\Fondo.png"))
        self.Label_Imagen.setScaledContents(True)
        self.Label_Imagen.setObjectName("Label_Imagen")
        self.Label_Usuario = QtWidgets.QLabel(self.centralwidget)
        self.Label_Usuario.setGeometry(QtCore.QRect(220, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Usuario.setFont(font)
        self.Label_Usuario.setStyleSheet("color: rgb(255, 255, 255);")
        self.Label_Usuario.setObjectName("Label_Usuario")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.Label_Imagen.raise_()
        self.Line_Usuario.raise_()
        self.Line_Contrasena.raise_()
        self.Ingresar.raise_()
        self.Boton_Cracion_Usuario.raise_()
        self.Label_Usuario.raise_()
        self.label_2.raise_()
        Window_Inicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window_Inicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        Window_Inicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window_Inicio)
        self.statusbar.setObjectName("statusbar")
        Window_Inicio.setStatusBar(self.statusbar)

        self.retranslateUi(Window_Inicio)
        QtCore.QMetaObject.connectSlotsByName(Window_Inicio)

    def retranslateUi(self, Window_Inicio):
        _translate = QtCore.QCoreApplication.translate
        Window_Inicio.setWindowTitle(_translate("Window_Inicio", "MainWindow"))
        self.Ingresar.setText(_translate("Window_Inicio", "Ingresar"))
        self.Boton_Cracion_Usuario.setText(_translate("Window_Inicio", "Registrarse"))
        self.Label_Usuario.setText(_translate("Window_Inicio", "Usuario"))
        self.label_2.setText(_translate("Window_Inicio", "Contraseña"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_Inicio = QtWidgets.QMainWindow()
    ui = Ui_Window_Inicio()
    ui.setupUi(Window_Inicio)
    Window_Inicio.show()
    sys.exit(app.exec_())