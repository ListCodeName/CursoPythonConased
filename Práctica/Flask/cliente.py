import requests

class Client:
    def __init__(self, server_url='http://127.0.0.1:5000'):
        self.server_url = server_url

    def send_request(self, message: str):
        # Enviar un mensaje al servidor
        response = requests.post(self.server_url + "/send_request", json={'message': message})
        
        if response.status_code == 200:
            print(f"Respuesta del servidor: {response.json()['response']}")
        else:
            print(f"Error al enviar la solicitud: {response.status_code}")
