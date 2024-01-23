"""
Teoria de lectura de archivos

Para abrir un archivo se usa el método open("ruta del archivo", "r -> read")
"""
# Para abrir un archivo se usa el método open("ruta del archivo", "r -> read")
archivo_marcas = open('TICII_Python\EjerFicheros\MarcasCoches.txt', 'r')

print(archivo_marcas)

# readLines() lee todas las líneas del archivo
lista_marcas = archivo_marcas.readlines()

print(lista_marcas)

#Recorrer toda la lista
for marca in lista_marcas:
    print(marca)


# Cerramos el archivo
archivo_marcas.close()
