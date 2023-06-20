
import time
import traceback
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
from resources.QRC import images
from Python.model.Usuario import Usuario
from Python.model import CRUD
from PyQt5.QtGui import QIcon
#import os
#from google.cloud import pubsub_v1




#credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


class controller_Chat(QMainWindow):
    mensaje_recibido = QtCore.pyqtSignal(str)

    def __init__(self):

        self.hilo = None
        
        self.username_receptor = None
        self.username_mensajero = None
        
        QMainWindow.__init__(self)
        uic.loadUi('src/resources/interface/Ventana_Chat.ui', self)
        #uic.loadUi('src/resources/interface/Receptor.ui', self)
        self.pushButton_7.clicked.connect(self.actualizar_lista_widget_grupos)
        self.lista_grupos.itemClicked.connect(self.mostrar_miembros_grupos)

        self.send_button.clicked.connect(self.enviarMensaje)
        ##self.lista_grupos.itemClicked.connect(self.recibir_mensajes_topic)
        self.widgets_enviados = []
        self.widgets_recibidos = []
        self.receptor_widget = QtWidgets.QWidget()
        self.mensajero_widget = QtWidgets.QWidget()
        self.mensaje_recibido.connect(self.mostrar_mensaje_recibido)
        uic.loadUi('src/resources/interface/Receptor.ui', self.receptor_widget)
        self.username_receptor = self.receptor_widget.findChild(QtWidgets.QLabel, 'username_receptor')
        uic.loadUi('src/resources/interface/Mensajero.ui', self.mensajero_widget)
        self.username_mensajero = self.mensajero_widget.findChild(QtWidgets.QLabel, 'username_mensajero')
        self.icono_conexion_activo = 'src/resources/QRC/Icons/Online 2.png'
        self.icono_conexion_inactivo = 'src/resources/QRC/Icons/Online.png'
        self.cambio_manual = False
        
        


    def cajaMensajeEnviado(self, mensaje):
        print("Mensaje enviado:", mensaje)
        if mensaje:
            sendWidget = QtWidgets.QWidget()  
            uic.loadUi('src/resources/interface/Mensajero.ui', sendWidget)
            defaultPixmap = sendWidget.fotoPerfil.pixmap() #type: ignore
            sendWidget.message_mensajero.setText(str(mensaje))
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(sendWidget.sizeHint())
            self.chat_listWidget.addItem(item)
            self.chat_listWidget.setItemWidget(item, sendWidget)
            self.chat_listWidget.setMinimumWidth(sendWidget.width())
            self.widgets_enviados.append(sendWidget)
            if self.usuario.fotoPerfil == None:
                sendWidget.fotoPerfil.setPixmap(defaultPixmap) #type: ignore    
            else:

                pixmap = QtGui.QPixmap() #type: ignore
                   #type: ignore  
                pixmap.loadFromData(self.usuario.fotoPerfil) #type: ignore
                pixmap = pixmap.scaled(70, 70, QtCore.Qt.KeepAspectRatio) #type: ignore
                sendWidget.fotoPerfil.setPixmap(pixmap) #type: ignore

            sendWidget.username_mensajero.setText(self.usuario.nombre+" "+self.usuario.apellido)       

    def cajaMensajeRecibido(self, mensaje, correoReceptor):
        print("Mensaje recibido:", mensaje)
        if mensaje:
            receiveWidget = QtWidgets.QWidget()
            uic.loadUi('src/resources/interface/Receptor.ui', receiveWidget)
            defaultPixmap = receiveWidget.fotoPerfil.pixmap() #type: ignore
            receiveWidget.message_receptor.setText(str(mensaje))
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(receiveWidget.sizeHint())
            self.chat_listWidget.addItem(item)
            self.chat_listWidget.setItemWidget(item, receiveWidget)
            self.chat_listWidget.setMinimumWidth(receiveWidget.width())
            self.widgets_recibidos.append(receiveWidget)
            usuarioReceptor = CRUD.readUsuarioSinContrasena(correoReceptor)
            if usuarioReceptor.fotoPerfil == None: #type: ignore
                receiveWidget.fotoPerfil.setPixmap(defaultPixmap) #type: ignore    
            else:

                pixmap = QtGui.QPixmap() #type: ignore
                   #type: ignore  
                pixmap.loadFromData(usuarioReceptor.fotoPerfil) #type: ignore
                pixmap = pixmap.scaled(70, 70, QtCore.Qt.KeepAspectRatio) #type: ignore
                receiveWidget.fotoPerfil.setPixmap(pixmap) #type: ignore
            receiveWidget.username_receptor.setText(usuarioReceptor.nombre+" "+usuarioReceptor.apellido) #type: ignore

    def mostrar_mensaje_recibido(self, mensaje):
        self.mensaje_recibido.emit(mensaje)

    def obtener_id_grupo(self, nombre_grupo):        
        return CRUD.obtener_id_grupo(nombre_grupo)

    def actualizar_lista_widget_grupos(self):
        
        listaNombres = CRUD.obtener_nombres_grupo(self.usuario.correo) #type: ignore
        print(listaNombres)
        self.lista_grupos.clear()
        for nombre in listaNombres: #type: ignore
            item = QtWidgets.QListWidgetItem()
            item.setText(str(nombre[0])) #type: ignore
            self.lista_grupos.addItem(item)

    def setUsuario(self, usr: Usuario):
        self.usuario = usr        
                            

    def mostrar_miembros_grupos(self, item):
        self.chat_listWidget.clear()
        if self.hilo != None:
            self.hilo.terminate()

        self.grupo_seleccionado = item.text()
        nombre_grupo = self.grupo_seleccionado
        self.hilo = claseHilo(self.grupo_seleccionado)
        self.hilo.newValor.connect(self.cargarMensajes)
        self.hilo.start()	
        print(nombre_grupo)
        
        self.lista_miembros.clear()
        for miembro in CRUD.obtener_miembros_grupos(nombre_grupo):#type: ignore
            item = QtWidgets.QListWidgetItem()
            item.setText(str(miembro[0]) + " " + str(miembro[1]))
            # Agregar icono de conexión
            icono = QIcon(self.icono_conexion_activo)
            item.setIcon(icono)
            self.lista_miembros.addItem(item)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable) #type: ignore
             # Establecer el estado del ítem como activo solo si no se cambió manualmente
            if not self.cambio_manual:
                item.setCheckState(QtCore.Qt.Checked)#type: ignore

        self.id_grupo_seleccionado = self.obtener_id_grupo(nombre_grupo)
        # Conectar la señal itemChanged al método cambiar_estado_miembro
        self.lista_miembros.itemChanged.connect(self.cambiar_estado_miembro)

    def cambiar_estado_miembro(self, item):
        if not self.cambio_manual:
            self.cambio_manual = True
            if item.checkState() == QtCore.Qt.Checked:  # Estado activo # type: ignore
                item.setIcon(QIcon(self.icono_conexion_activo))
                # Realizar acciones cuando el miembro está activo
            else:  # Estado inactivo
                item.setIcon(QIcon(self.icono_conexion_inactivo))
                # Realizar acciones cuando el miembro está inactivo
            self.cambio_manual = False
    
    def cargarMensajes(self, newValor):                    
        try:    
            self.id_grupo_seleccionado = self.obtener_id_grupo(self.grupo_seleccionado)
            mensaje = newValor	
            
            
            if mensaje[1] == self.id_grupo_seleccionado:
                    print(mensaje[3])
                    if(mensaje[2] == self.usuario.correo):
                        self.cajaMensajeEnviado(mensaje[3])

                    else:
                        self.cajaMensajeRecibido(mensaje[3], mensaje[2])
                        print(mensaje[2])
        
        except:
            print(traceback.format_exc())
        

    def cargarTodosLosMensajes(self):
        try:
            mensajesListaTemp = CRUD.obtener_mensajes_grupo("TEST1")
            
            for mensaje in mensajesListaTemp:   #type: ignore                     
                self.cargarMensajes(mensaje)
        except:
            print(traceback.format_exc())


    def enviarMensaje(self):
        try:
            texto_mensaje = str(self.message_line_edit.text())
            if texto_mensaje:
                CRUD.enviar_mensaje_grupo(self.id_grupo_seleccionado, self.usuario.correo, texto_mensaje)                
                
                self.message_line_edit.clear()
        except:
            print(traceback.format_exc())


'''
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

'''

class claseHilo(QThread):
    newValor = pyqtSignal(tuple)
    def __init__(self, nombreGrupo = None):

        
        self.nombreGrupo = nombreGrupo
        super(claseHilo, self).__init__()


    def setGrupo(self, nombreGrupo):
        self.nombreGrupo = nombreGrupo

    def run(self):
        try:
            mensajesLista = []
            mensajesListaTemp = CRUD.obtener_mensajes_grupo(self.nombreGrupo)
            
          
            mensajesLista = mensajesListaTemp
            while True:
                
                    print("Hilo ejecutandose")                     
                    mensajesListaTemp = CRUD.obtener_mensajes_grupo(self.nombreGrupo)                                                                              
                    if mensajesListaTemp != mensajesLista:
                        mensajesLista = mensajesListaTemp
                        self.newValor.emit(mensajesListaTemp[-1])       #type: ignore  
                        print("-----------------------", mensajesListaTemp[-1])       #type: ignore
                    #time.sleep(0.25)
        except:
            print(traceback.format_exc())
            print("Error en el hilo")                    
