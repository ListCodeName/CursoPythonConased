from flask import Flask, request, jsonify

class Server:
    def __init__(self):
        self.app = Flask(__name__)

        # Ruta para recibir la solicitud POST
        @self.app.route('/send_request', methods=['POST'])
        def handle_request():
            # Obtener los datos enviados por el cliente
            data = request.json
            if 'message' in data:
                response = {"response": f"Mensaje recibido: {data['message']}"}
            else:
                response = {"response": "No se recibió mensaje"}
            return jsonify(response)

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

