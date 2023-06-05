import datetime
import sys
import traceback
import typing

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic



#import de model
from Python.model.CRUD import CRUD
from Python.model.Usuario import Usuario

from resources.QRC import images
from Python.model.Grupo import grupo


class ControllerBusquedaGrupo(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Grupos.ui',self)
        self.crd = CRUD()
        self.botoncreargrupo.clicked.connect(self.creargrupo)
        self.pushButton_8.clicked.connect(self.actualizar_lista_mis_grupos)


    def creargrupo(self):
        if self.Line_NombreGrupo.text() and self.Text_DescripcionGrupo.toPlainText() :
            grupotemporal=grupo(0,self.Line_NombreGrupo.text(),1,self.Text_DescripcionGrupo.toPlainText())
            self.crd.createGrupo(grupotemporal)
            self.crd.obtener_ultimo_ID_grupo()
        else:
            self.crd.mostrarCajaDeMensaje("Advertencia","No debe dejar espacios en blanco",QtWidgets.QMessageBox.Warning)
        self.Line_NombreGrupo.clear()
        self.Text_DescripcionGrupo.clear()

    def setUsuario(self, usr: Usuario):
        self.usuario = usr


    def actualizar_lista_mis_grupos(self):
        self.crd.obtener_nombres_grupo(self.usuario.correo)
        print(self.crd.Nombres_grupos)
        self.List_MisGrupos.clear()
        for nombre in self.crd.Nombres_grupos:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(nombre[0]))
            self.List_MisGrupos.addItem(item)

  

    
