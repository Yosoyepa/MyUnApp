import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from resources.QRC import images
from Python.model.Usuario import Usuario
from Python.model.CRUD import CRUD

import os
from google.pubsub_v1 import PubsubMessage
from google import pubsub_v1




from Python.model.CRUD import CRUD


credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path




class controller_Chat(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Pagina_Chat.ui', self)
        uic.loadUi('src/resources/interface/Receptor.ui', self)
        self.pushButton_7.clicked.connect(self.actualizar_lista_widget_grupos)
        self.lista_grupos.itemClicked.connect(self.mostrar_miembros_grupos)
        ##self.lista_grupos.itemClicked.connect(self.Mostrar_chat_grupal)
        self.send_button.clicked.connect(self.enviar_mensaje)
        self.send_button.clicked.connect(self.enviar_mensaje_a_topic)
        self.lista_grupos.itemClicked.connect(self.crear_suscripcion)
        self.lista_grupos.itemClicked.connect(self.recibir_mensajes_topic)
        # Cargar Mensajero.ui
        self.widgets_enviados = []
        self.widgets_recibidos = []
        #Cargar Receptor.ui
        self.receptor_widget = QtWidgets.QWidget()
        uic.loadUi('src/resources/interface/Receptor.ui', self.receptor_widget)

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

    def recibir_mensaje(self,mensaje):
        if mensaje:
            receiveWidget = QtWidgets.QWidget()
            uic.loadUi('src/resources/interface/Receptor.ui', receiveWidget)
            receiveWidget.message_receptor.setText(str(mensaje))
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(receiveWidget.sizeHint())
            self.chat_listWidget.addItem(item)
            self.chat_listWidget.setItemWidget(item, receiveWidget)
            self.chat_listWidget.setMinimumWidth(receiveWidget.width())
            # Agregar el widget a la lista de widgets recibidos
            self.widgets_recibidos.append(receiveWidget)
        



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

    def setear_usuario(self, usr: Usuario):
        self.crd_usuario = usr
        nombre_usuario = str(self.crd_usuario.nombre + " " + self.crd_usuario.apellido)
        nombre_usuario = nombre_usuario.replace(" ", "_")
        print(nombre_usuario)
        return  nombre_usuario
    

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

    def crear_suscripcion(self,item):
    # Configurar el cliente de Pub/Sub
        nombre_grupo = item.text()
        id_grupo = self.obtener_id_grupo(nombre_grupo)
        print(id_grupo)
        project_id = 'exalted-summer-387903'
        subscriber = pubsub_v1.SubscriberClient()
        topic_name = self.crd.obtener_topic_grupo(id_grupo)
        print(topic_name)

        #Comprobar que el usuario no tiene una suscripción al topic
        nombre_user = self.setear_usuario(self.usuario)
        # Crear el nombre de la suscripción
        subscription_name = f'{nombre_user}_subscription'
        print(subscription_name)
        #Crear la suscripción
        topic_path = f'projects/{project_id}/topics/{topic_name}'
        subscription_path = f'projects/{project_id}/subscriptions/{subscription_name}'


        subscription = pubsub_v1.Subscription(name=subscription_path, topic=topic_path)
        subscriber.create_subscription(request=subscription)

    def enviar_mensaje_a_topic(self,item):
        # Configurar el cliente de Pub/Sub
        texto_mensaje = str(self.message_line_edit.text())
        if texto_mensaje:
            nombre_grupo = item.text()
            id_grupo = self.obtener_id_grupo(nombre_grupo)
            project_id = 'exalted-summer-387903'
            publisher = pubsub_v1.PublisherClient()
            topic_name = self.crd.obtener_topic_grupo(id_grupo)
            # Obtener el topic del chat grupal
            topic_path = f'projects/{project_id}/topics/{topic_name}'

            # Publicar el mensaje en el topic del chat grupal
            future = publisher.publish(topic_path,texto_mensaje.encode())
            future.result()
            print(f'Mensaje enviado al topic {topic_name}: {texto_mensaje}')
        
    
    def recibir_mensajes_topic(self):
        # Configurar el cliente de Pub/Sub
        project_id = 'exalted-summer-387903'
        subscriber = pubsub_v1.SubscriberClient()
        # Obtener la suscripción del usuario
        subscription_name = f'{self.setear_usuario}_subscription'
        subscription_path = subscriber.subscription_path(project_id, subscription_name)
        def callback(message):
            print(f"Mensaje recibido para {self.setear_usuario}: {message.data.decode()}")
            self.recibir_mensaje(message.data.decode())
        # Aceptar el mensaje para que no se reenvíe
            message.ack()
        # Iniciar la escucha de mensajes
        future = subscriber.subscribe(subscription_path, callback=callback)
        try:
            future.result()
        except KeyboardInterrupt:
            future.cancel()

