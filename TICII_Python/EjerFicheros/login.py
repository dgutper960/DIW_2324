
print("Bienvenido")
user = input("¿Como te llamas?")

# Abrimos el archivo
file_users = open('TICII_Python/EjerFicheros/usersRegistered.txt', 'r')
# Leemos las filas
lista_usuarios = file_users.readlines()

# Una vez las líneas leídas, recorremos la lista_usuarios para comprobar
# que el user está registrado
for user_registered in lista_usuarios:
    
    user_registered = user_registered.strip()
    
    # Comprobamos
    if user_registered == user:
        print("Estas registrado y eres bienvenid@")
        
print(lista_usuarios)

file_users.close()
