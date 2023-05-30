import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from resources.QRC import images
from Python.model.Usuario import Usuario
from Python.model.CRUD import CRUD



class controller_Chat(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Pagina_Chat.ui', self)
        self.pushButton_7.clicked.connect(self.actualizar_lista_widget_grupos)
        self.lista_grupos.itemClicked.connect(self.mostrar_miembros_grupos)
    
    ##Metodo para chats grupales

    def chat_grupal(self, nombre_grupo):
        #Limpiar el contenido existente en el area del chat
        self.widget_chat.clear()
        #Obtener los mensajes del grupo
        self.crd.obtener_mensajes_grupo(nombre_grupo)
        pass



    ##Metodos para saber los grupos a los que pertenece el usuario y los miembros de cada grupo
    def actualizar_lista_widget_grupos(self):
        self.crd = CRUD()
        self.crd.obtener_nombres_grupo(self.usuario.correo) 
        print(self.crd.Nombres_grupos)
        self.lista_grupos.clear()
        for nombre in self.crd.Nombres_grupos:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(nombre[0]))
            self.lista_grupos.addItem(item)


    def set_usuario(self, usr: Usuario):
        self.usuario = usr

    def mostrar_miembros_grupos(self, item):
        grupo_seleccionado = item.text()
        nombre_grupo = grupo_seleccionado
        print(nombre_grupo,":asdsad")
        self.crd.obtener_miembros_grupos(nombre_grupo)
        self.lista_miembros.clear()
        for miembro in self.crd.Miembros_grupos:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(miembro[0])+ " " + str(miembro[1]))
            self.lista_miembros.addItem(item)

    
