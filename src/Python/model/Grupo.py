class grupo:
    def __init__(self, id, nombre, estado, descripcion):
        self.id:int = id
        self.nombre:str = nombre   
        self.estado:bool = estado ##PARA VER SI EL GRUPO HA SIDO ELIMINADO  O NO 
        self.descripcion:str = descripcion
        
        self.listaMiembros= []
    
        
        