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
        uic.loadUi('src/resources/interface/Receptor.ui', self)
        self.pushButton_7.clicked.connect(self.actualizar_lista_widget_grupos)
        self.lista_grupos.itemClicked.connect(self.mostrar_miembros_grupos)
        ##self.lista_grupos.itemClicked.connect(self.Mostrar_chat_grupal)
        self.send_button.clicked.connect(self.enviar_mensaje)
        # Cargar Mensajero.ui
        self.widgets_enviados = []
        #Cargar Receptor.ui
        self.receptor_widget = QtWidgets.QWidget()
        uic.loadUi('src/resources/interface/Receptor.ui', self.receptor_widget)
    ##Metodo para chats grupales

    # def Mostrar_chat_grupal(self, nombre_grupo):
    #     #Toma el nombre del grupo
    #     nombre_grupo = self.lista_grupos.currentItem().text()
    #     #Limpiar el contenido existente en el area del chat
    #     ##Pendiente de implementar.
    #     #Obtener los mensajes del grupo
    #     self.crd.obtener_mensajes_grupo(nombre_grupo)
    #     #Mostrar los mensajes en el area del chat
    #     for mensaje in self.crd.Mensajes_grupo:
    #         self.widget_chat.append(mensaje[0] + "a las " + mensaje[1] + "de:" + mensaje[2])

    # Metodo para tomar el texto que digita el usuario y enviarlo al chat grupal mediante el line_text_chat
    def enviar_mensaje(self):
        texto_mensaje = str(self.message_line_edit.text())
        if texto_mensaje:
            sendWidget = QtWidgets.QWidget()
            uic.loadUi('src/resources/interface/Mensajero.ui', sendWidget)
            sendWidget.message_mensajero.setText(texto_mensaje)
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(sendWidget.sizeHint())
            self.chat_listWidget.addItem(item)
            self.chat_listWidget.setItemWidget(item, sendWidget)
            self.chat_listWidget.setMinimumWidth(sendWidget.width())
            # Agregar el widget a la lista de widgets enviados
            self.widgets_enviados.append(sendWidget)
        #Liampi el campo de texto despues de enviar el mensaje
        self.message_line_edit.clear()

    def recibir_mensaje(self, mensaje):
        if mensaje:
            receiveWidget = self.receptor_widget
            receiveWidget.message_receptor.setText(str(mensaje))
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(receiveWidget.sizeHint())
            self.chat_listWidget.addItem(item)
            self.chat_listWidget.setItemWidget(item, receiveWidget)
            self.chat_listWidget.setMinimumWidth(receiveWidget.width())
        



    def obtener_id_grupo(self, nombre_grupo):
        self.crd.obtener_id_grupo(nombre_grupo)
        return self.crd.id_grupo


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

    
