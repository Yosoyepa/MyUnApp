
import sys
import typing

from PyQt5.QtWidgets import QWidget, QMainWindow
from resources.QRC import images
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from Python.controller.ControllerMenu import controllerMenu
from Python.controller.ControllerInicioSesion import controllerInicioSesion
from Python.controller.ControllerRegistro import controllerRegistro
from Python.controller.ControllerCambioContrasena import controllerCambio
from Python.controller.ControllerChat import controllerChat


class app(QMainWindow):
    def __init__(self) :
        super(app, self).__init__()
        self.pilaWidgets = QtWidgets.QStackedWidget(self)

        self.inicioSesion = controllerInicioSesion()
        self.registro = controllerRegistro()
        self.menuC = controllerMenu()
        self.cambioContrasena = controllerCambio()

        self.pilaWidgets.addWidget(self.inicioSesion)
        self.pilaWidgets.addWidget(self.registro)
        self.pilaWidgets.addWidget(self.cambioContrasena)
        self.pilaWidgets.addWidget(self.menuC)


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
        self.inicioSesion.Boton_Cambio_Contra.clicked.connect(self.CambioRecuperacionContrasenaFromInicioSesion)


        self.registro.boton_Iniciar_sesion.clicked.connect(self.cambioInicioSesionFromRegistro)
        self.registro.Boton_Registro.clicked.connect(self.botonRegistrar)

        self.cambioContrasena.atrasButton.clicked.connect(self.CambioInicioSesionFromRecuperacionContrasena)
        

####CAMBIOS
    def cambioInicioSesionFromRegistro(self):
        self.setWindowTitle("Iniciar sesion")
        self.pilaWidgets.setCurrentWidget(self.inicioSesion)        

    def cambioRegistroFromInicioSesion(self):
        self.setWindowTitle("Registro")
        self.pilaWidgets.setCurrentWidget(self.registro)

    def CambioRecuperacionContrasenaFromInicioSesion(self):
        self.setWindowTitle("Recuperación contraseña")
        self.pilaWidgets.setCurrentWidget(self.cambioContrasena)

    def CambioInicioSesionFromRecuperacionContrasena(self):
        self.setWindowTitle("Iniciar sesion")
        self.pilaWidgets.setCurrentWidget(self.inicioSesion)

#Cambios a Chat

########FUNCIONES

    def botonIniciarSesion(self):
        if(self.inicioSesion.abrirMenu()):

            self.close()

       
    def botonRegistrar(self):
        self.registro.registrar()


    
    

if __name__ == '__main__':
    aplicacion = QtWidgets.QApplication(sys.argv)
    window = app()
    window.show()
    sys.exit(aplicacion.exec_())