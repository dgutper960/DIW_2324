
## TEORIA ESCRITURA DE FICHEROS
# Para abrir un fichero en modo escritura usamos: open("ruta/del/fichero", "w")
# Para abrir un fichero en modo append usamos: open("ruta/del/fichero", "a")

# Modo escritura elimina lo que había en el fichero y escribe lo nuevo sobre lo antiguo.
# Modo append añade lo nuevo a lo antiguo en el fichero

# ATENCIÓN: SI NO ENCUENTRA EL FICHERO, LO CREA NUEVO

fichero_coches = open("TICII_Python/EjerFicheros/MarcasCoches.txt", "w")

lista_marcas = ["Citroen", "Ford", "Subaru", "Mercedes", "Audi", "BMW"]

for marca in lista_marcas:
    fichero_coches.write(marca+"\n")

fichero_coches.close()

fichero_coches = open("TICII_Python/EjerFicheros/MarcasCoches.txt", "a")

marca_usuario = "1"
while marca_usuario != "0":
    marca_usuario = input("Dime una marca para añadir: (0 para salir)")
    
    if marca_usuario != "0":
        fichero_coches.write(marca_usuario+"\n")

fichero_coches.close()

## UN EJERCICIO PARA DAR DE ALTA A UN USUARIO EN EL SISTEMA
# LOS USUARIOS SE GUARDAN EN UN TXT
# usuario:contraseña

# Da la bienvendia
# Pide un usuario y pide una contraseña
# OBVIAMENTE, hay que comprobar que el usuario no exista ya en el sistema

# CIFRADO CESAR PARA LA CONTRASEÑA Y QUE GUARDE LA CONTRASEÑA CIFRADA EN EL FICHERO
# Cambiar cada letra por el caracter 3 posiciones a la derecha


