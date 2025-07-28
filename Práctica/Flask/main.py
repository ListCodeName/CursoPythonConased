import threading
from servidor import Server
from cliente import Client

def start_server():
    server = Server()
    server.run()

# Iniciar servidor en un hilo
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Crear cliente
client = Client()

# Enviar solicitud al servidor
mensaje = ""
while(mensaje != "exit"):
    mensaje = input("Enviar al Servidor: ")
    client.send_request(mensaje)
