from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


#import de model
from Python.model import CRUD
from Python.model.Usuario import Usuario





class ControllerAdminGrupo(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_AdministracionGrupos.ui',self)
        
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
        self.Boton_Actualizar.clicked.connect(self.actualizarNombre)
        self.Boton_Limpiar.clicked.connect(self.limpiar2)


    def limpiar(self):
        self.List_Integrantes.clear()
        self.List_Solicitudes.clear()


    def abrirAjustes(self, usuario, nombreGrupo):
        if CRUD.admin(usuario,nombreGrupo) == True:
            self.usuarioDentro = usuario
            self.grupoEntrado = nombreGrupo
            return True
        else:
            CRUD.mostrarCajaDeMensaje("Error", "Usted no es administrador del grupo.", QMessageBox.Critical)

    def mostrarIntegrantes(self):
        lista = CRUD.mostrarMiembrosGrupo(self.grupoEntrado)
        self.List_Integrantes.clear()
        for nombre in lista: #type: ignore
            item = QtWidgets.QListWidgetItem()
            item.setText(str(nombre[0]))
            self.List_Integrantes.addItem(item)

    def mostrarSolicitudes(self):
        lista = CRUD.mostrarSolicitudes(self.grupoEntrado)
        self.List_Solicitudes.clear()
        if lista==None:
            CRUD.mostrarCajaDeMensaje("Advertencia", "No hay solicitudes de ingreso.", QMessageBox.Information)
        else:
            for nombre in lista:
                item = QtWidgets.QListWidgetItem()
                item.setText(str(nombre[0]))
                self.List_Solicitudes.addItem(item)

    def dscIntegranteAdmin(self):
        try:
            Usuario = self.List_Integrantes.currentItem().text()
            cantidaAdmin = CRUD.buscarSiHayAdmin(self.grupoEntrado)
            if self.usuarioDentro == Usuario:
                CRUD.mostrarCajaDeMensaje("Informacion", "No te puedes quitar tu mismo el administrador", QMessageBox.Information)
            else:
                if cantidaAdmin > 1:#type: ignore
                    if CRUD.admin(Usuario,self.grupoEntrado)==True:
                        CRUD.removerAdmin(Usuario,self.grupoEntrado)
                        texto = "El usuario "+Usuario+" ya no es administrador"
                        CRUD.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
                        self.mostrarIntegrantes
                    else:
                        CRUD.mostrarCajaDeMensaje("Informacion", "El usuario no es administrador", QMessageBox.Information)
                else:
                    CRUD.mostrarCajaDeMensaje("Advertencia", "El grupo no puede quedar sin administradores", QMessageBox.Critical)
        except:
            CRUD.mostrarCajaDeMensaje("Advertencia","Debe escojer un usuario",QtWidgets.QMessageBox.Warning)

    def ascIntegranteAdmin(self):
        try:
            Usuario = self.List_Integrantes.currentItem().text()
            if Usuario == self.usuarioDentro:
                CRUD.mostrarCajaDeMensaje("Informacion", "Usted ya es administrador", QMessageBox.Information)
            else:
                CRUD.ascenderAdmin(Usuario,self.grupoEntrado)
                texto = "El usuario "+Usuario+" ahora es administrador"
                CRUD.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
                self.mostrarIntegrantes
        except:
            CRUD.mostrarCajaDeMensaje("Advertencia","Debe escojer un usuario",QtWidgets.QMessageBox.Warning)

    def eliminarUser(self):
        try:
            Usuario = self.List_Integrantes.currentItem().text()
            cantidaAdmin = CRUD.buscarSiHayAdmin(self.grupoEntrado)
            if Usuario == self.usuarioDentro:
                CRUD.mostrarCajaDeMensaje("Advertencia", "No se puede eliminar a usted mismo", QMessageBox.Critical)
            else:
                if cantidaAdmin > 1 or (cantidaAdmin == 1 and CRUD.admin(Usuario,self.grupoEntrado)==False): #type: ignore
                    CRUD.eliminarPersona(Usuario,self.grupoEntrado)
                    texto = "El usuario "+Usuario+" ha sido eleminido del grupo"
                    CRUD.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
                else: 
                    CRUD.mostrarCajaDeMensaje("Advertencia", "El grupo no puede quedar sin administradores", QMessageBox.Critical)
        except:
            CRUD.mostrarCajaDeMensaje("Advertencia","Debe escojer un usuario",QtWidgets.QMessageBox.Warning)

    def aceptarSolicitud(self):
        try:
            Usuario = self.List_Solicitudes.currentItem().text()
            CRUD.aceptarSolicitud(Usuario,self.grupoEntrado)
            texto = "El usuario "+Usuario+" a sido aceptado en el grupo"
            CRUD.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
            self.mostrarSolicitudes
        except:
            CRUD.mostrarCajaDeMensaje("Advertencia","Debe escojer un usuario",QtWidgets.QMessageBox.Warning)

    def rechazarSolicitud(self):
        try:
            Usuario = self.List_Solicitudes.currentItem().text()
            CRUD.rechazarSolicitud(Usuario,self.grupoEntrado)
            texto = "El usuario "+Usuario+" no ha entrado al grupo"
            CRUD.mostrarCajaDeMensaje("Informacion", texto, QMessageBox.Information)
            self.mostrarSolicitudes
        except:
            CRUD.mostrarCajaDeMensaje("Advertencia","Debe escojer un usuario",QtWidgets.QMessageBox.Warning)

    def actualizarNombre(self):
        nuevoNombre = self.Line_NewNombre.text()
        nuevaDescripcion = self.Text_Descripcion.toPlainText()
        if nuevoNombre != "" and nuevaDescripcion != "" :
            CRUD.cambiarDescripcionGrupo(self.grupoEntrado,nuevaDescripcion)
            CRUD.cambiarNombreGrupo(self.grupoEntrado,nuevoNombre)
            self.grupoEntrado = nuevoNombre
            CRUD.mostrarCajaDeMensaje("Informacion", "Nombre y descripcion actualizados correctamente", QMessageBox.Information)
        elif nuevoNombre == "" and nuevaDescripcion != "" :
            CRUD.cambiarDescripcionGrupo(self.grupoEntrado,nuevaDescripcion)
            CRUD.mostrarCajaDeMensaje("Informacion", "Descripcion actualizada correctamente", QMessageBox.Information)
        elif nuevoNombre != "" and nuevaDescripcion == "" :
            CRUD.cambiarNombreGrupo(self.grupoEntrado,nuevoNombre)
            self.grupoEntrado = nuevoNombre
            CRUD.mostrarCajaDeMensaje("Informacion", "Nombre actualizado correctamente", QMessageBox.Information)
        else:
            CRUD.mostrarCajaDeMensaje("Advertencia", "Rellene alguno de los espacios", QMessageBox.Critical)
        self.limpiar2()

    def limpiar2(self):
        self.Line_NewNombre.clear()
        self.Text_Descripcion.clear()