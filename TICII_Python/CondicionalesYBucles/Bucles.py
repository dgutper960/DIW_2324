## Teoria de bucles

# Bucles while
"""
Los bucles while nos permiten ejecutar una sección de código repetidas
veces. El código se ejecutará mientras una condición determinada se cumpla.
Cuando la condición deje de cumplirse, el bucle terminará y la ejecución del 
programa seguirá de forma normal.
Se llama iteración a una ejecución completa del bloque de código.

1. Representar while con Python
while condicion:
    cuerpo del bucle
 
"""
# Ejemplo 1. Contar hasta 10
numero = 0
while numero<5:
    print(f"{numero}")
    numero = numero + 1


# Ejemplo 2. Numero 0 para salir
numeroParaSalir = 0
numeroIntroducido = None
while numeroIntroducido != numeroParaSalir:
    numeroIntroducido = int(input("Introduzca un numero: "))

print("Saliendo...")

# Ejemplo 3. Bar bonillo
opcion = 1
while opcion != 0:
    print("Bienvenid@ al bar Bonillo. ¿Qué desea?")
    print("1. Bravas muy bravas")
    print("2. Bravas moderadas")
    print("0. Salir")
    opcion = int(input())
    if opcion == 1:
        print("Ha elegido usted unas bravas muy bravas")
    elif opcion == 2:
        print("Ha elegido usted unas bravas moderadas")
    elif opcion == 0:
        print("Ha elegido salir")
    else:
        print("Opcion incorrecta")

print("Hasta la proxima")
    

# Bucles for
"""
El bucle for es un tipo de bucle, parecido al while pero con ciertas diferencias.
La principal es que el número de iteraciones de un for está definido de antemano,
mientras que en un while no. La principal diferencia con respecto al while es la condición.
Mientras que en el while la condición era evaluada en cada iteración para decidir si volver
a ejecutar o no el código, en el for no existe tal condición, sino un iterable que
define las veces que se ejecutará el código

1. Representar for con Python
for variable in elemento iterable (lista, cadena, range, etc.):
    cuerpo del bucle
 
"""
# Ejemplo 1. Rango hasta 10
for i in range(10):
    print(i)
    
# Ejemplo 2. Rango de 3 a 10
for i in range(3, 10):
    print(i)

# Ejemplo 3. Recorrer una cadena (la i se convierte a char)
cadena = "esternocleidomastoideo"
for i in cadena:
    print(i)

# Ejemplo 4. Imprimir numeros pares del 1 al 200
for i in range(0,200):
    if i%2 == 0:
        print(i)
        
for i in range(0, 200, 2):
    print(i)
