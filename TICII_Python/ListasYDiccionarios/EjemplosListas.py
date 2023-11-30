# Ejemplo 1 - Declaracion de lista
# Para declarar una lista en Python, se pone el nombre de la lista
# y entre corchetes se añaden los elementos separados por comas
usersRegistered = ["user123", "manuManu", "reshulon6969"]
passwordsRegistered = ["1234", "manuManu", "1234"]

# Para acceder a un elemento, se indica entre corchetes la posición a la que se quiere
# acceder -> las posiciones van de 0 hasta n-1 siendo n el tamaño
print(usersRegistered[0]) # Debería mostrarse "user123"

# Para recorrer una lista, se usa el bucle for, siendo la variable auxiliar
# cada uno de los elementos de la lista
for elemento in usersRegistered:
    print(elemento)
    
# BONUS TRACK
# 
userPorTeclado = "manuManu" # Lo que se introduce por teclado
posicion = 0
for i, user in enumerate(usersRegistered):
    if user == userPorTeclado:
        posicion = i
        print("El usuario es correcto")

passwordPorTeclado = "1234"
if passwordsRegistered[i] == passwordPorTeclado:
    print("Bienvenido a la aplicacion")
    

# Wrapped Diego
