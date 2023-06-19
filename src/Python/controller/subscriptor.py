# import os
# from google.cloud import pubsub_v1

# credentials_path = "src\Python\controller\exalted-summer-387903-263021af32c1.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# usuario = "Juan_Andrade"

# def recibir_mensajes(usuario):
#     # Configurar el cliente de Pub/Sub
#     project_id = 'exalted-summer-387903'
#     subscriber = pubsub_v1.SubscriberClient()
#     # Obtener la suscripción del usuario
#     subscription_name = f'{usuario}_subscription'
#     subscription_path = subscriber.subscription_path(project_id, subscription_name)

#     def callback(message):
#     # # Obtener el remitente del mensaje
#     #     remitente = message.attributes.get('remitente')
#     # # Verificar si el remitente no es el usuario actual
#     #     if remitente != usuario:
#     #     # Procesar el mensaje recibido y mostrarlo en la interfaz de usuario
#     #         print(f"Mensaje recibido para {usuario}: {message.data.decode()}")
#         print(f"Mensaje recibido para {usuario}: {message.data.decode()}")
#     # Aceptar el mensaje para que no se reenvíe
#         message.ack()
#     # Iniciar la escucha de mensajes
#     future = subscriber.subscribe(subscription_path, callback=callback)
#     try:
#         future.result()
#     except KeyboardInterrupt:
#         future.cancel()

# recibir_mensajes(usuario)