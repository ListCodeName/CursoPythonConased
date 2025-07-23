#Descarga de la librería PyQT6
"""
Para hacer uso de la librería PyQT6 debemos descargarla a nuestra carpeta de Python instalada en el PC.
pip install PyQT6

Una vez descargadas todas las librerías y dependencias de PyQT estaremos listos para crear nuestras ventanas.

"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
)

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo con QGridLayout")
        self.resize(300, 150)
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Crear widgets
        nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        boton_saludo = QPushButton("Saludar")

        # Posicionar widgets en el grid: (fila, columna)
        layout.addWidget(nombre_label, 0, 0)
        layout.addWidget(self.nombre_input, 0, 1)
        layout.addWidget(boton_saludo, 1, 0, 1, 2)  # ocupa 2 columnas

        # Evento botón
        boton_saludo.clicked.connect(self.saludar)

        self.setLayout(layout)

    def saludar(self):
        nombre = self.nombre_input.text()
        self.setWindowTitle(f"Hola, {nombre}!")
        print(f"Hola, {nombre}!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
