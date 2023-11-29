## Ejercicios de bucles + condicionales

### Actividad 1

Implementa un algoritmo en el que dado un entero n > 1 leído por teclado, calcule e imprima los elementos correspondientes a la Conjetura de Ullman (en honor al matemático S. Ullman). La conjetura consiste en lo siguiente:
• Empieza con cualquier entero positivo.
• Si es par, se divide entre 2; si es impar se multiplica por 3 se agrega 1.
• Se itera hasta obtener el número 1. while num > 1

## Actividad 2

Declara una variable con nombre **palabra_magica** y dale el valor que tú quieras.
Realiza un programa que muestre el mensaje "No has dicho la palabra mágica" de forma indefinida hasta que el usuario introduzca la palabra_magica de forma correcta.

## Actividad 3

Realiza un programa que *itere* sobre un string que el usuario introducirá por teclado y que cuente el número de vocales **a** que el string tiene.
Por ejemplo:
usuario introduce: "esternocleidomastoideo"
programa muestra: "esternocleidomastoideo contiene 1 a"

### Actividad 4

Realiza un programa que pida números por teclado al usuario de forma indefinida y que realice la suma de los números pares introducidos y de los números impares introducidos. Cuando se introduce un número negativo el programa debe mostrar la suma de los pares y la suma de los impares.

### Actividad 5

Vamos a simular el login de un usuario dentro de una aplicación para una cafetería. **CoffeeShop Ubrique**
Declara 2 variables llamadas usuarioRegistrado y contraseniaRegistrada que tengan como objetivo almacenar los datos del único usuario registrado dentro de tu aplicación.
Seguidamente, simula un login a una aplicación, donde un usuario deba introducir correctamente su usuario y contraseña. En el caso de que alguno de los datos sean incorrectos, se debe imprimir un mensaje por pantalla que lo indique. El programa deberá seguir pidiendo el usuario y la contraseña hasta que ambos datos sean correctos.
Una vez el usuario introduzca las credenciales de forma correcta, el programa mostrará las opciones disponibles, que son:

1. Café (1€)
2. Té verde (1.5€)
3. Tostada con aceite y tomate (2€)
4. Space cake (4€)
0. Salir

El usuario podrá seleccionar productos de manera **indefinida**, y, según lo que el usuario seleccione, el programa deberá mostrar un mensaje adecuado.
"Ha seleccionado un café"
"Ha seleccionado una space cake"