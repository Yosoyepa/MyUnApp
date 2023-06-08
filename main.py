
import sys
import os
from PyQt5.QtWidgets import QWidget, QMainWindow
from resources.QRC import images
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from Python.controller.ControllerMenu import selectorMenu
from Python.controller.ControllerInicioSesion import controllerInicioSesion
from Python.controller.ControllerRegistro import controllerRegistro
from Python.controller.Controller_Chat import controller_Chat
class app(QMainWindow):
    def __init__(self) :
        super(app, self).__init__()
        self.pilaWidgets = QtWidgets.QStackedWidget(self)

        self.inicioSesion = controllerInicioSesion()
        self.registro = controllerRegistro(self, self.inicioSesion.crd)
        self.menu = selectorMenu()        
        

        self.pilaWidgets.addWidget(self.inicioSesion)
        self.pilaWidgets.addWidget(self.registro)
        
        

        self.setCentralWidget(self.pilaWidgets)


        self.pilaWidgets.setCurrentWidget(self.inicioSesion)

        self.inicializar()       

    def inicializar(self):
        self.resize(800, 536)
        self.setMaximumSize(800, 536)
        self.conexiones()
        self.setWindowTitle("Iniciar Sesion")

    def conexiones(self):
        self.inicioSesion.Boton_Cracion_Usuario.clicked.connect(self.cambioRegistroFromInicioSesion)
        self.inicioSesion.Ingresar.clicked.connect(self.botonIniciarSesion)



        self.registro.boton_Iniciar_sesion.clicked.connect(self.cambioInicioSesionFromRegistro)
        self.registro.Boton_Registro.clicked.connect(self.botonRegistrar) 

        

####CAMBIOS
    def cambioInicioSesionFromRegistro(self):
        self.setWindowTitle("Iniciar sesion")
        self.pilaWidgets.setCurrentWidget(self.inicioSesion)        

    def cambioRegistroFromInicioSesion(self):
        self.setWindowTitle("Registro")
        self.pilaWidgets.setCurrentWidget(self.registro)


########FUNCIONES

    def botonIniciarSesion(self):
        if(self.inicioSesion.abrirMenu()):
            self.pilaWidgets.setCurrentWidget(self.menu)            
            self.close()
      
    def botonRegistrar(self):
        self.registro.registrar()
        

    

    
    

if __name__ == '__main__':
    aplicacion = QtWidgets.QApplication(sys.argv)
    window = app()
    window.show()
    sys.exit(aplicacion.exec_())