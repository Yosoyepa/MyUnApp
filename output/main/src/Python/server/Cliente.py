import traceback, threading
import socket

class Cliente:
    def __init__(self):
        try:
            self.socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket establecido")
            self.socketCliente.connect(('localhost', 8800))
            print("Socket conectado")
            hiloMensajes = threading.Thread(name = 'enviarMensajes', target=self.enviar())
            hiloMensajes.start()
        except:
            print(traceback.format_exc())

    def enviar(self):
        usuario = 'XD'#input("Escribe tu usuario: ")
        while True:
            try:                
                mensaje = f"{usuario} > " + input(f"{usuario} > ")
                enviar = bytes(mensaje, "UTF-8")
                self.socketCliente.send(enviar)
            except:
                print(traceback.format_exc())
clt = Cliente()