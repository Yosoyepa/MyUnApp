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



    def setContrasenaConHash(self, contrasena):
        self.contrasena:str = contrasena
     
    def setContrasenaSinHash(self, contrasena):#usar si la contraseña no está hasheada
        try:
            self.contrasena:str = generate_password_hash(contrasena, method="scrypt")
        except:
            print("error")




    def setFechaNacimiento(self, fechaTexto:str, separador:str):
        try:
            fechaArr = fechaTexto.split(separador)
            self.fechaNacimiento:datetime.date = datetime.date(int(fechaArr[0]), int(fechaArr[1]), int(fechaArr[2]))
        except:
            print(traceback.format_exc())
            self.fechaNacimiento:datetime.date = datetime.date(int(fechaArr[2]), int(fechaArr[1]), int(fechaArr[0]))


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
    def Mandar_Codigo(cls, correo):
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

        return Codigo
    