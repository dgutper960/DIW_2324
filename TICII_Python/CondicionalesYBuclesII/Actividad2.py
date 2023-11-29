palabra_magica = "illo"
palabra_usuario = ""

# Bucle para repetir un mensaje de manera indefinida
while palabra_usuario != palabra_magica:
    palabra_usuario = input("Introduzca la contraseña: ")
    
    # If para mostrar un mensaje si no se introduce la palabra correcta
    if palabra_usuario != palabra_magica:
        print("No has dicho la palabra magica")
        
print("Bienvenid@ al sistema")