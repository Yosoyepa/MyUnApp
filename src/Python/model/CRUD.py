import datetime
from random import randint
import smtplib
import traceback
import mysql.connector
from Python.model.Usuario import Usuario
from PyQt5.QtWidgets import QMessageBox


class CRUD:
    
    def __init__(self):
        self.__hostBD = "34.68.234.58"
        self.__usuarioBD = "root"
        self.__contraseñaBD = 'cm<\PbV#1PN"#k4T'
        self.__dataBase = "myunbd"
        self.__portBD = "3306"
        
        try:
            self.__conexion = mysql.connector.connect(user=self.__usuarioBD, password=self.__contraseñaBD, host=self.__hostBD, database=self.__dataBase, port=self.__portBD)
            self.__cur = self.__conexion.cursor()
        except :
            traceback.print_exc()          
        print("conexion exitosa")          
            
            
    def createUsuario(self, usuario:Usuario):
        query = (f"INSERT INTO USUARIO Values('{usuario.correo}', '{usuario.nombre}', '{usuario.apellido}', '{usuario.contrasena}', '{usuario.fechaNacimiento}', NOW())")
        try:            
            self.__cur.execute(query)
            self.__conexion.commit()
        except :
            traceback.print_exc()
        
        
    def readUsuario(self, correo, contrasena) -> Usuario:
                       
        query = (f"SELECT * FROM USUARIO WHERE CORREO_USUARIO = '{correo}'")
        try:
            self.__cur.execute(query)                
            result = self.__cur.fetchone()
            if(result != None):
                
                if(Usuario.verificarContrasena(contrasena, result[3])):
                    print('inicio de sesion exitoso')
                    user = Usuario(result[0], result[1], result[2], result[5])                    
                    user.setFechaNacimiento(str(result[4]), '-')
                    
                    user.setContrasenaConHash(result[3])
                    return user
                else:
                    self.mostrarCajaDeMensaje("ADVERTENCIA", "La contraseña digitada es incorrecta.", QMessageBox.Critical)
                    
            else:
                self.mostrarCajaDeMensaje("ADVERTENCIA", "El correo ingresado no es de la UNAL o no está registrado.", QMessageBox.Critical)
        except:
            traceback.print_exc()
        
        return None
        
    def cambiarContrasena(self, correo, contrasena):
        try:
            contrasena = Usuario.hashearContrasena(contrasena)
            query = (f"UPDATE USUARIO SET CONTRASENA_USUARIO = '{contrasena}' WHERE CORREO_USUARIO = '{correo}'")
            self.__cur.execute(query)
            self.__conexion.commit()
            self.mostrarCajaDeMensaje("COMPLETADO", "La contraseña ha sido cambiada con exito.", QMessageBox.Information)
        except:
            print(traceback.format_exc())

    def usuarioExiste(self, correo):  
        try:     
            query = f"select CORREO_USUARIO from USUARIO WHERE CORREO_USUARIO= '{correo}'"
            self.__cur.execute(query)
            result = self.__cur.fetchone()
            if result != None:
                return True
            else:
                self.mostrarCajaDeMensaje("ADVERTENCIA", "El correo escrito no está registrado.", QMessageBox.Critical)
        except:            
            print(traceback.format_exc())         

    def mostrarCajaDeMensaje(self,Titulo,Cuerpo, icono):
        msg = QMessageBox()
        msg.setIcon(icono)
        msg.setText(Titulo)
        msg.setInformativeText(Cuerpo)
        msg.setWindowTitle("Error")
        msg.exec_()

    def mandarCodigoVerificacion(self, correo):
        try:
            Codigo = ""
            for i in range(5):
                Codigo += str(randint(0,9))
            print(Codigo)

            message = "Hola, tu codigo es: " + Codigo
            subject = "Envio de Codigo"
            message = 'Subject: {}\n\n{}'.format(subject,message)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            password = "tsmicpleanexdnsm" #contraseña ocultada en env/.env
            server.starttls()
            server.login("myunapp3@gmail.com", password)
            server.sendmail ('myunapp3@gmail.com', correo, message) 
            server.quit()
        except:
            print(traceback.format_exc())

        return Codigo
    
    # def createGrupo(self, nombre, descripcion, usuario):
    #     try:
    #         query = (f"INSERT INTO GRUPO VALUES(NULL, '{nombre}', '{descripcion}', 1, '{usuario.correo}')")
    #         self.__cur.execute(query)
    #         self.__conexion.commit()
    #         print("Grupo creado con exito")
    #     except:
    #         print(traceback.format_exc())

    def obtener_nombres_grupo(self, correo):
        try:    
            query = (f"SELECT G.NOMBRE_GRUPO FROM GRUPO G INNER JOIN MIEMBRO_GRUPO MG ON G.ID_GRUPO = MG.ID_GRUPO WHERE MG.CORREO_USUARIO ='{correo}'")
            self.__cur.execute(query)
            self.Nombres_grupos = self.__cur.fetchall()
            return self.Nombres_grupos
        except:
            print(traceback.format_exc())

    def obtener_miembros_grupos(self, nombre_grupo):
        try:    
            query = (f"SELECT U.NOMBRE_USUARIO, U.APELLIDO_USUARIO FROM USUARIO U INNER JOIN MIEMBRO_GRUPO MG ON U.CORREO_USUARIO = MG.CORREO_USUARIO INNER JOIN GRUPO G ON G.ID_GRUPO = MG.ID_GRUPO WHERE G.NOMBRE_GRUPO ='{nombre_grupo}'")
            self.__cur.execute(query)
            self.Miembros_grupos = self.__cur.fetchall()
            print(self.Miembros_grupos)
            return self.Miembros_grupos
        except:
            print(traceback.format_exc())

    def obtener_mensajes_grupo(self, nombre_grupo):
        try:    
            query = (f"SELECT M.CUERPO_MENSAJE, M.FECHA_MENSAJE, U.NOMBRE_USUARIO, U.APELLIDO_USUARIO FROM MENSAJE M INNER JOIN USUARIO U ON M.CORREO_USUARIO = U.CORREO_USUARIO INNER JOIN GRUPO G ON G.ID_GRUPO = M.ID_GRUPO WHERE G.NOMBRE_GRUPO ='{nombre_grupo}'")
            self.__cur.execute(query)
            self.Mensajes_grupo = self.__cur.fetchall()
            return self.Mensajes_grupo
        except:
            print(traceback.format_exc())

    def enviar_mensaje_grupo(self, id_grupo, correo, mensaje):
        try:
            query = (f"INSERT INTO MENSAJE VALUES(NULL, '{id_grupo}', '{correo}', '{mensaje} , NOW(),')")
            self.__cur.execute(query)
            self.__conexion.commit()
            print("Mensaje enviado con exito")
        except:
            print(traceback.format_exc())

    def obtener_id_grupo(self, nombre_grupo):
        try:
            query = (f"SELECT ID_GRUPO FROM GRUPO WHERE NOMBRE_GRUPO = '{nombre_grupo}'")
            self.__cur.execute(query)
            self.id_grupo = self.__cur.fetchone()
            return self.id_grupo
        except:
            print(traceback.format_exc())

    def obtener_topic_grupo(self, id_grupo):
        try:
            query = (f"SELECT TEMA_GRUPO FROM GRUPO WHERE ID_GRUPO = '{id_grupo}'")
            self.__cur.execute(query)
            self.topic_grupo = self.__cur.fetchone()
            return self.topic_grupo[0]
        except:
            print(traceback.format_exc())