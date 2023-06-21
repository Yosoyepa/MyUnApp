import datetime
import sys
import traceback
import typing

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic



#import de model
from Python.model import CRUD
from Python.model.Usuario import Usuario

from resources.QRC import images
from Python.model.Grupo import grupo


class ControllerBusquedaGrupo(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Grupos.ui',self)
        
        self.botoncreargrupo.clicked.connect(self.creargrupo)
        self.pushButton_8.clicked.connect(self.actualizar_lista_mis_grupos)
        self.Boton_BusGrupo.clicked.connect(self.actualizar_lista_todoslosgrupos)
        self.solButton.clicked.connect(self.enviar_solicitud)
        self.List_BuscGrupos.itemClicked.connect(self.sel_grupo)
        self.Boton_Eliminar.clicked.connect(self.salirGrupo)
        self.Boton_lupa.clicked.connect(self.actualizar_lista_de_un_grupo_especifico)


    def creargrupo(self):
        if self.Line_NombreGrupo.text() and self.Text_DescripcionGrupo.toPlainText() :
            grupotemporal=grupo(0,self.Line_NombreGrupo.text(),1,self.Text_DescripcionGrupo.toPlainText())
            CRUD.createGrupo(grupotemporal,self.usuario)
            CRUD.obtener_ultimo_ID_grupo()
        else:
            CRUD.mostrarCajaDeMensaje("Advertencia","No debe dejar espacios en blanco",QtWidgets.QMessageBox.Warning)
        self.Line_NombreGrupo.clear()
        self.Text_DescripcionGrupo.clear()

    def setUsuario(self, usr: Usuario):
        self.usuario = usr


    def actualizar_lista_mis_grupos(self):
        nombresGrupo = CRUD.obtener_nombres_grupo(self.usuario.correo)
        print(nombresGrupo)
        self.List_MisGrupos.clear()
        for nombre in nombresGrupo: #type: ignore
            item = QtWidgets.QListWidgetItem()
            item.setText(str(nombre[0]))
            self.List_MisGrupos.addItem(item)
    
    def salirGrupo(self):
        try:
            grupoTemp = self.List_MisGrupos.currentItem().text()
            usuarios = CRUD.mostrarMiembrosGrupo(grupoTemp)
            cantidaAdmin = CRUD.buscarSiHayAdmin(grupoTemp)
            if cantidaAdmin > 1 or (cantidaAdmin == 1 and CRUD.admin(self.usuario.correo,grupoTemp)==False): #type: ignore
                CRUD.eliminarPersona(self.usuario.correo,grupoTemp)
                CRUD.mostrarCajaDeMensaje("Informacion", "Usted ha salido del grupo "+grupoTemp+" satisfactoriamente", QtWidgets.QMessageBox.Information)
            else:
                if len(usuarios) == 1:#type: ignore
                    CRUD.eliminarPersona(self.usuario.correo,grupoTemp)
                    CRUD.mostrarCajaDeMensaje("Informacion", "Usted ha salido del grupo "+grupoTemp+" satisfactoriamente", QtWidgets.QMessageBox.Information)
                    CRUD.eliminarGrupo(grupoTemp)
                else:
                    CRUD.mostrarCajaDeMensaje("Advertencia","El grupo no puede quedar sin administradores",QtWidgets.QMessageBox.Warning)
        except:
            CRUD.mostrarCajaDeMensaje("Advertencia","Debe escojer un grupo",QtWidgets.QMessageBox.Warning)


    def actualizar_lista_de_un_grupo_especifico(self):
        if nombreGrupo := self.Busqueda_grupos.text():
            resultados = CRUD.obtener_nombres_grupo_especifico(nombreGrupo)
            print(resultados)
            self.List_BuscGrupos.clear()
            for nombre in resultados: #type: ignore
                item = QtWidgets.QListWidgetItem()
                item.setText(str(nombre[0]))
                self.List_BuscGrupos.addItem(item)
        else:
            CRUD.mostrarCajaDeMensaje("Advertencia","No debe dejar espacios en blanco",QtWidgets.QMessageBox.Warning)
        self.Busqueda_grupos.clear()
    
    def actualizar_lista_todoslosgrupos(self):

        nombresGrupos = CRUD.obtener_nombres_todoslosgrupos()
        print(nombresGrupos)
        self.List_BuscGrupos.clear()
        for nombre in nombresGrupos: #type: ignore
            item = QtWidgets.QListWidgetItem()
            item.setText(str(nombre[0]))
            self.List_BuscGrupos.addItem(item)

    def sel_grupo(self, item):
        grupo_seleccionado=item.text()
        self.idgrupo= CRUD.obtener_id(grupo_seleccionado)
        print(self.idgrupo)


    def enviar_solicitud(self):
        CRUD.Enviar_sol(self.usuario , self.idgrupo)

            
            




    
