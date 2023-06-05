from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


#import de model
from Python.model.CRUD import CRUD
from Python.model.Usuario import Usuario


from controller.ControllerBusquedaGrupos import ControllerBusquedaGrupo



class ControllerAdminGrupo(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_AdministracionGrupos.ui',self)
        self.crd = CRUD()
        self.grupos = ControllerBusquedaGrupo()


    def abrirAjustes(self, usuario, nombreGrupo):
        if self.crd.admin(usuario,nombreGrupo) == True:
            return True
        else:
            self.crd.mostrarCajaDeMensaje("Error", "Usted no es administrador del grupo.", QMessageBox.Critical)
