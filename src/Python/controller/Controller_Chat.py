import sys
import threading
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from resources.QRC import images
from Python.model.Usuario import Usuario
from Python.model.CRUD import CRUD
import os
from google.cloud import pubsub_v1

from Python.model.CRUD import CRUD


credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


class controller_Chat(QMainWindow):
    mensaje_recibido = QtCore.pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Pagina_Chat.ui', self)
        uic.loadUi('src/resources/interface/Receptor.ui', self)
        self.pushButton_7.clicked.connect(self.actualizar_lista_widget_grupos)
        self.lista_grupos.itemClicked.connect(self.mostrar_miembros_grupos)
        self.send_button.clicked.connect(self.enviar_mensaje_a_topic)
        self.send_button.clicked.connect(self.enviar_mensaje)
        self.lista_grupos.itemClicked.connect(self.recibir_mensajes_topic)
        self.widgets_enviados = []
        self.widgets_recibidos = []
        self.receptor_widget = QtWidgets.QWidget()
        self.mensaje_recibido.connect(self.mostrar_mensaje_recibido)
        uic.loadUi('src/resources/interface/Receptor.ui', self.receptor_widget)


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
            self.widgets_enviados.append(sendWidget)
        self.message_line_edit.clear()

    def recibir_mensaje(self, mensaje):
        print("Mensaje recibido:", mensaje)
        if mensaje:
            receiveWidget = QtWidgets.QWidget()
            uic.loadUi('src/resources/interface/Receptor.ui', receiveWidget)
            receiveWidget.message_receptor.setText(str(mensaje))
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(receiveWidget.sizeHint())
            self.chat_listWidget.addItem(item)
            self.chat_listWidget.setItemWidget(item, receiveWidget)
            self.chat_listWidget.setMinimumWidth(receiveWidget.width())
            self.widgets_recibidos.append(receiveWidget)

    def mostrar_mensaje_recibido(self, mensaje):
        self.mensaje_recibido.emit(mensaje)

    def obtener_id_grupo(self, nombre_grupo):
        self.crd.obtener_id_grupo(nombre_grupo)
        return self.crd.id_grupo

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

    def setear_usuario(self, usr: Usuario):
        self.crd_usuario = usr
        nombre_usuario = str(self.crd_usuario.nombre + " " + self.crd_usuario.apellido)
        nombre_usuario = nombre_usuario.replace(" ", "_")
        print(nombre_usuario)
        return nombre_usuario

    def mostrar_miembros_grupos(self, item):
        grupo_seleccionado = item.text()
        nombre_grupo = grupo_seleccionado
        print(nombre_grupo, ":asdsad")
        self.crd.obtener_miembros_grupos(nombre_grupo)
        self.lista_miembros.clear()
        for miembro in self.crd.Miembros_grupos:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(miembro[0]) + " " + str(miembro[1]))
            self.lista_miembros.addItem(item)

        self.id_grupo_seleccionado = self.obtener_id_grupo(nombre_grupo)

    def enviar_mensaje_a_topic(self):
        texto_mensaje = str(self.message_line_edit.text())
        if texto_mensaje:
            project_id = 'exalted-summer-387903'
            publisher = pubsub_v1.PublisherClient()
            topic_name = self.crd.obtener_topic_grupo(self.id_grupo_seleccionado)
            topic_path = f'projects/{project_id}/topics/{topic_name}'
            future = publisher.publish(topic_path, texto_mensaje.encode())
            future.result()
            print(f'Mensaje enviado al topic {topic_name}: {texto_mensaje}')
        
    def recibir_mensajes_topic(self):
        project_id = 'exalted-summer-387903'
        subscriber = pubsub_v1.SubscriberClient()
        nombre_user = self.setear_usuario(self.usuario)
        subscription_name = f'{nombre_user}_subscription'
        subscription_path = subscriber.subscription_path(project_id, subscription_name)

        def callback(message):
            mensaje = message.data.decode()
            print(f"Mensaje recibido para {nombre_user}: {mensaje}")
            print("Mensaje recibido en el hilo secundario:", message.data.decode())
            self.mensaje_recibido.emit(mensaje)
            message.ack()

        thread = threading.Thread(target=lambda: subscriber.subscribe(subscription_path, callback=callback))
        thread.start()


