import traceback

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic



from resources.QRC import images2

from Python.model import CRUD
from Python.model.Usuario import Usuario

class controllerCambioContrasena(QMainWindow):
    def __init__(self, parent = None):        

        QMainWindow.__init__(self)
        self.parent = parent  # type: ignore
        uic.loadUi('src/resources/interface/Ventana_Cambio_Contrasena.ui', self)
        self.set_image_opacity(0.44)
        
        self.cambiarButton.clicked.connect(self.cambiaContrasena)
        
    
    def set_image_opacity(self, value):
        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.label_fondo)
        graphics_effect.setOpacity(value)
        self.label_fondo.setGraphicsEffect(graphics_effect)

    def setCorreo(self, correo: str):
        self.correo = correo

    def cambiaContrasena(self):
        CRUD.cambiarContrasena(self.correo, self.textoContrasena.text())    
        self.parent.habilitarVentana(True)    
        self.close()