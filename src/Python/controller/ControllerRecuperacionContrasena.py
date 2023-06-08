import sys
import traceback

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Python.controller.ControllerCodigo import controllerCodigo


from resources.QRC import images

from Python.model.CRUD import CRUD
from Python.model.Usuario import Usuario


class controllerRecuperacion(QMainWindow):
    def __init__(self, parent = None):
        self.crd = CRUD()
        QMainWindow.__init__(self)

        self.parent = parent

        uic.loadUi('src/resources/interface/Ventana_Recuperacion.ui', self)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.set_image_opacity(0.44)

        self.controllerCodigo = controllerCodigo(parent= self.parent, instruccion = True)


        self.atrasButton.clicked.connect(self.funcionBotonAtras)
        self.continuarButton.clicked.connect(self.cambioCodigoFromRecuperacion)
        
    
    def set_image_opacity(self, value):
        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.label_fondo)
        graphics_effect.setOpacity(value)
        self.label_fondo.setGraphicsEffect(graphics_effect)


    def enviarCodigo(self) -> bool:
        try:
            if self.textoEmail.text() != "":
                correoUnalArr = self.textoEmail.text().split("@")
                correo_Unal = correoUnalArr[1]
                if correo_Unal == "unal.edu.co":      
                    if self.crd.usuarioExiste(self.textoEmail.text()):
                        
                        return True
                      
                    
                else:
                    self.crd.mostrarCajaDeMensaje("ADVERTENCIA", "El correo escrito no es de la UNAL.", QtWidgets.QMessageBox.Warning)
                    return False

            else:
                self.crd.mostrarCajaDeMensaje("ADVERTENCIA", "No ha escrito ningún correo.", QtWidgets.QMessageBox.Warning)
                return False
        except:
            self.crd.mostrarCajaDeMensaje("ADVERTENCIA", "El correo escrito no es válido.", QtWidgets.QMessageBox.Warning)
            print(traceback.format_exc())
            return False


    def cambioCodigoFromRecuperacion(self):    
        
        if self.enviarCodigo():
            
            self.controllerCodigo.generarCodigo(self.textoEmail.text())
            self.controllerCodigo.show()    
            self.close()

    def funcionBotonAtras(self):
        self.textoEmail.setText("")
        self.parent.habilitarVentana(True)
        self.close()
    
  

'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerCambio()
controlador.setWindowTitle("Recuperación contraseña")

controlador.show()
app.exec_()'''