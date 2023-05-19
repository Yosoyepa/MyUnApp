import socket, traceback, threading

class Servidor:
    def __init__(self):
        try:
            clientes = []
            hilos = []

            self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketServer.bind(("localhost", 8800))
            self.socketServer.listen(5)
            print('Socket establecido')                            
            hiloConexiones = threading.Thread(name="recibir", target=self.recibirConexiones())            
            hiloConexiones.start()
            hiloMensajes = threading.Thread(name="recibirMensaje", target=self.recibirMensajes())
            hiloMensajes.start()
        except:
            print(traceback.format_exc())

    def recibirConexiones(self):
       
        while True:
            try:
                print('Esperando...')
                self.socketActivo, self.direccion = self.socketServer.accept()
                print(self.direccion[0], "ha entrado")
                
                
            except:
                traceback.format_exc()

    def recibirMensajes(self):
        try:
            while True:
                mensajeCodificado = self.socketActivo.recv(2048)
                mensaje = mensajeCodificado.decode()
                if (mensaje == ''):
                    continue
                print(self.direccion[0], '>', mensaje)
        except:
            print(traceback.format_exc())
srv = Servidor()