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
        self.grupoEntrado = ""
        self.conexiones()

    def conexiones(self):
        self.Boton_Re1.clicked.connect(self.mostrarIntegrantes)
        self.Boton_Re2.clicked.connect(self.mostrarSolicitudes)


    def abrirAjustes(self, usuario, nombreGrupo):
        if self.crd.admin(usuario,nombreGrupo) == True:
            self.grupoEntrado = nombreGrupo
            return True
        else:
            self.crd.mostrarCajaDeMensaje("Error", "Usted no es administrador del grupo.", QMessageBox.Information)

    def mostrarIntegrantes(self):
        lista = self.crd.mostrarMiembrosGrupo(self.grupoEntrado)
        self.List_Integrantes.clear()
        for nombre in lista:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(nombre[0]))
            self.List_Integrantes.addItem(item)

    def mostrarSolicitudes(self):
        lista = self.crd.mostrarSolicitudes(self.grupoEntrado)
        self.List_Solicitudes.clear()
        if lista==None:
            self.crd.mostrarCajaDeMensaje("Advertencia", "No hay solicitudes de ingreso.", QMessageBox.Critical)
        else:
            for nombre in lista:
                item = QtWidgets.QListWidgetItem()
                item.setText(str(nombre[0]))
                self.List_Solicitudes.addItem(item)

    def dscIntegranteAdmin(self):
        Usuario = self.List_Integrantes.currentItem().text()
        self.crd.removerAdmin(Usuario,self.grupoEntrado)
        self.mostrarIntegrantes
