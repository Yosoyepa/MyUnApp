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


class controllerbusquedaGrupo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Pagina_Grupos.ui',self)
        self.crd = CRUD()
        self.botoncreargrupo.clicked.connect(self.creargrupo)


    def creargrupo(self):
        if self.Line_NombreGrupo.text() and self.Text_DescripcionGrupo.toPlainText() :
            grupotemporal=grupo(0,self.Line_NombreGrupo.text(),1,self.Text_DescripcionGrupo.toPlainText())
            self.crd.createGrupo(grupotemporal)
        else:
            self.crd.mostrarCajaDeMensaje("Advertencia","No debe dejar espacios en blanco",QtWidgets.QMessageBox.Warning)
        self.Line_NombreGrupo.clear()
        self.Text_DescripcionGrupo.clear()
    
