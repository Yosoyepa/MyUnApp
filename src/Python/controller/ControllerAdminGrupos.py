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
        self.usuarioDentro = ""
        self.conexiones()

    def conexiones(self):
        self.Boton_Re1.clicked.connect(self.mostrarIntegrantes)
        self.Boton_Re2.clicked.connect(self.mostrarSolicitudes)
        self.Boton_QuitarAdmin.clicked.connect(self.dscIntegranteAdmin)
        self.Boton_DarAdmin.clicked.connect(self.ascIntegranteAdmin)
        self.Boton_Eliminar.clicked.connect(self.eliminarUser)
        self.Boton_Aceptar.clicked.connect(self.aceptarSolicitud)
        self.Boton_Denegar.clicked.connect(self.rechazarSolicitud)


    def limpiar(self):
        self.List_Integrantes.clear()
        self.List_Solicitudes.clear()


    def abrirAjustes(self, usuario, nombreGrupo):
        if self.crd.admin(usuario,nombreGrupo) == True:
            self.usuarioDentro = usuario
            self.grupoEntrado = nombreGrupo
            return True
        else:
            self.crd.mostrarCajaDeMensaje("Error", "Usted no es administrador del grupo.", QMessageBox.Critical)

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
            self.crd.mostrarCajaDeMensaje("Advertencia", "No hay solicitudes de ingreso.", QMessageBox.Information)
        else:
            for nombre in lista:
                item = QtWidgets.QListWidgetItem()
                item.setText(str(nombre[0]))
                self.List_Solicitudes.addItem(item)

    def dscIntegranteAdmin(self):
        Usuario = self.List_Integrantes.currentItem().text()
        if self.crd.buscarSiHayAdmin(self.grupoEntrado)==True:
            self.crd.removerAdmin(Usuario,self.grupoEntrado)
            texto = "El usuario "+Usuario+" ya no es administrador"
            self.crd.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
            self.mostrarIntegrantes
        else:
            self.crd.mostrarCajaDeMensaje("Advertencia", "El grupo no puede quedar sin administradores", QMessageBox.Critical)

    def ascIntegranteAdmin(self):
        Usuario = self.List_Integrantes.currentItem().text()
        if Usuario == self.usuarioDentro:
            self.crd.mostrarCajaDeMensaje("Informacion", "Usted ya es administrador", QMessageBox.Information)
        else:
            self.crd.ascenderAdmin(Usuario,self.grupoEntrado)
            texto = "El usuario "+Usuario+" ahora es administrador"
            self.crd.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
            self.mostrarIntegrantes

    def eliminarUser(self):
        Usuario = self.List_Integrantes.currentItem().text()
        if Usuario == self.usuarioDentro:
            self.crd.mostrarCajaDeMensaje("Advertencia", "No se puede eliminar a usted mismo", QMessageBox.Critical)
        else:
            if self.crd.buscarSiHayAdmin==True:
                self.crd.eliminarPersona(Usuario)
                texto = "El usuario "+Usuario+" ha sido eleminido del grupo"
                self.crd.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
            else: 
                self.crd.mostrarCajaDeMensaje("Advertencia", "El grupo no puede quedar sin administradores", QMessageBox.Critical)

    def aceptarSolicitud(self):
        Usuario = self.List_Solicitudes.currentItem().text()
        self.crd.aceptarSolicitud(Usuario,self.grupoEntrado)
        texto = "El usuario "+Usuario+" a sido aceptado en el grupo"
        self.crd.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
        self.mostrarSolicitudes

    def rechazarSolicitud(self):
        Usuario = self.List_Solicitudes.currentItem().text()
        self.crd.rechazarSolicitud(Usuario,self.grupoEntrado)
        texto = "El usuario "+Usuario+" no ha entrado al grupo"
        self.crd.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
        self.mostrarSolicitudes
