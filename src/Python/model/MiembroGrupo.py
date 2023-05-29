
from Python.model.Usuario import Usuario


class MiembroGrupo(Usuario):
    def __init__(self, usuario:Usuario, idGrupo: int, dentroGrupo: bool, creadorGrupo: bool, adminGrupo: bool):
        super().__init__(usuario.contrasena, usuario.nombre, usuario.apellido, usuario.contrasena, usuario.fechaNacimiento, usuario.fechaNacimiento)
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
    