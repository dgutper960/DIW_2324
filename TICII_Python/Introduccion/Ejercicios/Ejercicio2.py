'''
Escribir un programa que pida al usuario su peso (en kg) y 
estatura (en metros), calcule el índice de masa corporal y 
lo almacene en una variable, y muestre por pantalla la frase 
Tu índice de masa corporal es \<imc>, donde \<imc> es el 
índice de masa corporal calculado redondeado con dos decimales.
'''
altura = 0
peso = 0

print('Introduce tu altura en metros')
altura = float(input())

print('Introduce tu peso en kilos')
peso = float(input())

imc = peso / altura**2
print(f'Tu imc es de {round(imc,2)}')