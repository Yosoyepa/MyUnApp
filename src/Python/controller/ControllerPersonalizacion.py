import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import traceback
#imports de controladores

from resources.QRC import images

#import de model
from Python.model import CRUD
from Python.model.Usuario import Usuario

class ControllerPersonalizacion(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Personalizacion.ui', self)
        
        
        self.labelImagen = self.findChild(QLabel, "imagenPerfil")
        self.defaultPixmap = self.imagenPerfil.pixmap() # type: ignore

        self.cambiarImagen.clicked.connect(self.cargarImagenPerfil)
        self.botonAplicarCambios.clicked.connect(self.aplicarCambios)
        self.botonEliminarFoto.clicked.connect(self.eliminarFoto)

    def cargarImagenPerfil(self):
        try:
            archivo = QFileDialog.getOpenFileName(self, "Abrir archivo", "C:\\", "Archivos de imagen (*.jpg *.png)")
            if archivo[0] != "":
                self.blob = self.cargarImagen(archivo[0])
                self.setPixmap(self.blob)
                self.usuario.fotoPerfil = self.blob
                self.botonAplicarCambios.setEnabled(True)
                self.mostrarTexto = "Se ha cambiado la foto de perfil con exito."
        except:
            print(traceback.format_exc())

    def aplicarCambios(self):                        
        try:
            CRUD.actualizarImagenPerfil(self.usuario.fotoPerfil, self.usuario.correo)        
            self.botonAplicarCambios.setEnabled(False)
            CRUD.mostrarCajaDeMensaje("COMPLETADO", self.mostrarTexto, QtWidgets.QMessageBox.Information) # type: ignore
        except:
            print(traceback.format_exc())

    def setUsuario(self, usuario: Usuario):
        self.usuario = usuario
        self.setPixmap(self.usuario.fotoPerfil)
        self.setDatos()
        
    def cargarImagen(self, rutaImagen: str):
        with open(rutaImagen, 'rb') as file:
            binaryData = file.read()                        
        return binaryData # type: ignore      
      

    
    def setPixmap(self, fotoPerfil: bytes):
        try:
            #abrir imagen
            self.pixmap = QtGui.QPixmap()
            self.pixmap.loadFromData(fotoPerfil)
            # type: ignore
            if (self.pixmap.width() > 300 or self.pixmap.height() > 300):
                self.pixmap = self.pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio) # type: ignore
                self.labelImagen.setPixmap(self.pixmap) # type: ignore                                                                            
        except:
            print(traceback.format_exc())
    
    def setDatos(self):
        self.labelCorreo.setText(self.usuario.correo)
        self.labelNombres.setText(self.usuario.nombre)
        self.labelApellidos.setText(self.usuario.apellido)
        self.labelFecha.setText(str(self.usuario.fechaNacimiento))

    def eliminarFoto(self):
        self.labelImagen.setPixmap(self.defaultPixmap) # type: ignore
        self.usuario.fotoPerfil = None        
        self.botonAplicarCambios.setEnabled(True)
        self.mostrarTexto = "Se ha eliminado la foto de perfil con exito."