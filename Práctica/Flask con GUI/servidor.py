from flask import Flask, request, jsonify
import os
import signal

app = Flask(__name__)

@app.route('/send_request', methods=['POST'])
def send_request():
    data = request.get_json()
    message = data.get('message', '')

    if message:
        if message == "exit":
            print("Apagando el servidor...")
            os.kill(os.getpid(), signal.SIGINT)  # Enviar señal SIGINT para detener el servidor
            return jsonify({'response': 'Servidor apagado'}), 200
        else:        
            response = f"Mensaje recibido: {message}"
            return jsonify({'response': response}), 200
    else:
        return jsonify({'response': 'No se recibió un mensaje válido.'}), 400

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
