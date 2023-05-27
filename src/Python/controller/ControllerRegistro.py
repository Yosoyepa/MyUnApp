import datetime
import sys
import traceback


from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic


#import de model
from Python.model.CRUD import CRUD
from Python.model.Usuario import Usuario


from resources.QRC import images
class controllerRegistro(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Registro.ui', self)
        self.crd = CRUD()
        self.set_image_opacity(0.44)
        #Boton_Registro
        #self.Ingresar.clicked.connect(self.abrirMenu)

    def set_image_opacity(self, value):
        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.Label_Fondo)
        graphics_effect.setOpacity(value)
        self.Label_Fondo.setGraphicsEffect(graphics_effect)

    def registrar(self):
        
        user:Usuario = None
        if(self.Line_Nombre.text() == '' or self.Line_Apellido.text() == '' or self.Line_Email.text() == '' or self.Line_Contrasena.text() == '' or self.Line_ConfirmarContrasena.text() == ''):
            self.crd.mostrarCajaDeMensaje("ADVERTENCIA", 'No deje campos de texto vacíos', QtWidgets.QMessageBox.Warning)
            print("no deje campos vacíos")
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
                        self.crd.createUsuario(user)
                        
                    else:
                        print("La contraseña y la confirmación no coinciden")
                else:
                    print("el correo no es válido")
            except:
                print(traceback.format_exc())    
                                
            
        
        
'''
app = QtWidgets.QApplication(sys.argv)
controlador = controllerRegistro()
controlador.setWindowTitle("Registro")
controlador.set_image_opacity(0.44)
controlador.show()
app.exec_()
'''