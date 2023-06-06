import os
from google.pubsub_v1 import PubsubMessage
from google.cloud import pubsub_v1


from Python.model.CRUD import CRUD


credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

crd = CRUD()

id_grupo = 8
mensaje = 'WAZAAAAAAAAAAAAA'

usuario = "Juan_Andrade"

def crear_suscripcion(usuario,topic_name):
    # Configurar el cliente de Pub/Sub
    project_id = 'exalted-summer-387903'
    subscriber = pubsub_v1.SubscriberClient()
    topic_name = crd.obtener_topic_grupo(topic_name)

    # Crear el nombre de la suscripción
    subscription_name = f'{usuario}_subscription'

     #Crear la suscripción
    topic_path = f'projects/{project_id}/topics/{topic_name}'
    subscription_path = f'projects/{project_id}/subscriptions/{subscription_name}'


    subscription = pubsub_v1.Subscription(name=subscription_path, topic=topic_path)
    subscriber.create_subscription(request=subscription)

def enviar_mensaje(topic_name,mensaje):
    # Configurar el cliente de Pub/Sub
    project_id = 'exalted-summer-387903'
    publisher = pubsub_v1.PublisherClient()
    topic_name = crd.obtener_topic_grupo(topic_name)
    # Obtener el topic del chat grupal
    topic_path = f'projects/{project_id}/topics/{topic_name}'
    # Publicar el mensaje en el topic del chat grupal
    future = publisher.publish(topic_path,mensaje.encode())
    future.result()



##crear_suscripcion(usuario,id_grupo)

enviar_mensaje(id_grupo,mensaje)
