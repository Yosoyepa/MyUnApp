
import time
import traceback
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
from resources.QRC import images
from Python.model.Usuario import Usuario
from Python.model import CRUD
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
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
        self.pushButton_7.clicked.connect(self.actualizar_lista_widget_grupos)
        self.lista_grupos.itemClicked.connect(self.mostrar_miembros_grupos)
        self.send_button.clicked.connect(self.enviarMensaje)
        self.widgets_enviados = []
        self.widgets_recibidos = []
        self.receptor_widget = QtWidgets.QWidget()
        self.mensajero_widget = QtWidgets.QWidget()
        self.mensaje_recibido.connect(self.mostrar_mensaje_recibido)
        uic.loadUi('src/resources/interface/Receptor.ui', self.receptor_widget)
        self.username_receptor = self.receptor_widget.findChild(QtWidgets.QLabel, 'username_receptor')
        uic.loadUi('src/resources/interface/Mensajero.ui', self.mensajero_widget)
        self.username_mensajero = self.mensajero_widget.findChild(QtWidgets.QLabel, 'username_mensajero')
        self.icono_conexion_activo = 'src/resources/QRC/Icons/Online.png'
        self.icono_conexion_inactivo = 'src/resources/QRC/Icons/Online 2.png'
        self.cambio_manual = False
        self.disponible = True
        
        
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
        self.chat_listWidget.clear() #type: ignore

        # Detener el hilo actual si existe
        if self.hilo is not None:
            self.hilo.activo = False
            self.hilo.wait()
        
        self.usuario_actual = self.usuario.nombre + " " + self.usuario.apellido
        self.grupo_seleccionado = item.text() #type: ignore
        nombre_grupo = self.grupo_seleccionado

        # Verificar el estado de la casilla de verificación del usuario actual
        usuario_actual_activo = True  # Usuario activo por defecto
        for miembro in CRUD.obtener_miembros_grupos(nombre_grupo): #type: ignore
            if miembro[0] == self.usuario_actual:
                usuario_actual_activo = item.checkState() == QtCore.Qt.Checked #type: ignore
                break

        # Iniciar el hilo solo si el usuario actual está activo
        if usuario_actual_activo:
            self.hilo = claseHilo(self.grupo_seleccionado)
            self.hilo.newValor.connect(self.cargarMensajes)
            self.hilo.start()

        self.lista_miembros.clear()
        

        for miembro in CRUD.obtener_miembros_grupos(nombre_grupo): #type: ignore
            item = QtWidgets.QListWidgetItem()
            item.setText(str(miembro[0]) + " " + str(miembro[1]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable) #type: ignore
            if miembro[0] == self.usuario_actual:
                item.setCheckState(QtCore.Qt.Checked if usuario_actual_activo else QtCore.Qt.Unchecked) #type: ignore
            else:
                item.setCheckState(QtCore.Qt.Unchecked) #type: ignore
            icono = QIcon(self.icono_conexion_activo if usuario_actual_activo else self.icono_conexion_inactivo)
            item.setIcon(icono)
            self.lista_miembros.addItem(item)

        self.id_grupo_seleccionado = self.obtener_id_grupo(nombre_grupo)
        self.lista_miembros.itemClicked.connect(self.marcar_casilla)

    def marcar_casilla(self, item):
        if item.text().startswith(self.usuario_actual):
            if item.checkState() == QtCore.Qt.Checked: #type: ignore
                self.disponible = False
                item.setIcon(QIcon(self.icono_conexion_inactivo))
                self.hilo.activo = False #type: ignore
                QMessageBox.information(self, "Estado", "Estado inactivo. No recibirás mensajes.")
            else:
                self.disponible = True
                item.setIcon(QIcon(self.icono_conexion_activo))
                self.hilo.activo = True #type: ignore
                if not self.hilo.isRunning(): #type: ignore
                    self.hilo = claseHilo(self.grupo_seleccionado)
                    self.hilo.newValor.connect(self.cargarMensajes)
                    self.hilo.start() #type: ignore
                QMessageBox.information(self, "Estado", "Estado activo. Puedes recibir mensajes.")
        else:
            item.setCheckState(QtCore.Qt.Unchecked) #type: ignore
    
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
        if self.disponible == True:
            try:
                texto_mensaje = str(self.message_line_edit.text())
                if texto_mensaje:
                    CRUD.enviar_mensaje_grupo(self.id_grupo_seleccionado, self.usuario.correo, texto_mensaje)                
                    
                    self.message_line_edit.clear()
            except:
                print(traceback.format_exc())
        else:
            QMessageBox.information(self, "Informacion", "Actualmente te encuentras en estado inactivo, por lo tanto no puedes enviar mensajes.")
            self.message_line_edit.clear()


class claseHilo(QThread):
    newValor = pyqtSignal(tuple)
    def __init__(self, nombreGrupo = None):

        
        self.nombreGrupo = nombreGrupo
        self.activo = True  # Variable para controlar la ejecución del hilo
        super(claseHilo, self).__init__()


    def setGrupo(self, nombreGrupo):
        self.nombreGrupo = nombreGrupo

    def run(self):
        try:
            mensajesLista = []
            mensajesListaTemp = CRUD.obtener_mensajes_grupo(self.nombreGrupo)
            
          
            mensajesLista = mensajesListaTemp
            while self.activo:
                
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
