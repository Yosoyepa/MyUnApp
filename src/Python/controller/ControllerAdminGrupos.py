from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic



#import de model
from Python.model.CRUD import CRUD
from Python.model.Usuario import Usuario

from resources.QRC import images
from Python.model.Grupo import grupo


class ControllerAdminGrupo(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_AdministracionGrupos.ui',self)
        self.crd = CRUD()

    def abrirAjustes(self):
        self.clicked = self.List_MisGrupos.currentRow()
        print(self.clicked)
        return True
