import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from controller.Controller_Chat import controller_Chat
from resources.QRC import images
from Python.model.Usuario import Usuario


from controller.ControllerBusquedaGrupos import ControllerBusquedaGrupo
from controller.ControllerAdminGrupos import ControllerAdminGrupo
from controller.ControllerEventos import controllerEventos


class ControllerMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Menu.ui', self)         

        self.controllerGrupos = ControllerBusquedaGrupo()          
        self.controllerAdminGrupos = ControllerAdminGrupo()
        self.controllerChat = controller_Chat()
        self.controllerEventos = controllerEventos()   

        
        
        self.stackedWidget_4.addWidget(self.controllerGrupos)
        self.stackedWidget_4.addWidget(self.controllerAdminGrupos)
        self.stackedWidget_4.addWidget(self.controllerChat)
        self.stackedWidget_4.addWidget(self.controllerEventos)
        
        self.conexiones()


    def setUsuario(self, usuario):
        self.usuario = usuario
        self.controllerGrupos.setUsuario(self.usuario)
        self.controllerChat.setUsuario(self.usuario)
        self.controllerEventos.setUsuario(self.usuario)


    def conexiones(self):
        self.botonChat.clicked.connect(self.cambioChat)
        self.botonGrupos.clicked.connect(self.cambioBusquedaGrupos)
        self.botonCalendario.clicked.connect(self.cambioAEventos)
        self.controllerGrupos.Boton_AjustesGrupo.clicked.connect(self.comprobarAdmin)
        
        


    def cambioBusquedaGrupos(self):
        self.controllerAdminGrupos.limpiar()
        self.setWindowTitle("Busqueda Grupos")
        self.stackedWidget_4.setCurrentWidget(self.controllerGrupos)

    def cambioAEventos(self):
        self.stackedWidget_4.setCurrentWidget(self.controllerEventos)

    def cambioMenu(self):
        self.setWindowTitle("Menu")
        self.stackedWidget_4.setCurrentWidget(self.controllerMenu)

    def cambioChat(self):
        self.setWindowTitle("Chat")        
        self.stackedWidget_4.setCurrentWidget(self.controllerChat)

    def comprobarAdmin(self):
        nombreG = self.controllerGrupos.List_MisGrupos.currentItem().text()
        if self.controllerAdminGrupos.abrirAjustes(self.usuario.correo,nombreG)==True:
            self.abrirAdministracionGrupos()

    def abrirAdministracionGrupos(self):
        self.setWindowTitle("Ajustes grupo")
        self.stackedWidget_4.setCurrentWidget(self.controllerAdminGrupos)


    
'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerMenu()
controlador.setWindowTitle("Menu")

controlador.show()
app.exec_()'''