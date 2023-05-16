import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario:
    def __init__(self, correo, nombre, apellido, contrasena, fechaNacimiento, fechaRegistro):

        self.correo:str = correo
        self.nombre:str = nombre
        self.apellido:str = apellido
        self.contrasena:str = contrasena
        self.fechaNacimiento:datetime.date = fechaNacimiento
        self.fechaRegistro:datetime.datetime = fechaRegistro
     
    def hashContrasena(self, contrasena):
        try:
            self.contrasena:str = generate_password_hash(contrasena, method="scrypt")
        except:
            print("error")
            
    
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
