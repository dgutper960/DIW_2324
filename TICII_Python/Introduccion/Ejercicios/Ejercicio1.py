'''
Escribir un programa que pregunte al usuario por el número de 
horas trabajadas y el coste por hora. Después debe mostrar por 
pantalla la paga que le corresponde.
'''
horas_trabajadas = 0
coste_por_hora = 0

print("Dime cuantas horas has trabajado")
horas_trabajadas = int(input())

print("¿A cuanto te pagan la hora?")
coste_por_hora = int(input())

salario = horas_trabajadas * coste_por_hora
print(f'Te corresponden {salario}€')
