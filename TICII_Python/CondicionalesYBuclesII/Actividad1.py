num = 0

# Le preguntamos al usuario por un numero entero positivo
num = int(input("Por favor, introduzca un número entero positivo"))

# Aplicamos la conjetura de Ullmann
while num > 1:
    if num % 2 == 0:
        num = num / 2
        print(str(num)+", ")
    else:
        num = num * 3 + 1
        print(str(num)+", ")
        
print(num)