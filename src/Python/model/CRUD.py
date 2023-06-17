import datetime
import os
from random import randint
import smtplib
import traceback
import mysql.connector
from Python.model.Usuario import Usuario
from PyQt5.QtWidgets import QMessageBox
from Python.model.Grupo import grupo
import Levenshtein

from Python.model.MiembroGrupo import MiembroGrupo
credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json" #type: ignore
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

                 

            
def createUsuario(usuario:Usuario):
    query = (f"INSERT INTO USUARIO Values('{usuario.correo}', '{usuario.nombre}', '{usuario.apellido}', '{usuario.contrasena}', '{usuario.fechaNacimiento}', NOW())")
    try: 
        con = Conexion()        
        con.cur.execute(query)
        con.conexion.commit()
        del	con
    except :
        traceback.print_exc()
    
    
def readUsuario(correo, contrasena):
    con = None
    query = (f"SELECT * FROM USUARIO WHERE CORREO_USUARIO = '{correo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        result = con.cur.fetchone()
        del con
        if(result != None):
            
            if(Usuario.verificarContrasena(contrasena, result[3])):
                print('inicio de sesion exitoso')
                user = Usuario(result[0], result[1], result[2], result[5])                    
                user.setFechaNacimiento(str(result[4]), '-')
                
                user.setContrasenaConHash(result[3])
                return user
            else:
                mostrarCajaDeMensaje("ADVERTENCIA", "La contraseña digitada es incorrecta.", QMessageBox.Critical) # type: ignore
                
        else:
            mostrarCajaDeMensaje("ADVERTENCIA", "El correo ingresado no es de la UNAL o no está registrado.", QMessageBox.Critical)
    except:
        traceback.print_exc()
    
    if(con != None): # type: ignore
        del con # type: ignore
    return None
    
    
def cambiarContrasena(correo, contrasena):
    con = None
    try:
        con = Conexion()
        contrasena = Usuario.hashearContrasena(contrasena)
        query = (f"UPDATE USUARIO SET CONTRASENA_USUARIO = '{contrasena}' WHERE CORREO_USUARIO = '{correo}'")
        con.cur.execute(query)
        con.conexion.commit()
        mostrarCajaDeMensaje("COMPLETADO", "La contraseña ha sido cambiada con exito.", QMessageBox.Information)
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con


def obtener_nombres_grupo_especifico(nombre_grupo):
    con = None
    resultados = []

    try:
        con = Conexion()

        # Obtener todos los nombres de grupo
        query = "SELECT NOMBRE_GRUPO FROM GRUPO"
        con.cur.execute(query)
        nombres_grupo = con.cur.fetchall()

        # Calcular la similitud utilizando Levenshtein Distance y ordenar los resultados
        for nombre in nombres_grupo:
            similitud = Levenshtein.distance(str(nombre_grupo), str(nombre[0]))  # Calcula la distancia de Levenshtein
            resultados.append((nombre[0], similitud))

        resultados.sort(key=lambda x: x[1])  # Ordena los resultados por similitud (distancia de Levenshtein)

        resultados = resultados[:3]  # Obtiene los primeros 3 resultados

    except:
        traceback.print_exc()

    if con:
        del con

    return resultados


def usuarioExiste(correo):  
    con = None
    try:
        con = Conexion()     
        query = f"select CORREO_USUARIO from USUARIO WHERE CORREO_USUARIO= '{correo}'"
        con.cur.execute(query)	
        
        result = con.cur.fetchone()
        if result != None:
            return True
        else:
            mostrarCajaDeMensaje("ADVERTENCIA", "El correo escrito no está registrado.", QMessageBox.Critical)
    except:            
        print(traceback.format_exc())         
    finally:
        if(con != None):
            del con

def mostrarCajaDeMensaje(Titulo,Cuerpo, icono):
    msg = QMessageBox()
    msg.setIcon(icono)
    msg.setText(Titulo)
    msg.setInformativeText(Cuerpo)
    msg.setWindowTitle(Titulo)
    msg.exec_()

def mandarCodigoVerificacion(correo):
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
        mostrarCajaDeMensaje("Error", "No se pudo enviar el correo.", QMessageBox.Critical)
        return None
def Obtener_nombre_usario_por_correo(correo):
    con = None
    try:
        con = Conexion()
        query = (f"SELECT CONCAT(NOMBRE_USUARIO, ' ', APELLIDO_USUARIO) AS NOMBRE_COMPLETO FROM USUARIO WHERE CORREO_USUARIO ='{correo}'")
        con.cur.execute(query)
        result = con.cur.fetchall()
        return result[0][0]
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

def createGrupo(grupo:grupo, usuario:Usuario):
    con = None
    query = (f"insert into GRUPO values (null,'{grupo.nombre}',1,'{grupo.descripcion}','esperando topic' )")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()               
        #self.creacion_de_topic(grupo)
        miembroTemp = MiembroGrupo(usuario, obtener_ultimo_ID_grupo(), True, True, True) # type: ignore
        crearMiembroGrupo(miembroTemp)
        mostrarCajaDeMensaje("COMPLETADO", "El grupo ha sido creado con exito.", QMessageBox.Information)
    except :
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def obtener_nombres_grupo(correo): # type: ignore
    con = None
    query = (f"SELECT G.NOMBRE_GRUPO FROM GRUPO G INNER JOIN MIEMBRO_GRUPO MG ON G.ID_GRUPO = MG.ID_GRUPO WHERE MG.CORREO_USUARIO ='{correo}'")
    try:    
        con = Conexion()
        con.cur.execute(query)        
        result = con.cur.fetchall()
        
        return result
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

def obtener_ultimo_ID_grupo():
    con = None
    query = (f"SELECT MAX(ID_GRUPO) FROM GRUPO")
    try:
        con = Conexion()
        con.cur.execute(query)
        
        ultima_id_grupos = int(con.cur.fetchone()[0]) # type: ignore
        return ultima_id_grupos
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

'''
def creacion_de_topic(self,grupo: grupo):
    grupo.id = self.obtener_ultimo_ID_grupo() # type: ignore
    project_id = 'exalted-summer-387903'
    nombre_grupo_modificado = f'{grupo.nombre}_{grupo.id}'
    nombre_grupo_modificado = nombre_grupo_modificado.replace(' ','-')
    self.añadir_topic(grupo,nombre_grupo_modificado)
    topic_id = nombre_grupo_modificado
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id,topic_id)
    topic = publisher.create_topic(request={"name":topic_path})
    print(f"created_topic:{topic.name}")
'''
    
def añadir_topic(grupo:grupo,topic_name):
    con = None
    query = (f"update GRUPO SET TEMA_GRUPO = '{topic_name}' WHERE ID_GRUPO = {grupo.id}")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def obtener_nombres_todoslosgrupos():
    con = None
    query = (f"select nombre_grupo from GRUPO")
    try:    
        con = Conexion()
        con.cur.execute(query)                
        Nombres_todosgrupos = con.cur.fetchall()
        return Nombres_todosgrupos
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

def Enviar_sol(usuario: Usuario, id_grupo):
    con = None
    query = (f"insert into SOLICITUD values(null,'{usuario.correo}','{id_grupo}', NOW() ,null,0)") 
    try:            
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
        mostrarCajaDeMensaje("COMPLETADO", "La solicitud ha sido enviada.", QMessageBox.Information)
    except :
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def obtener_id(nombre_grupo):
    con = None
    query = (f"SELECT ID_GRUPO FROM GRUPO WHERE NOMBRE_GRUPO = '{nombre_grupo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        return self.__cur.fetchone()[0] # type: ignore
    except:
        print(traceback.format_exc())
        return None
    finally:
        if(con != None):
            del con

def crearMiembroGrupo(miembro:MiembroGrupo):
    con = None
    query = (f"INSERT INTO MIEMBRO_GRUPO VALUES({miembro.idGrupo}, '{miembro.correo}', {miembro.dentroGrupo}, {miembro.creadorGrupo}, {miembro.adminGrupo},'TEXTO');")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()


def admin(usuario,nombreGrupo):
    con = None
    #query = (f"SELECT MG.ADMIN_GRUPO FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO and G.NOMBRE_GRUPO = '{nombreGrupo}' and MG.CORREO_USUARIO = '{usuario}'")
    idTemp = sacarID(nombreGrupo)
    query = (f"SELECT ADMIN_GRUPO FROM MIEMBRO_GRUPO WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{usuario}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        Lista = con.cur.fetchone()[0] # type: ignore
        if Lista==True:
            return True
        else:
            return False
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def mostrarMiembrosGrupo(nombreGrupo):
    con = None
    query = (f"SELECT MG.CORREO_USUARIO FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO and G.NOMBRE_GRUPO = '{nombreGrupo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        Lista = con.cur.fetchall()
        return Lista
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def mostrarSolicitudes(grupoEntrado):
    con = None
    #query =  (f"SELECT S.CORREO_USUARIO FROM SOLICITUD S INNER JOIN GRUPO G WHERE G.ID_GRUPO = S.ID_GRUPO AND G.NOMBRE_GRUPO='{grupoEntrado}' AND S.SOLICITUD_ACEPTADA=0")
    idTemp = sacarID(grupoEntrado)
    query = (f"SELECT CORREO_USUARIO FROM SOLICITUD WHERE ID_GRUPO = '{idTemp}' AND SOLICITUD_ACEPTADA = 0")
    try:
        con = Conexion()
        con.cur.execute(query)
        Lista = con.cur.fetchall()
        return Lista
    except:
        traceback.print_exc()

def removerAdmin(correo,grupo):
    con = None
    #query = (f"UPDATE MIEMBRO_GRUPO MG INNER JOIN GRUPO G SET MG.ADMIN_GRUPO = 0 WHERE MG.ID_GRUPO = G.ID_GRUPO AND MG.CORREO_USUARIO='{correo}' AND G.NOMBRE_GRUPO = '{grupo}'")
    idTemp = sacarID(grupo)
    query = (f"UPDATE MIEMBRO_GRUPO SET ADMIN_GRUPO = 0 WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{correo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def ascenderAdmin(correo,grupo):
    con = None
    #query = (f"UPDATE MIEMBRO_GRUPO MG INNER JOIN GRUPO G SET MG.ADMIN_GRUPO = 1 WHERE MG.ID_GRUPO = G.ID_GRUPO AND MG.CORREO_USUARIO='{correo}' AND G.NOMBRE_GRUPO = '{grupo}'")
    idTemp = sacarID(grupo)
    query = (f"UPDATE MIEMBRO_GRUPO SET ADMIN_GRUPO = 1 WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{correo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def eliminarPersona(correo,nombreGrupo):
    con = None
    #query = (f"DELETE FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO AND MG.CORREO_USUARIO='{correo}' AND G.NOMBRE_GRUPO = '{nombreGrupo}'")
    idTemp = sacarID(nombreGrupo)
    query = (f"DELETE FROM MIEMBRO_GRUPO WHERE ID_GRUPO = '{idTemp}' AND CORREO_USUARIO = '{correo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def buscarSiHayAdmin(nombreGrupo):
    con = None
    conteo = 0
    #query = (f"SELECT MG.ADMIN_GRUPO FROM MIEMBRO_GRUPO MG INNER JOIN GRUPO G WHERE MG.ID_GRUPO = G.ID_GRUPO and G.NOMBRE_GRUPO = '{nombreGrupo}'")
    idTemp = sacarID(nombreGrupo)
    query = (f"SELECT ADMIN_GRUPO FROM MIEMBRO_GRUPO WHERE ID_GRUPO = '{idTemp}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        Lista = con.cur.fetchall()
        for i in range(len(Lista)):
            if Lista[i][0] == 1:
                conteo+=1
        return conteo
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def aceptarSolicitud(correo,nombreGrupo):
    con = None
    idTemp = sacarID(nombreGrupo)
    query = (f"UPDATE SOLICITUD SET FECHA_HORA_ACEPTACION = now(), SOLICITUD_ACEPTADA = 1 WHERE CORREO_USUARIO = '{correo}' AND ID_GRUPO = '{idTemp}';")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
        query = (f"INSERT INTO MIEMBRO_GRUPO VALUES('{idTemp}','{correo}',1,0,0,'TEXTO')")
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def sacarID(nombreGrupo):
    con = None
    query = (f"SELECT ID_GRUPO FROM GRUPO WHERE NOMBRE_GRUPO = '{nombreGrupo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        Lista = con.cur.fetchone()
        return Lista[0] #type: ignore
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def rechazarSolicitud(correo,nombreGrupo):
    con = None
    idTemp = sacarID(nombreGrupo)
    query = (f"DELETE FROM SOLICITUD WHERE CORREO_USUARIO = '{correo}' AND ID_GRUPO = '{idTemp}';")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def eliminarGrupo(nombreGrupo):
    con = None
    query = (f"DELETE FROM GRUPO WHERE NOMBRE_GRUPO = '{nombreGrupo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con

def cambiarNombreGrupo(nombreGrupo,newNombre):
    con = None
    idTemp = sacarID(nombreGrupo)
    query = (f"UPDATE GRUPO SET NOMBRE_GRUPO = '{newNombre}' WHERE ID_GRUPO = '{idTemp}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con            

def cambiarDescripcionGrupo(nombreGrupo,newDescripcion):
    con = None
    idTemp = sacarID(nombreGrupo)
    query = (f"UPDATE GRUPO SET DESCRIPCION_GRUPO = '{str(newDescripcion)}' WHERE ID_GRUPO = '{idTemp}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()
    except:
        traceback.print_exc()
    finally:
        if(con != None):
            del con



# def createGrupo(self, nombre, descripcion, usuario):
#     try:
#         query = (f"INSERT INTO GRUPO VALUES(NULL, '{nombre}', '{descripcion}', 1, '{usuario.correo}')")
#         self.__cur.execute(query)
#         self.__conexion.commit()
#         print("Grupo creado con exito")
#     except:
#         print(traceback.format_exc())

def obtener_nombres_grupo(correo):
    con = None
    query = (f"SELECT G.NOMBRE_GRUPO FROM GRUPO G INNER JOIN MIEMBRO_GRUPO MG ON G.ID_GRUPO = MG.ID_GRUPO WHERE MG.CORREO_USUARIO ='{correo}'")
    try:    
        con = Conexion()
        
        con.cur.execute(query)
        Nombres_grupos = con.cur.fetchall()
        return Nombres_grupos
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

def obtener_miembros_grupos(nombre_grupo):
    con = None
    query = (f"SELECT U.NOMBRE_USUARIO, U.APELLIDO_USUARIO FROM USUARIO U INNER JOIN MIEMBRO_GRUPO MG ON U.CORREO_USUARIO = MG.CORREO_USUARIO INNER JOIN GRUPO G ON G.ID_GRUPO = MG.ID_GRUPO WHERE G.NOMBRE_GRUPO ='{nombre_grupo}'")
    try:    
        con = Conexion()
        con.cur = con.conexion.cursor()
        
        con.cur.execute(query)
        Miembros_grupos = con.cur.fetchall()
        print(Miembros_grupos)
        con.cur.close()
        con.conexion.close()
        return Miembros_grupos
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

def obtener_mensajes_grupo(nombre_grupo):
    con = None
    query = (f"SELECT M.ID_MENSAJE ,M.ID_GRUPO, U.CORREO_USUARIO , M.TEXTO_MENSAJE, U.NOMBRE_USUARIO, U.APELLIDO_USUARIO, M.FECHA_HORA_MENSAJE FROM MENSAJE M INNER JOIN USUARIO U ON M.CORREO_USUARIO = U.CORREO_USUARIO INNER JOIN GRUPO G ON G.ID_GRUPO = M.ID_GRUPO WHERE G.NOMBRE_GRUPO ='{nombre_grupo}' order by M.ID_MENSAJE")
    try:    
        con = Conexion()                
        con.cur.execute(query)            
        Mensajes_grupo = con.cur.fetchall()            
        return Mensajes_grupo        
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

def enviar_mensaje_grupo(id_grupo, correo, mensaje):
    con = None
    query = (f"INSERT INTO MENSAJE VALUES(NULL, {id_grupo}, '{correo}', '{mensaje}' , NOW())")
    try:                    
        con = Conexion()
        con.cur.execute(query)
        con.conexion.commit()        
        print("Mensaje enviado con exito")        
    except:
        print(traceback.format_exc())
    finally:	
        if(con != None):
            del con

def obtener_id_grupo(nombre_grupo):
    con = None
    query = (f"SELECT ID_GRUPO FROM GRUPO WHERE NOMBRE_GRUPO = '{nombre_grupo}'")
    try:        
        con = Conexion()
        con.cur.execute(query)                
        id_grupo = con.cur.fetchone()[0] #type: ignore        
        return id_grupo
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con

def obtener_topic_grupo(id_grupo):
    con = None
    query = (f"SELECT TEMA_GRUPO FROM GRUPO WHERE ID_GRUPO = '{id_grupo}'")
    try:
        con = Conexion()
        con.cur.execute(query)
        topic_grupo = con.cur.fetchone()[0] #type: ignore
        return topic_grupo
    except:
        print(traceback.format_exc())
    finally:
        if(con != None):
            del con    

class Conexion:
    
    def __init__(self):
        self.__hostBD = "34.68.234.58"
        self.__usuarioBD = "root"
        self.__contraseñaBD = 'cm<\PbV#1PN"#k4T' #type: ignore
        self.__dataBase = "myunbd"
        self.__portBD = "3306"
        
        try:
            self.conexion = mysql.connector.connect(user=self.__usuarioBD, password=self.__contraseñaBD, host=self.__hostBD, database=self.__dataBase, port=self.__portBD)
            self.cur = self.conexion.cursor()
        except :
            traceback.print_exc()          
        print("conexion exitosa")  

    def __del__(self):
        self.cur.close()
        self.conexion.close()
        print("conexion cerrada")