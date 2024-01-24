
# EJERCICIO LOGIN MEJORADO

# Variables para contener el input del usuario
usuarioInput = ""
passwordInput = ""

print("Bienvenid@ a UbriWeb SA")
print("Introduzca sus credenciales...")

usuarioInput = input("user: ")
passwordInput = input("pass: ")

# Una vez pedidas las credenciales, abrimos el fichero
ficheroCredenciales = open("TICII_Python/EjerFicheros/EjercicioLoginMejorado/usuariosRegistrados.txt", "r")

# Una vez abierto el fichero, LEEMOS el fichero
listaUsuariosRegistrados = ficheroCredenciales.readlines()

# En este punto tenemos una lista con todos los usuarios registrados en el sistema
# Debemos recorrer esa lista para comprobar si el usuarioInput y el passwordInput coinciden con 
# alguien del fichero.
elUsuarioExiste = False
for user in listaUsuariosRegistrados:
    # TENEMOS QUE ELIMINAR EL SALTO DE LÍNEA (\n)
    # user = user.strip()
    user = user.replace("\n", "")
    
    # Lo que vamos a hacer es divivir la línea del fichero por su coma
    user_password = user.split(",")

    if usuarioInput == user_password[0] and passwordInput == user_password[1]:
        elUsuarioExiste = True
        
    
# Fuera del for
if elUsuarioExiste == True:
    print("Bienvenid@ "+usuarioInput)
else:
    print("Acceso denegado")

# TENEMOS QUE CERRAR EL FICHERO
ficheroCredenciales.close()
    
    

