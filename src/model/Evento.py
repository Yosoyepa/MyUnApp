import datetime

class Evento:
    def __init__(self):
        self.idEvento                   ##
        self.idGrupo                    ##
        self.correoUsuario:str          ##DATOS PARA VERIFICAR EL CREADOR DEL EVENTO
        self.nombreEvento:str
        self.fechaHoraEvento:datetime.datetime
        self.aprobado:bool
        
        