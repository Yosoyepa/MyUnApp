import datetime
import os
from random import randint
import smtplib
import traceback
import mysql.connector
from Python.model.Usuario import Usuario
from PyQt5.QtWidgets import QMessageBox
from Python.model.Grupo import grupo
from google.cloud import pubsub_v1
from Python.model.MiembroGrupo import MiembroGrupo
credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


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
        msg.setWindowTitle(Titulo)
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
            password = "svwazwubbdybkswa" #contraseña ocultada en env/.env
            server.starttls()
            server.login("myunapp3@gmail.com", password)
            server.sendmail ('myunapp3@gmail.com', correo, message) 
            server.quit()
            return Codigo
        except:
            print(traceback.format_exc())
            self.mostrarCajaDeMensaje("Error", "No se pudo enviar el correo.", QMessageBox.Critical)
            return None
    
    def createGrupo(self, grupo:grupo, usuario:Usuario):
        query = (f"insert into GRUPO values (null,'{grupo.nombre}',1,'{grupo.descripcion}','esperando topic' )")
        try:            
            self.__cur.execute(query)
            self.__conexion.commit()
            self.creacion_de_topic(grupo)
            miembroTemp = MiembroGrupo(usuario, self.obtener_ultimo_ID_grupo(), True, True, True)
            self.crearMiembroGrupo(miembroTemp)
            self.mostrarCajaDeMensaje("COMPLETADO", "El grupo ha sido creado con exito.", QMessageBox.Information)
        except :
            traceback.print_exc()

    def obtener_nombres_grupo(self, correo):
        try:    
            query = (f"SELECT G.NOMBRE_GRUPO FROM GRUPO G INNER JOIN MIEMBRO_GRUPO MG ON G.ID_GRUPO = MG.ID_GRUPO WHERE MG.CORREO_USUARIO ='{correo}'")
            self.__cur.execute(query)
            self.Nombres_grupos = self.__cur.fetchall()
            return self.Nombres_grupos
        except:
            print(traceback.format_exc())

    def obtener_ultimo_ID_grupo(self):
        try:
            query = (f"SELECT MAX(ID_GRUPO) FROM GRUPO")
            self.__cur.execute(query)
            self.ultima_id_grupos = str(self.__cur.fetchone()[0])
            return self.ultima_id_grupos
        except:
            print(traceback.format_exc())

    def creacion_de_topic(self,grupo: grupo):
        grupo.id = self.obtener_ultimo_ID_grupo()
        project_id = 'exalted-summer-387903'
        nombre_grupo_modificado = f'{grupo.nombre}_{grupo.id}'
        nombre_grupo_modificado = nombre_grupo_modificado.replace(' ','-')
        self.añadir_topic(grupo,nombre_grupo_modificado)
        topic_id = nombre_grupo_modificado
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(project_id,topic_id)
        topic = publisher.create_topic(request={"name":topic_path})
        print(f"created_topic:{topic.name}")

    def añadir_topic(self,grupo:grupo,topic_name):
        query = (f"update GRUPO SET TEMA_GRUPO = '{topic_name}' WHERE ID_GRUPO = {grupo.id}")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

    def crearMiembroGrupo(self,miembro:MiembroGrupo):
        query = (f"INSERT INTO MIEMBRO_GRUPO VALUES({miembro.idGrupo}, '{miembro.correo}', {miembro.dentroGrupo}, {miembro.creadorGrupo}, {miembro.adminGrupo},'TEXTO');")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()


    def admin(self,usuario,nombreGrupo):
        #query = (f"SELECT MG.ADMIN_GRUPO FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO and G.NOMBRE_GRUPO = '{nombreGrupo}' and MG.CORREO_USUARIO = '{usuario}'")
        idTemp = self.sacarID(nombreGrupo)
        query = (f"SELECT ADMIN_GRUPO FROM MIEMBRO_GRUPO WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{usuario}'")
        try:
            self.__cur.execute(query)
            Lista = self.__cur.fetchone()[0]
            if Lista==True:
                return True
            else:
                return False
        except:
            traceback.print_exc()

    def mostrarMiembrosGrupo(self,nombreGrupo):
        query = (f"SELECT MG.CORREO_USUARIO FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO and G.NOMBRE_GRUPO = '{nombreGrupo}'")
        try:
            self.__cur.execute(query)
            Lista = self.__cur.fetchall()
            return Lista
        except:
            traceback.print_exc()

    def mostrarSolicitudes(self,grupoEntrado):
        #query =  (f"SELECT S.CORREO_USUARIO FROM SOLICITUD S INNER JOIN GRUPO G WHERE G.ID_GRUPO = S.ID_GRUPO AND G.NOMBRE_GRUPO='{grupoEntrado}' AND S.SOLICITUD_ACEPTADA=0")
        idTemp = self.sacarID(grupoEntrado)
        query = (f"SELECT CORREO_USUARIO FROM SOLICITUD WHERE ID_GRUPO = '{idTemp}' AND SOLICITUD_ACEPTADA = 0")
        try:
            self.__cur.execute(query)
            Lista = self.__cur.fetchall()
            return Lista
        except:
            traceback.print_exc()

    def removerAdmin(self,correo,grupo):
        #query = (f"UPDATE MIEMBRO_GRUPO MG INNER JOIN GRUPO G SET MG.ADMIN_GRUPO = 0 WHERE MG.ID_GRUPO = G.ID_GRUPO AND MG.CORREO_USUARIO='{correo}' AND G.NOMBRE_GRUPO = '{grupo}'")
        idTemp = self.sacarID(grupo)
        query = (f"UPDATE MIEMBRO_GRUPO SET ADMIN_GRUPO = 0 WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{correo}'")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

    def ascenderAdmin(self,correo,grupo):
        #query = (f"UPDATE MIEMBRO_GRUPO MG INNER JOIN GRUPO G SET MG.ADMIN_GRUPO = 1 WHERE MG.ID_GRUPO = G.ID_GRUPO AND MG.CORREO_USUARIO='{correo}' AND G.NOMBRE_GRUPO = '{grupo}'")
        idTemp = self.sacarID(grupo)
        query = (f"UPDATE MIEMBRO_GRUPO SET ADMIN_GRUPO = 1 WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{correo}'")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

    def eliminarPersona(self,correo,nombreGrupo):
        #query = (f"DELETE FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO AND MG.CORREO_USUARIO='{correo}' AND G.NOMBRE_GRUPO = '{nombreGrupo}'")
        idTemp = self.sacarID(nombreGrupo)
        query = (f"DELETE FROM MIEMBRO_GRUPO WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{correo}'")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()
            
    def buscarSiHayAdmin(self,nombreGrupo):
        conteo = 0
        #query = (f"SELECT MG.ADMIN_GRUPO FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO and G.NOMBRE_GRUPO = '{nombreGrupo}'")
        idTemp = self.sacarID(nombreGrupo)
        query = (f"SELECT ADMIN_GRUPO FROM MIEMBRO_GRUPO WHERE ID_GRUPO = '{idTemp}'")
        try:
            self.__cur.execute(query)
            Lista = self.__cur.fetchall()
            for i in range(len(Lista)):
                if Lista[i][0] == 1:
                    conteo+=1
            return conteo
        except:
            traceback.print_exc()

    def aceptarSolicitud(self,correo,nombreGrupo):
        idTemp = self.sacarID(nombreGrupo)
        query = (f"UPDATE SOLICITUD SET FECHA_HORA_ACEPTACION = now(), SOLICITUD_ACEPTADA = 1 WHERE CORREO_USUARIO = '{correo}' AND ID_GRUPO = '{idTemp}';")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
            query = (f"INSERT INTO MIEMBRO_GRUPO VALUES('{idTemp}','{correo}',1,0,0,'TEXTO')")
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

    def sacarID(self,nombreGrupo):
        query = (f"SELECT ID_GRUPO FROM GRUPO WHERE NOMBRE_GRUPO = '{nombreGrupo}'")
        try:
            self.__cur.execute(query)
            Lista = self.__cur.fetchone()
            return Lista[0]
        except:
            traceback.print_exc()

    def rechazarSolicitud(self,correo,nombreGrupo):
        idTemp = self.sacarID(nombreGrupo)
        query = (f"DELETE FROM SOLICITUD WHERE CORREO_USUARIO = '{correo}' AND ID_GRUPO = '{idTemp}';")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

    def eliminarGrupo(self,nombreGrupo):
        query = (f"DELETE FROM GRUPO WHERE NOMBRE_GRUPO = '{nombreGrupo}'")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

    def cambiarNombreGrupo(self,nombreGrupo,newNombre):
        idTemp = self.sacarID(nombreGrupo)
        query = (f"UPDATE GRUPO SET NOMBRE_GRUPO = '{newNombre}' WHERE ID_GRUPO = '{idTemp}'")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

    def cambiarDescripcionGrupo(self,nombreGrupo,newDescripcion):
        idTemp = self.sacarID(nombreGrupo)
        query = (f"UPDATE GRUPO SET DESCRIPCION_GRUPO = '{str(newDescripcion)}' WHERE ID_GRUPO = '{idTemp}'")
        try:
            self.__cur.execute(query)
            self.__conexion.commit()
        except:
            traceback.print_exc()

