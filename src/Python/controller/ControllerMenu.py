import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from resources.QRC import images
from Python.model.Usuario import Usuario


from controller.ControllerBusquedaGrupos import ControllerBusquedaGrupo
from controller.ControllerAdminGrupos import ControllerAdminGrupo
from controller.ControllerEventos import controllerEventos


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
        self.controllerAdminGrupos = ControllerAdminGrupo()
        self.controllerEventos = controllerEventos()

        self.pilaWidget = QtWidgets.QStackedWidget(self)

        self.pilaWidget.addWidget(self.controllerMenu)
        self.pilaWidget.addWidget(self.controllerGrupos)
        self.pilaWidget.addWidget(self.controllerAdminGrupos)
        self.pilaWidget.addWidget(self.controllerEventos)
        self.setCentralWidget(self.pilaWidget)

        self.pilaWidget.setCurrentWidget(self.controllerMenu)

        self.inicializar()
   
    def inicializar(self):
        self.resize(1280, 720)        
        self.conexiones()        

    def setUsuario(self, usuario):
        self.usuario = usuario
        self.controllerGrupos.setUsuario(self.usuario)
        self.controllerEventos.setUsuario(self.usuario)


    def conexiones(self):
        self.controllerMenu.botonGrupos.clicked.connect(self.cambioBusquedaGruposFromMenu)
        self.controllerGrupos.Boton_Menu.clicked.connect(self.cambioMenuFromBusquedaGrupos)
        self.controllerGrupos.Boton_AjustesGrupo.clicked.connect(self.ComprovarAdmin)
        self.controllerAdminGrupos.Boton_Atras.clicked.connect(self.cambioBusquedaGruposFromMenu)
        self.controllerMenu.botonCalendario.clicked.connect(self.cambioAEventos)

    def cambioBusquedaGruposFromMenu(self):
        self.controllerAdminGrupos.limpiar()
        self.setWindowTitle("Busqueda Grupos")
        self.pilaWidget.setCurrentWidget(self.controllerGrupos)

    def cambioAEventos(self):
        self.pilaWidget.setCurrentWidget(self.controllerEventos)

    def cambioMenuFromBusquedaGrupos(self):
        self.setWindowTitle("Menu")
        self.pilaWidget.setCurrentWidget(self.controllerMenu)

    def ComprovarAdmin(self):
        nombreG = self.controllerGrupos.List_MisGrupos.currentItem().text()
        if self.controllerAdminGrupos.abrirAjustes(self.usuario.correo,nombreG)==True:
            self.AbrirAdministracionGrupos()

    def AbrirAdministracionGrupos(self):
        self.setWindowTitle("Ajustes grupo")
        self.pilaWidget.setCurrentWidget(self.controllerAdminGrupos)
'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerMenu()
controlador.setWindowTitle("Menu")

controlador.show()
app.exec_()'''