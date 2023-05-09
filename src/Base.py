import datetime

#librerias para PYQT5
from PyQt5 import QtWidgets, uic, QtGui
from Ventana_Ingreso import Ui_Window_Inicio
from Ventana_Registro import Ui_Window_Registro
from Ventana_Menu import Ui_Ventana_Menu
import sys

#Libreria para SQL
import mysql.connector

# libreria para poder mandar un email
import smtplib
from email.message import EmailMessage



#Cargar archivo ui.py
class Entrada(QtWidgets.QMainWindow):
    def __init__(self):
        super(Entrada, self).__init__()
        self.ui = Ui_Window_Inicio()
        self.ui.setupUi(self)

        #Fondo
        self.ui.Label_Imagen.setPixmap(QtGui.QPixmap("resources\Fondo.png"))

class Creacion_Usuario(QtWidgets.QMainWindow):
    def __init__(self):
        super(Creacion_Usuario, self).__init__()
        self.ui = Ui_Window_Registro()
        self.ui.setupUi(self)

        # Fondo
        self.ui.Laber_Imagen.setPixmap(QtGui.QPixmap("resources\Fondo.png"))


class Creacion_Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Creacion_Menu, self).__init__()
        self.ui = Ui_Ventana_Menu()
        self.ui.setupUi(self)

        # Fondo
        self.ui.label_Imagen_Menu.setPixmap(QtGui.QPixmap("resources\Fondo.png"))



#Clase maestra
class Aplicacion(QtWidgets.QMainWindow):
    def __init__(self):
        super(Aplicacion, self).__init__()

        #Creacion repertorio de widgets
        self.Repertorio = QtWidgets.QStackedWidget(self)
        self.Pagina_Entrada = Entrada()
        self.Pagina_Creacion_Usuario = Creacion_Usuario()
        self.Pagina_Menu = Creacion_Menu()
        self.Repertorio.addWidget(self.Pagina_Entrada)
        self.Repertorio.addWidget(self.Pagina_Creacion_Usuario)
        self.Repertorio.addWidget(self.Pagina_Menu)

        #Widget central del repertorio
        self.setCentralWidget(self.Repertorio)
        self.Repertorio.setCurrentWidget(self.Pagina_Entrada)

        #Inicio
        self.Pagina_Entrada.ui.Ingresar.clicked.connect(self.Analisis)
        self.Pagina_Entrada.ui.Boton_Cracion_Usuario.clicked.connect(self.Cambio_A_Creacion_Usuario)
        self.Pagina_Creacion_Usuario.ui.Boton_Registro.clicked.connect(self.Anadir)

        #ConexionBD
        self.Conexion_BD()


    def Conexion_BD(self):
        self.HostBD = "localhost"
        self.UsuarioBD = ""
        self.ContraseñaBD = ""
        self.DataBase = ""
        self.PortBD = "3306"
        self.conexion = mysql.connector.connect(user=self.UsuarioBD,password=self.ContraseñaBD,host=self.HostBD,database=self.DataBase,port=self.PortBD)
        self.cur = self.conexion.cursor()

    def Analisis(self):
        self.Usuario = self.Pagina_Entrada.ui.Line_Usuario.text()
        self.Contraseña = self.Pagina_Entrada.ui.Line_Contrasena.text()
        query = ("SELECT NOMBRE_USUARIO, CONTRASENA_USUARIO FROM USUARIO WHERE NOMBRE_USUARIO = %s AND CONTRASENA_USUARIO = %s")
        self.cur.execute(query, (self.Usuario,self.Contraseña))
        Resultado=self.cur.fetchone()
        if Resultado!=None and self.Usuario == Resultado[0] and self.Contraseña == Resultado[1]:
            self.Cambio_A_Menu()
        else:
            self.Mostrar_MsgError("Error a conectar",'Usuario o contraseña incorrectos')

    def Mostrar_MsgError(self,Titulo,Cuerpo):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(Titulo)
        msg.setInformativeText(Cuerpo)
        msg.setWindowTitle("Error")
        msg.exec_()

    def Anadir(self):
        self.Nombre_Nuevo = self.Pagina_Creacion_Usuario.ui.Line_Nombre.text()
        self.Apellido_Nuevo = self.Pagina_Creacion_Usuario.ui.Line_Apellido.text()
        self.Contraseña_Nueva = self.Pagina_Creacion_Usuario.ui.Line_Contrasena.text()
        self.Correo_Nuevo = self.Pagina_Creacion_Usuario.ui.Line_Email.text()
        self.Fecha_Nacimiento_Nueva = self.Pagina_Creacion_Usuario.ui.Fecha.text()
        self.Fecha_Nacimiento_Nueva = self.Fecha_Nacimiento_Nueva.replace("/","-")
        if self.Nombre_Nuevo == "" or self.Apellido_Nuevo == "" or self.Contraseña_Nueva == "" or self.Correo_Nuevo == "" or self.Fecha_Nacimiento_Nueva == "":
            self.Mostrar_MsgError("Datos incompletos","Por favor diligenciar todos los campos")
        else:
            try:
                query = ("INSERT INTO USUARIO Values(NULL,%s,%s,%s,%s,%s)")
                self.cur.execute(query, (self.Nombre_Nuevo, self.Correo_Nuevo, self.Contraseña_Nueva, self.Fecha_Nacimiento_Nueva, datetime.datetime.now()))
                self.conexion.commit()
                self.Mostrar_MsgError("Registro exitoso", "El usuario a sido creado")
                self.Cambio_A_Inicio()
            except Exception as e:
                print(e)
                self.Mostrar_MsgError("Datos invalidos", "Por favor diligenciar los campos con logica")

    def Cambio_A_Creacion_Usuario(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Creacion_Usuario)

    def Cambio_A_Inicio(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Entrada)

    def Cambio_A_Menu(self):
        self.Repertorio.setCurrentWidget(self.Pagina_Menu)


#Ejecutable
app = QtWidgets.QApplication([])
application = Aplicacion()
application.show()
sys.exit(app.exec())


