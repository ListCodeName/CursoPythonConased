# Ejercicio de bucles y condicionales
#
# Escriba un programa que simule un software de una pantalla, en el cual permita:
# * Modificar el brillo de la pantalla
# * Modificar el contraste de la pantalla
# * Modificar el color de la pantalla (RGB) accediendo a cada uno de los colores por separado o bien
#  por medio de una opción pre definida que cambie los tres colores a la vez. Ej: Frío (Más azul), Cálido (Más rojo), Natural (Equilibrado).
# * Mostrar todos los valores actuales por pantalla con un formato amigable.
# * Opción para salir del programa.
#  
# El programa debe imprimir un menú de opciones y permitir al usuario elegir una opción.
# Acceder a una de las opciones como un sub menú, borrando los datos impresos anteriormente.
# Para borrar la consola, podemos utilizar el comando de python `os.system('cls' if os.name == 'nt' else 'clear')`
# import os <--- Importando la librería os para limpiar la consola