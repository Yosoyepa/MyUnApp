import datetime
import sys
import traceback


from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic


#import de model
from Python.model import CRUD
from Python.model.Usuario import Usuario
from Python.controller.ControllerCodigo import controllerCodigo


from resources.QRC import images
class controllerRegistro(QMainWindow):
    def __init__(self, parent = None):
        


        self.parent = parent # type: ignore

        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Registro.ui', self)
        
        self.set_image_opacity(0.44)
        
        self.controllerCodigo = controllerCodigo(instruccion = False, parent = self.parent, parent2= self)



    def set_image_opacity(self, value):
        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.Label_Fondo)
        graphics_effect.setOpacity(value)
        self.Label_Fondo.setGraphicsEffect(graphics_effect)

    def registrar(self):
        
        user:Usuario = None # type: ignore
        if(self.Line_Nombre.text() == '' or self.Line_Apellido.text() == '' or self.Line_Email.text() == '' or self.Line_Contrasena.text() == '' or self.Line_ConfirmarContrasena.text() == ''):
            CRUD.mostrarCajaDeMensaje("ADVERTENCIA", 'No deje campos de texto vacíos', QtWidgets.QMessageBox.Warning)
            
        else:
            try:
                correoUnalArr = self.Line_Email.text().split("@", 1)
                correo_Unal = correoUnalArr[1]
                if correo_Unal == "unal.edu.co":
                    if self.Line_Contrasena.text() == self.Line_ConfirmarContrasena.text():
                        
                        user = Usuario(self.Line_Email.text(), self.Line_Nombre.text(), self.Line_Apellido.text(), datetime.datetime.now())
                        user.setFechaNacimiento(self.Fecha.text(), '/')
                        user.setContrasenaSinHash(self.Line_Contrasena.text())
                 
                        
                        user.mostrar()
                        self.controllerCodigo.generarCodigo(user.correo)
                        if self.controllerCodigo.codigo != None:
                            self.controllerCodigo.setUsuario(user)
                            self.limpiarCampos()
                            self.habilitarVentana(False)
                   
                            self.controllerCodigo.show()
                                            
                            
                        
                    else:
                        CRUD.mostrarCajaDeMensaje("ADVERTENCIA", 'La contraseña y la confirmación no coinciden.', QtWidgets.QMessageBox.Warning)
                        
                else:
                    CRUD.mostrarCajaDeMensaje("ADVERTENCIA", 'el correo no es válido.', QtWidgets.QMessageBox.Warning)
                    
            except:
                print(traceback.format_exc())    
                                
            
        
    def limpiarCampos(self):
        self.Line_Nombre.setText("")
        self.Line_Apellido.setText("")
        self.Line_Email.setText("")
        self.Line_Contrasena.setText("")
        self.Line_ConfirmarContrasena.setText("")
    

    def habilitarVentana(self, habilitar: bool):
        self.centralwidget.setEnabled(habilitar)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, habilitar) # type: ignore
        
'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerRegistro()
controlador.setWindowTitle("Registro")
controlador.set_image_opacity(0.44)
controlador.show()
app.exec_()
'''