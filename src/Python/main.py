
import sys
import typing

from PyQt5.QtWidgets import QWidget, QMainWindow
from resources.QRC import images
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from Python.controller.ControllerMenu import controllerMenu
from Python.controller.ControllerInicioSesion import controllerInicioSesion
from Python.controller.ControllerRegistro import controllerRegistro

class app(QMainWindow):
    def __init__(self) :
        super(app, self).__init__()
        self.pilaWidgets = QtWidgets.QStackedWidget(self)

        self.inicioSesion = controllerInicioSesion()
        self.registro = controllerRegistro()
        self.menuC = controllerMenu()

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
        self.inicioSesion.Boton_Cracion_Usuario.clicked.connect(self.cambioRegistro)
        self.registro.boton_Iniciar_sesion.clicked.connect(self.cambioInicioSesion)
        self.inicioSesion.Ingresar.clicked.connect(self.cambioMenu)
        self.registro.Boton_Registro.clicked.connect(self.registrar)

    def cambioInicioSesion(self):
        self.pilaWidgets.setCurrentWidget(self.inicioSesion)

    def cambioRegistro(self):
        self.pilaWidgets.setCurrentWidget(self.registro)

    def cambioMenu(self):
        self.inicioSesion.abrirMenu()
        #self.close()
       
    def registrar(self):
        self.registro.registrar()
    

if __name__ == '__main__':
    aplicacion = QtWidgets.QApplication(sys.argv)
    window = app()
    window.show()
    sys.exit(aplicacion.exec_())