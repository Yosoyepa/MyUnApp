import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from resources.QRC import images
from Python.model.Usuario import Usuario


from controller.ControllerBusquedaGrupos import ControllerBusquedaGrupo


class ControllerMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Menu.ui', self)                


class selectorMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)              
        
        ##controladores
        self.controllerGrupos = ControllerBusquedaGrupo()  
        self.controllerMenu = ControllerMenu()

        self.pilaWidget = QtWidgets.QStackedWidget(self)

        self.pilaWidget.addWidget(self.controllerMenu)
        self.pilaWidget.addWidget(self.controllerGrupos)
        
        self.setCentralWidget(self.pilaWidget)

        self.pilaWidget.setCurrentWidget(self.controllerMenu)

        self.inicializar()
        
    def inicializar(self):
        self.resize(1280, 720)        
        self.conexiones()        

    def setUsuario(self, usuario):
        self.usuario = usuario
        self.controllerGrupos.setUsuario(self.usuario)

    def conexiones(self):
        self.controllerMenu.botonGrupos.clicked.connect(self.cambioBusquedaGruposFromMenu)
        self.controllerGrupos.Boton_Menu.clicked.connect(self.cambioMenuFromBusquedaGrupos)

    def cambioBusquedaGruposFromMenu(self):
        self.setWindowTitle("Busqueda Grupos")
        self.pilaWidget.setCurrentWidget(self.controllerGrupos)

    def cambioMenuFromBusquedaGrupos(self):
        self.setWindowTitle("Menu")
        self.pilaWidget.setCurrentWidget(self.controllerMenu)
'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerMenu()
controlador.setWindowTitle("Menu")

controlador.show()
app.exec_()'''