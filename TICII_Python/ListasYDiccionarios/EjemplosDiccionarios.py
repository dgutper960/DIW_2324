# Definición de diccionario
divisas = {"Euro": "€", "Dolar": "$", "Bitcoin": "BTC", "Dogecoin": "DOGE"}

"""
Escribir un programa que guarde en una variable el 
diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario 
por una divisa y muestre su símbolo o un mensaje de aviso si la divisa 
no está en el diccionario.
"""

# Manera 1
print("Dime la divisa que quieras comprobar: ")
divisaUsuario = input()

if divisas.get(divisaUsuario) == None:
    print("La divisa no se encuentra en el diccionario")
    respuesta = input("¿le gustaria incluir esa divisa en el diccionario?")
    if respuesta == "Si" or respuesta == "s":
        simbolo = input("Indique el simbolo de la divisa")
        divisas[divisaUsuario] = simbolo
else: 
    print(f'El simbolo de la divisa indicada es: {divisas[divisaUsuario]}')

# Imprimir por pantalla el diccionario entero (Clave y Valor)
# Debemos recorrer el diccionario (MIRANDO LA PIZARRA)
for clave in divisas:
    print(clave+": "+divisas[clave])


