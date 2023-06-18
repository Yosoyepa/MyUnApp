import sys
import traceback

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Python.controller.ControllerCambioContrasena import controllerCambioContrasena

from resources.QRC import images




from Python.model import CRUD
from Python.model.Usuario import Usuario


class controllerCodigo(QMainWindow):
    def __init__(self, parent = None, parent2 = None,instruccion = True): #instruccion: true para cambiar contraseña, false para registrar
        
        QMainWindow.__init__(self)

        self.parent = parent # type: ignore
        self.parent2 = parent2

        self.controllerCambioContrasena = controllerCambioContrasena(self.parent)
        uic.loadUi('src/resources/interface/Ventana_Codigo.ui', self)
        self.set_image_opacity(0.44)

        
        if(instruccion):
            self.okButton.clicked.connect(self.cambioCambiarContrasena)
        else:
            self.okButton.clicked.connect(self.registrar)

        self.correo = None

        self.codigo = None

    
    def set_image_opacity(self, value):
        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.label_fondo)
        graphics_effect.setOpacity(value)
        self.label_fondo.setGraphicsEffect(graphics_effect)

    def generarCodigo(self, correo:str):        
        self.correo = correo
        self.codigo = CRUD.mandarCodigoVerificacion(self.correo)

    
    
    def registrar(self):
        if self.confirmarCodigo():
            CRUD.createUsuario(self.user)
            CRUD.mostrarCajaDeMensaje("COMPLETADO", "El registro fue completado existosamente :D .", QtWidgets.QMessageBox.Information)
            self.parent.cambioInicioSesionFromRegistro()
            self.parent2.habilitarVentana(True) #type: ignore
            self.close()

    def setUsuario(self, user: Usuario):
        self.user = user
    
    def cambioCambiarContrasena(self):
        if self.confirmarCodigo():
            self.controllerCambioContrasena.setCorreo(self.correo) #type: ignore
            self.controllerCambioContrasena.show()
            self.close()        
            
  
        


    def confirmarCodigo(self):

        if self.textoCodigo.text() == self.codigo :
            return True
        else:
            CRUD.mostrarCajaDeMensaje("ADVERTENCIA", "El código digitado no coincide con el enviado a su correo.", QtWidgets.QMessageBox.Warning)
            self.textoCodigo.setText("")
            return False
            
'''    
app = QtWidgets.QApplication(sys.argv)
controlador = controllerCodigo()
controlador.setWindowTitle("Recuperación contraseña")

controlador.show()
app.exec_()
'''