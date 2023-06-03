import os
from google.cloud import pubsub_v1

credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


def recibir_mensajes():
    # Configurar el suscriptor de Pub/Sub
    project_id = 'exalted-summer-387903'
    subscription_name = 'chat_myun-sub'
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message):
        # Procesar el mensaje recibido
        print("Mensaje recibido:", message.data.decode())

        # Aceptar el mensaje para que no se reenvíe
        message.ack()

    # Iniciar la recepción de mensajes
    subscriber.subscribe(subscription_path, callback=callback)

    # Mantener el programa en ejecución
    while True:
        pass

# Iniciar el servidor
recibir_mensajes()
