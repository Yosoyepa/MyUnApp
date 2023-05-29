import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic

#imports de vistas
from Python.controller.ControllerMenu import controllerMenu
from resources.QRC import images

#import de model
from Python.model.CRUD import CRUD
from Python.model.Usuario import Usuario



class controllerInicioSesion(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Ingreso.ui', self)
        self.set_image_opacity(0.44)
    	
        self.crd = CRUD()
        #ventanas
        self.menu = controllerMenu()

    def set_image_opacity(self, value):
        graphics_effect = QtWidgets.QGraphicsOpacityEffect(self.Label_Imagen)
        graphics_effect.setOpacity(value)
        self.Label_Imagen.setGraphicsEffect(graphics_effect)

    def abrirMenu(self) -> bool: ###RETORNA BOOLEANO PARA COMPROBAR QUE EL INICIO DE SESION FUE CORRECTO
        if self.Line_Usuario.text() == '' or self.Line_Contrasena.text() == '':
            self.crd.mostrarCajaDeMensaje("ADVERTENCIA", "no deje campos de texto vacíos.", QtWidgets.QMessageBox.Warning) 
            return False
        else:
        
            usr: Usuario = self.crd.readUsuario(self.Line_Usuario.text(), self.Line_Contrasena.text())
            print(usr)
            if(usr != None):
                usr.mostrar()
                self.menu.show()        
                return True
            else: 
                return False

    

    
    
'''

app = QtWidgets.QApplication(sys.argv)
controlador = controllerInicioSesion()
controlador.setWindowTitle("Iniciar Sesion")
controlador.set_image_opacity(0.44)
controlador.show()
app.exec_()
'''