import os
from google.cloud import pubsub_v1

credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

def enviar_mensaje(mensaje):
    # Configurar el cliente de Pub/Sub
    project_id = 'exalted-summer-387903'
    topic_name = 'chat_myun'
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    # Publicar el mensaje en el topic
    future = publisher.publish(topic_path, mensaje.encode())
    future.result()  # Esperar a que se complete la publicación

# Ejemplo de uso
enviar_mensaje("Hola, este es un tercer mensaje desde el cliente")
