# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: #c0e1ec;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 182, 1080))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: #01233C;")   
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 0, 100, 100))
        self.pushButton.setObjectName("pushButton")
        #Establecer la imagen del boton
        icon = QIcon()
        icon.addPixmap(QPixmap("C:/Users/juanc/Documents/My Un APP Grupos/Iconos/Exterior.png"), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        # Establecer propiedades del botón
        # Hacer que la imagen tenga animacion al ser presionada
        self.pushButton.setFlat(True) 
        self.pushButton.setStyleSheet("background-color: transparent;")  # Hace que el fondo del botón sea transparente
        
        # cambiar el tamaño de la imagen
        self.pushButton.setIconSize(QtCore.QSize(100, 100))  # Cambia el tamaño del icono del botón
        
        # Boton Para ir a la seccion de grupos
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 210, 100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("C:/Users/juanc/Documents/My Un APP Grupos/Iconos/User_Groups_Icon.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setStyleSheet("background-color: transparent;")
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        
        #Frame para la barra lateral de arriba
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: #01233C;")
        self.frame.setGeometry(QtCore.QRect(169, -6, 1751, 104))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        #Frame para la parte de creacion de grupos

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(231, 188, 754, 770))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("background-color: #004B73; border-radius: 30px;")
        
        #Boton para crear grupos

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 40, 100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("C:/Users/juanc/Documents/My Un APP Grupos/Iconos/Añadir_Grupo_De_Usuarios_Hombre_Hombre.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))

        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setGeometry(QtCore.QRect(60, 168, 619, 530))
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color: #C0E1EC; border-radius: 0px;")   
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 201, 21))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 201, 21))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 70, 201, 21))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 201, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(170, 30, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(20, 40, 141, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 80, 131, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 120, 141, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        ##Frame para la seleccion de grupos y lista de miembros
        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1094, 188, 754, 770))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setStyleSheet("background-color: #004B73; border-radius: 30px;")

        ##Icono para ver los grupos

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 40, 100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("C:/Users/juanc/Documents/My Un APP Grupos/Iconos/Conferencia.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))

        ##Widget para la lista de grupos
        self.widget_3 = QtWidgets.QWidget(self.frame_3)
        self.widget_3.setGeometry(QtCore.QRect(60, 140, 619, 274))
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setStyleSheet("background-color: #C0E1EC; border-radius: 0px;")

        ##Boton con el icono para seleccionar un grupo
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 10, 376, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        icon5 = QIcon()
        icon5.addPixmap(QPixmap("C:/Users/juanc/Documents/My Un APP Grupos/Iconos/R2-D2.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(100, 100))
        
        # Aumenta el tamaño del texto del botón
        font = QtGui.QFont()
        font.setPointSize(20) # Ajusta el tamaño del texto
        self.pushButton_5.setFont(font)
        
        # Ajusta la política de tamaño para que el botón sea redimensionable
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        ##Widget para la lista de miembros de un grupo seleccionado
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setGeometry(QtCore.QRect(60, 450, 619, 274))
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setStyleSheet("background-color: #C0E1EC; border-radius: 0px;")

       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", " "))
        self.pushButton_2.setText(_translate("MainWindow", " "))
        self.pushButton_3.setText(_translate("MainWindow", " "))
        self.pushButton_4.setText(_translate("MainWindow", " "))
        self.pushButton_5.setText(_translate("MainWindow", "GRUPO EPICO 1"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "NOMBRE DEL GRUPO"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "AÑADIR MIEMBROS"))
        self.checkBox.setText(_translate("MainWindow", "USUARIO DISPONIBLE"))
        self.checkBox_2.setText(_translate("MainWindow", "USUARIO DISPONIBLE"))
        self.checkBox_3.setText(_translate("MainWindow", "USUARIO DISPONIBLE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
