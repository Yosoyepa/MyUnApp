
from Python.model.Usuario import Usuario


class MiembroGrupo(Usuario):
    def __init__(self, usuario:Usuario, idGrupo: int, dentroGrupo: bool, creadorGrupo: bool, adminGrupo: bool):
<<<<<<< HEAD
        super().__init__(usuario.contrasena, usuario.nombre, usuario.apellido, usuario.contrasena,
                          usuario.fechaNacimiento, usuario.fechaNacimiento)
=======
        super().__init__(usuario.correo, usuario.nombre, usuario.apellido, usuario.fechaRegistro)
>>>>>>> 7bb247f9785291d4d09b94d9fcde2ac0686e094d
        self.idGrupo: int = idGrupo
        self.dentroGrupo:bool = dentroGrupo
        self.creadorGrupo:bool = creadorGrupo
        self.adminGrupo:bool = adminGrupo
        
    def RevAdmnin(self):
        if self.adminGrupo==False:
            return False
        else:
            return True
        
    def RevDentroGrupo(self):
        if self.dentroGrupo==False:
            return False
        else:
            return True
    