import datetime
import traceback
import mysql.connector
from Python.model.Usuario import Usuario



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
                    print("La contrasena es incorrecta")
            else:
                print('El correo ingresado no esta registrado')
        except:
            traceback.print_exc()
        
        return None
        



      