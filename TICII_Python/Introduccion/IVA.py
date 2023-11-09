# Hacer un programa que dado un precio introducido por teclado
# que aplique el iva a dicho producto y muestre el resultado por
# pantalla

precio = 0
iva = 1.21

print("Por favor, introduzca el precio del producto ")
precio = int(input()) # El valor que tomará precio será lo que introduzcamos por teclado

precio_con_iva = precio * iva # El operador para multiplicar es -> *

print("El precio con iva es: "+str(precio_con_iva))

# COSAS A TENER EN CUENTA
# input() -> Lee por teclado y almacena una cadena de caracteres
# str() -> Cambia el tipo de dato a cadena de caracteres
# int() -> Cambia el tipo de dato a numérico entero
# * -> para multiplicar
# + -> para sumar o concatenar
