import datetime
import traceback
from random import randint
import smtplib
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario:
    def __init__(self, correo, nombre, apellido, fechaRegistro):

        self.correo:str = correo
        self.nombre:str = nombre
        self.apellido:str = apellido      
        self.fechaRegistro:datetime.datetime = fechaRegistro

        self.descripcion = None

    def setFotoPerfil(self, fotoPerfil):
        self.fotoPerfil = fotoPerfil


    def setContrasenaConHash(self, contrasena):
        self.contrasena:str = contrasena
     
    def setContrasenaSinHash(self, contrasena):#usar si la contraseña no está hasheada
        try:
            self.contrasena:str = generate_password_hash(contrasena, method="scrypt")
        except:
            print("error")



    def setFechaNacimiento(self, fechaTexto:str, separador:str):
        fechaArr = []
        try:
            fechaArr = fechaTexto.split(separador)
            self.fechaNacimiento:datetime.date = datetime.date(int(fechaArr[0]), int(fechaArr[1]), int(fechaArr[2]))
        except:
            print(traceback.format_exc())
            self.fechaNacimiento:datetime.date = datetime.date(int(fechaArr[2]), int(fechaArr[1]), int(fechaArr[0]))

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def mostrar(self):
      
        print(self.correo)
        print(self.nombre)
        print(self.apellido)
        print(self.contrasena)
        print(self.fechaNacimiento)
        print(self.fechaRegistro)
                    
     
        
    @classmethod
    def verificarContrasena(cls, contrasenaSinEncriptar, contrasenaHasheada) -> bool:
        
        return check_password_hash(contrasenaHasheada, contrasenaSinEncriptar)

    @classmethod
    def hashearContrasena(cls, contrasena: str) -> str:
        return generate_password_hash(contrasena, method="scrypt")