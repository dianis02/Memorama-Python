# Proyecto1-Python-
Creación de un memora con persistencia de los usuarios

Ejecutar con:
Python3

Mi proyecto esta compuesto por 2 archivos.py , registro.py y juego.py
Para probarlo basta ejecutar el archivo registro.py


JUEGO.PY
En este archivo cree  el tablero como una lista de listas e hice una
función para imprimir este.
Cree 2 tableros, uno con "O" que son las fichas volteadas, este es el 
tablero que ve el usuario, y otro tablero con elementos unicode
Para revolver los elementos de unicode den el tablero, use shuffle en la
lista de elementos unicode y despues los fui agregando fila por fila en el
tablero.
Después hice una función llamada juego.
Esta solicita las coordenadas para elegir las 2 fichas necesarias,
al escogerlas puede caer en condicionales en caso de que no sean validas 
las coordenadas, que sea la misma carta, que ya se haya descubierto esa
carta. Luego las condicionales siguientes es para determinar si las fichas 
son iguales o no. Las coordenadas dadas se utilizan en el tablero con los
elementos unicode, pero unas vez que se eligen cartas validas , se cambian 
los elementos del tablero del usuario por los elemenos de unicode.
si son iguales los simbolos, estas ya no se cambian, por el otro lado
se mostraran los simbolos y luego se volveran a cambiar por "O".
Se rompe el ciclo cuando ambos tableros son iguales (Ganaste) o cuando un 
contador llega a 3 que son el número de intentos admitidos.
La función regresa 1 en caso de ganar o 0 en caso de perder

REGISTRO.PY
Primero hice la clase Jugador, la cual tiene de atributos strings usuario
,contraseña e integers num de partidas, victorias y perdidas.
Hice los metodos para aumentar los atributos mencionados anteriormente,
además de uno para volver a poner en ceros los atibutos e imprimir estos.

Luego sigue el menu, el cual se divide en 2 partes, el primer menu para 
registrarse e iniciar sesión y el siguiente menu se abre despues de 
iniciar sesión. En el segundo menu podemos ver las estadisticas, jugar,
borrar el historial y salir.
En el primer menu, cuando se registra utilizo shelve para almacenar al 
jugador. Utilizo de llave el usuario y si ya existe la llave es que ya se
creo un usuario con ese nombre.
Luego para iniciar sesión si la llave es existe, comparamos la contraseña 
del jugador con la que ingresan y si es igual se permite el acceso.
Luego en el segundo menu hacemos uso de las función juego que importamos
de juego.py, y dependiendo el resultado se aumenta el atributo correspondiente
del jugador. 
Para romper ambos ciclos del menu, cuando la opción es igual a salir, 
rompemos el primer ciclo y utilizamos un booleano para entrar a una condicional
y romper el otro ciclo y finalizar el programa.



usuarios ya creados:
usuario:Diana------password:0210
usuario:Isabel-----password:021097
usuario:Nelly------password:0611
