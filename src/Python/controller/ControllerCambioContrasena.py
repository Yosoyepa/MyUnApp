import sys
import traceback

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from resources.QRC import images

from model.CRUD import CRUD
from Python.model.Usuario import Usuario


class controllerCambio(QMainWindow):
    def __init__(self):
        self.crd = CRUD()
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Recuperacion.ui', self)
        self.set_image_opacity(0.44)
        
        
        self.continuarButton.clicked.connect(self.enviarCodigo)
    
    def set_image_opacity(self, value):
        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.label_fondo)
        graphics_effect.setOpacity(value)
        self.label_fondo.setGraphicsEffect(graphics_effect)


    def enviarCodigo(self):
        try:
            correoUnalArr = self.textoEmail.text().split("@", 1)
            correo_Unal = correoUnalArr[1]
            if self.textoEmail.text() != "":
                if correo_Unal != "unal.edu.co":
                    self.crd.mandarCodigoVerificacion(self.textoEmail.text())
                else:
                    self.crd.mostrarCajaDeMensaje("ADVERTENCIA", "El correo escrito no es de la UNAL", QtWidgets.QMessageBox.Warning)
            else:
                self.crd.mostrarCajaDeMensaje("ADVERTENCIA", "No ha escrito ningún correo", QtWidgets.QMessageBox.Warning)
        except:
            print(traceback.format_exc())
        self.crd.mandarCodigoVerificacion(self.textoEmail.text())

'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerCambio()
controlador.setWindowTitle("Recuperación contraseña")

controlador.show()
app.exec_()'''