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


class selectorMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)              
        
        ##controladores
        self.controllerGrupos = ControllerBusquedaGrupo()  
        self.controllerMenu = ControllerMenu()
        self.controllerAdminGrupos = ControllerAdminGrupo()
        self.controllerChat = controller_Chat()
        self.controllerEventos = controllerEventos()

        self.pilaWidget = QtWidgets.QStackedWidget(self)

        self.pilaWidget.addWidget(self.controllerMenu)
        self.pilaWidget.addWidget(self.controllerGrupos)
        self.pilaWidget.addWidget(self.controllerAdminGrupos)
        self.pilaWidget.addWidget(self.controllerChat)
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
        self.controllerChat.setUsuario(self.usuario)
        self.controllerEventos.setUsuario(self.usuario)


    def conexiones(self):

        ###CONEXIONES VISTA MENU
        self.controllerMenu.botonGrupos.clicked.connect(self.cambioBusquedaGrupos)
        self.controllerMenu.botonChat.clicked.connect(self.cambioChat)        

        ###CONEXIONES VISTA BUSQUEDA GRUPOS
        self.controllerGrupos.Boton_Menu.clicked.connect(self.cambioMenu)
        self.controllerGrupos.Boton_AjustesGrupo.clicked.connect(self.comprobarAdmin)
        self.controllerGrupos.Boton_Chat.clicked.connect(self.cambioChat)

        self.controllerAdminGrupos.Boton_Atras.clicked.connect(self.cambioBusquedaGrupos)

        ###CONEXIONES VISTA CHAT
        self.controllerChat.botonMenu.clicked.connect(self.cambioMenu)	
        self.controllerChat.botonGrupos.clicked.connect(self.cambioBusquedaGrupos)
        self.controllerMenu.botonCalendario.clicked.connect(self.cambioAEventos)

    def cambioBusquedaGrupos(self):
        self.controllerAdminGrupos.limpiar()
        self.setWindowTitle("Busqueda Grupos")
        self.pilaWidget.setCurrentWidget(self.controllerGrupos)

    def cambioAEventos(self):
        self.pilaWidget.setCurrentWidget(self.controllerEventos)

    def cambioMenu(self):
        self.setWindowTitle("Menu")
        self.pilaWidget.setCurrentWidget(self.controllerMenu)

    def cambioChat(self):
        self.setWindowTitle("Chat")        
        self.pilaWidget.setCurrentWidget(self.controllerChat)

    def comprobarAdmin(self):
        nombreG = self.controllerGrupos.List_MisGrupos.currentItem().text()
        if self.controllerAdminGrupos.abrirAjustes(self.usuario.correo,nombreG)==True:
            self.abrirAdministracionGrupos()

    def abrirAdministracionGrupos(self):
        self.setWindowTitle("Ajustes grupo")
        self.pilaWidget.setCurrentWidget(self.controllerAdminGrupos)

    
'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerMenu()
controlador.setWindowTitle("Menu")

controlador.show()
app.exec_()'''