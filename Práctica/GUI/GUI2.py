import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Posicionamiento manual")
        self.setFixedSize(400, 200)  # Tamaño fijo de la ventana
        self.init_ui()

    def init_ui(self):
        # Crear campo de texto
        self.campo_texto = QLineEdit(self)
        self.campo_texto.setGeometry(50, 50, 200, 30)  # x, y, ancho, alto

        # Crear botón
        self.boton = QPushButton("Haz clic", self)
        self.boton.setGeometry(270, 50, 80, 30)  # x, y, ancho, alto

        # Conectar el botón con una función
        self.boton.clicked.connect(self.on_click)

    def on_click(self):
        texto = self.campo_texto.text()
        self.setWindowTitle(f"Texto ingresado: {texto}")
        print(f"Texto ingresado: {texto}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
