## ENUNCIADO EJERCICIO CLASE
Realiza en Python un programa que simule el acceso a un sistema. El programa contará con 
dos ficheros, uno para almacenar los usuarios registrados, y otro para almacenar las sesiones
activas en el sistema.

Usuarios.txt  
usuario:contraseña  

Sesiones.txt  
id_sesion:usuario

El programa dará la bienvenida al sistema y, a continuación, dará las opciones de login, alta o salir.

#### *Opc login*
	Se pregunta por el nombre de usuario  

	Si el sistema detecta que dicho usuario tiene una sesión activa, entonces le permite la entrada sin preguntarle por la contraseña.

	Si el usuario no tiene una sesión activa se le pide la contraseña
	
	Se comprueba si las credenciales son correctas.

	Si son correctas se permite la entrada y acto seguido se da de alta una nueva sesión en el sistema

#### *Opc alta*
	Se pregunta por un nombre de usuario.

	Se pregunta por una contraseña.

	Se comprueba si dichas credenciales existen ya en el sistema.

	Si no existen, se dan de alta, se permite la entrada, y se genera una sesión nueva.