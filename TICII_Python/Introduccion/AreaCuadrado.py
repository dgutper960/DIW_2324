"""
Escribe un programa que calcule el área de un cuadrado 
cuyo lado se introduce por teclado.
"""

# Definir dos variables, una para almacenar el lado, y otra
# para almacenar el area
lado = 0
area = 0

# Mostrar por pantalla un mensaje para el usuario
print("Oye, cuanto mide el lado del cuadrado?")

# Leer por teclado lo que introduzca el user y almacenarlo en lado
lado = int(input())

# Hacer la multiplicacion y almacenarla en area
area = lado * lado 

# Mostrar el area por pantalla
print("El area del cuadrado es "+str(area))