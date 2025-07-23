import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estilizado con CSS en PyQt6")
        self.setFixedSize(400, 200)
        self.init_ui()
        self.estilizar()

    def init_ui(self):
        # Campo de texto
        self.campo_texto = QLineEdit(self)
        self.campo_texto.setGeometry(50, 50, 200, 30)

        # Botón
        self.boton = QPushButton("Haz clic", self)
        self.boton.setGeometry(270, 50, 80, 30)
        self.boton.clicked.connect(self.on_click)

    def estilizar(self):
        # Estilo para toda la ventana
        self.setStyleSheet("""
            QWidget {
                background-color: #2e3440;   /* Fondo gris oscuro */
            }

            QLineEdit {
                background-color: #eceff4;
                color: #2e3440;
                border: 2px solid #88c0d0;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #5e81ac;
                color: white;
                border: none;
                padding: 5px;
                font-weight: bold;
                border-radius: 4px;
            }

            QPushButton:hover {
                background-color: #81a1c1;
            }

            QPushButton:pressed {
                background-color: #4c566a;
            }
        """)

    def on_click(self):
        texto = self.campo_texto.text()
        self.setWindowTitle(f"Texto ingresado: {texto}")
        print(f"Texto ingresado: {texto}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
