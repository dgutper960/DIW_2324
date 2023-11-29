cadena_usuario = ""
contador_de_aes = 0

cadena_usuario = input("Por favor, introduzca una palabra: ")

for letra in cadena_usuario:
    if letra == "a":
        contador_de_aes = contador_de_aes + 1

print(f"La cadena {cadena_usuario} tiene {contador_de_aes} aes")