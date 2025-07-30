import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import threading

class Client:
    def __init__(self, server_url='http://127.0.0.1:5000'):
        self.server_url = server_url

    def send_request(self, message: str):
        response = requests.post(self.server_url + "/send_request", json={'message': message})
        
        if response.status_code == 200:
            return response.json()['response']
        else:
            return f"Error al enviar la solicitud: {response.status_code}"

class ClientApp(QWidget):
    def __init__(self):
        super().__init__()

        self.client = Client()  # Instanciamos el cliente
        
        # Configurar la ventana principal
        self.setWindowTitle('Cliente PyQt6')
        self.setGeometry(100, 100, 400, 200)

        # Crear los elementos de la interfaz
        self.layout = QVBoxLayout()

        self.text_input = QLineEdit(self)  # Campo de texto para ingresar el mensaje
        self.text_input.setPlaceholderText('Escribe tu mensaje aquí...')

        self.send_button = QPushButton('Enviar', self)  # Botón para enviar el mensaje
        self.send_button.clicked.connect(self.send_message)  # Conectamos el evento de clic

        self.response_label = QLabel('Respuesta: ', self)  # Etiqueta para mostrar la respuesta

        # Añadir los elementos al layout
        self.layout.addWidget(self.text_input)
        self.layout.addWidget(self.send_button)
        self.layout.addWidget(self.response_label)

        self.setLayout(self.layout)

    def send_message(self):
        message = self.text_input.text()  # Obtener el mensaje del campo de texto
        if message:
            response = self.client.send_request(message)  # Enviar el mensaje y obtener la respuesta
            self.response_label.setText(f"Respuesta: {response}")
        else:
            self.response_label.setText("Por favor, ingresa un mensaje.")

def run_client():
    app = QApplication(sys.argv)
    window = ClientApp()
    window.show()
    sys.exit(app.exec())  # Iniciar el ciclo de eventos de PyQt6

if __name__ == "__main__":
    # Solo ejecutamos el cliente en el hilo principal
    run_client()  # Este es el hilo principal donde corre la GUI
