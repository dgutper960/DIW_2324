# Teoria operadores
# Aritméticos
# Relacionales
# Lógicos


# Teoria condicionales
# if normal
# Es una estructura condicional que, si la condición se evalúa a True
# se ejecuta el cuerpo del condicional.
# if [condicion] :
#   [cuerpo del if]
# En PSeInt
# Si [condicion]
#   [cuerpo del if]

tieneDinero = False
tieneBach = True
tieneGS = False

if tieneDinero == True or tieneBach == True or tieneGS == True :
    print("A la universidad niñic@")
    

vaEnChandal = False
estaEbrio = True

if vaEnChandal == False and estaEbrio == False :
    print("Pasa niñic@")


# if else
# Si [condicion]
#   cuerpo Si
# SiNo
#   cuerpo SiNo
if vaEnChandal == False and estaEbrio == False:
    print("Pasas")
else:
    print("No Pasas")

# Ejercicio 1
contrasenia = "1234567890"

print("Dime la contrasenia: ")
contraseniaUsuario = input()

if contraseniaUsuario == contrasenia:
    print("Contrasenia correcta")
else:
    print("Contrasenia incorrecta")