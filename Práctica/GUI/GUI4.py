import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(400, 200, 300, 200)

        # Layout principal
        self.layout = QVBoxLayout()

        # Etiquetas y campos de entrada
        self.usuario_label = QLabel("Usuario:")
        self.usuario_input = QLineEdit()
        
        self.clave_label = QLabel("Contraseña:")
        self.clave_input = QLineEdit()
        self.clave_input.setEchoMode(QLineEdit.EchoMode.Password)  # Mostrar asteriscos en la contraseña

        # Botón de login
        self.login_button = QPushButton("Iniciar sesión")
        self.login_button.clicked.connect(self.validar_login)

        # Añadir widgets al layout
        self.layout.addWidget(self.usuario_label)
        self.layout.addWidget(self.usuario_input)
        self.layout.addWidget(self.clave_label)
        self.layout.addWidget(self.clave_input)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def validar_login(self):
        usuario = self.usuario_input.text()
        clave = self.clave_input.text()

        # Datos correctos (en una aplicación real se validarían con una base de datos)
        if usuario == "admin" and clave == "1234":
            self.abrir_aplicacion_principal()
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos")

    def abrir_aplicacion_principal(self):
        self.close()  # Cerrar la ventana de login
        self.main_window = MainWindow()
        self.main_window.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación Principal")
        self.setGeometry(400, 200, 400, 300)

        # Layout principal de la ventana principal
        layout = QVBoxLayout()

        self.welcome_label = QLabel("¡Bienvenido a la aplicación principal!", self)
        layout.addWidget(self.welcome_label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Crear y mostrar la ventana de login
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())
