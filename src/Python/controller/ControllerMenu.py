import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from resources.QRC import images
from Python.model.Usuario import Usuario

from ControllerChat import controllerChat


class controllerMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Grupos.ui', self)
        self.CambioChat = uic.loadUi('src/resources/interface/Ventana_Grupos.ui', self)


        self.Chat = controllerChat()
        self.Boton_Chat.clicked.connect()

        #self.Ingresar.clicked.connect(self.abrirMenu)
       
'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerMenu()
controlador.setWindowTitle("Menu")

controlador.show()
app.exec_()'''