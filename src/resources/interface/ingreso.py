# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_IngresoUhDGlD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources.QRC.images

class Ui_Window_Inicio(object):
    def setupUi(self, Window_Inicio):
        if not Window_Inicio.objectName():
            Window_Inicio.setObjectName(u"Window_Inicio")
        Window_Inicio.resize(800, 536)
        Window_Inicio.setMinimumSize(QSize(800, 536))
        Window_Inicio.setMaximumSize(QSize(800, 536))
        self.centralwidget = QWidget(Window_Inicio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#01233C")
        self.Line_Usuario = QLineEdit(self.centralwidget)
        self.Line_Usuario.setObjectName(u"Line_Usuario")
        self.Line_Usuario.setGeometry(QRect(215, 300, 370, 20))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Line_Usuario.setFont(font)
        self.Line_Usuario.setStyleSheet(u"background-color:#FFFFFF; color:#01233C; border-radius:10px")
        self.Line_Usuario.setCursorPosition(0)
        self.Line_Usuario.setReadOnly(False)
        self.Line_Contrasena = QLineEdit(self.centralwidget)
        self.Line_Contrasena.setObjectName(u"Line_Contrasena")
        self.Line_Contrasena.setGeometry(QRect(215, 364, 371, 21))
        font1 = QFont()
        font1.setPointSize(9)
        self.Line_Contrasena.setFont(font1)
        self.Line_Contrasena.setStyleSheet(u"background-color:#FFFFFF; color:#01233C; border-radius:10px")
        self.Line_Contrasena.setMaxLength(12)
        self.Line_Contrasena.setReadOnly(False)
        self.Line_Contrasena.setPlaceholderText(u" Contrase\u00f1a")
        self.Ingresar = QPushButton(self.centralwidget)
        self.Ingresar.setObjectName(u"Ingresar")
        self.Ingresar.setGeometry(QRect(324, 404, 146, 45))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        self.Ingresar.setFont(font2)
        self.Ingresar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ingresar.setStyleSheet(u"QPushButton{\n"
"	background-color:#FFFFFF; \n"
"	color:#01233C; \n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#01233C; \n"
"	color:#FFFFFF; \n"
"	border-radius:20px;\n"
"}")
        self.Ingresar.setIconSize(QSize(20, 16))
        self.Boton_Cracion_Usuario = QPushButton(self.centralwidget)
        self.Boton_Cracion_Usuario.setObjectName(u"Boton_Cracion_Usuario")
        self.Boton_Cracion_Usuario.setEnabled(True)
        self.Boton_Cracion_Usuario.setGeometry(QRect(355, 456, 90, 21))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.Boton_Cracion_Usuario.setFont(font3)
        self.Boton_Cracion_Usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.Boton_Cracion_Usuario.setAcceptDrops(False)
        self.Boton_Cracion_Usuario.setLayoutDirection(Qt.LeftToRight)
        self.Boton_Cracion_Usuario.setStyleSheet(u"QPushButton{\n"
"	color: #FFFFFF; \n"
"	background-color: transparent; \n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #00EEFF; \n"
"	background-color: transparent; \n"
"	border-radius:10px;\n"
"}\n"
"")
        self.Label_Imagen = QLabel(self.centralwidget)
        self.Label_Imagen.setObjectName(u"Label_Imagen")
        self.Label_Imagen.setEnabled(True)
        self.Label_Imagen.setGeometry(QRect(-20, 0, 976, 541))
        self.Label_Imagen.setAutoFillBackground(False)
        self.Label_Imagen.setStyleSheet(u"background-color:rgb(85, 255, 0)")
        self.Label_Imagen.setPixmap(QPixmap(u":/newPrefix/Images/viejito-01.png"))
        self.Label_Imagen.setScaledContents(True)
        self.Label_Imagen.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.Label_Usuario = QLabel(self.centralwidget)
        self.Label_Usuario.setObjectName(u"Label_Usuario")
        self.Label_Usuario.setGeometry(QRect(220, 268, 181, 31))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.Label_Usuario.setFont(font4)
        self.Label_Usuario.setStyleSheet(u"color: #FFFFFF; background-color: transparent;")
        self.Label_Contrasena = QLabel(self.centralwidget)
        self.Label_Contrasena.setObjectName(u"Label_Contrasena")
        self.Label_Contrasena.setGeometry(QRect(220, 332, 111, 31))
        self.Label_Contrasena.setFont(font4)
        self.Label_Contrasena.setStyleSheet(u"color: #FFFFFF; background-color: transparent;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(-20, -20, 831, 535))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(34)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-image: url(:/newPrefix/Fondo.png);")
        self.label.setPixmap(QPixmap(u":/newPrefix/Fondo.png"))
        self.label.setScaledContents(True)
        self.Boton_Cambio_Contra = QPushButton(self.centralwidget)
        self.Boton_Cambio_Contra.setObjectName(u"Boton_Cambio_Contra")
        self.Boton_Cambio_Contra.setGeometry(QRect(310, 481, 180, 23))
        font5 = QFont()
        font5.setFamily(u"Microsoft YaHei UI")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.Boton_Cambio_Contra.setFont(font5)
        self.Boton_Cambio_Contra.setCursor(QCursor(Qt.PointingHandCursor))
        self.Boton_Cambio_Contra.setStyleSheet(u"color: #FFFFFF; background-color: transparent; border-radius:10px")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(337, 80, 126, 160))
        self.logo.setStyleSheet(u"background-color: transparent;")
        self.logo.setFrameShape(QFrame.Box)
        self.logo.setLineWidth(0)
        self.logo.setPixmap(QPixmap(u":/inicioSesion/Icons/logo.png"))
        self.logo.setScaledContents(True)
        Window_Inicio.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.Label_Imagen.raise_()
        self.Line_Usuario.raise_()
        self.Line_Contrasena.raise_()
        self.Ingresar.raise_()
        self.Boton_Cracion_Usuario.raise_()
        self.Label_Usuario.raise_()
        self.Label_Contrasena.raise_()
        self.Boton_Cambio_Contra.raise_()
        self.logo.raise_()

        self.retranslateUi(Window_Inicio)

        QMetaObject.connectSlotsByName(Window_Inicio)
    # setupUi

    def retranslateUi(self, Window_Inicio):
        Window_Inicio.setWindowTitle(QCoreApplication.translate("Window_Inicio", u"MainWindow", None))
        self.Line_Usuario.setText("")
        self.Line_Usuario.setPlaceholderText(QCoreApplication.translate("Window_Inicio", u" Correo", None))
        self.Line_Contrasena.setInputMask("")
        self.Ingresar.setText(QCoreApplication.translate("Window_Inicio", u"Ingresar", None))
        self.Boton_Cracion_Usuario.setText(QCoreApplication.translate("Window_Inicio", u"Registrarse", None))
        self.Label_Imagen.setText("")
        self.Label_Usuario.setText(QCoreApplication.translate("Window_Inicio", u"Correo ", None))
        self.Label_Contrasena.setText(QCoreApplication.translate("Window_Inicio", u"Contrase\u00f1a", None))
        self.label.setText("")
        self.Boton_Cambio_Contra.setText(QCoreApplication.translate("Window_Inicio", u"\u00bfOlvidaste tu contrase\u00f1a?", None))
    # retranslateUi



    def set_image_opacity(self, value):
        graphics_effect = QGraphicsOpacityEffect(self.Label_Imagen)
        graphics_effect.setOpacity(value)
        self.Label_Imagen.setGraphicsEffect(graphics_effect)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Window_Inicio = QMainWindow()
    ui = Ui_Window_Inicio()    
    ui.setupUi(Window_Inicio)
    ui.set_image_opacity(0.44)
    Window_Inicio.show()
    sys.exit(app.exec_())
