import shelve
from juego import juego
class Jugador():
	
	def __init__(self,usuario,password):
		self.usuario=usuario
		self.password=password
		self.numPartidas=0
		self.victorias=0
		self.perdidas=0
		
	#Aumenta en caso de que se haya jugado
	def aumentarPartida(self):
		self.numPartidas+=1
		
	#Función para aumentar las victorias si se gano el juego
	def aumentarVictoria(self):
		self.victorias+=1
	#Función para aumentar los juegos perdidos si se perdió la partida
	def aumentarPerdida(self):
		self.perdidas+=1
		
	#Función que imprime las estadisticas
	def print_estadisticas(self):
		 print("{}\t\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format("Jugador:", jugador.usuario,"No. de partidas:",jugador.numPartidas,"No. de victorias:",jugador.victorias,"No. de perdidas:",jugador.perdidas))
    
    #Función que restablece los datos a cero
	def borrar_historial(self):
		self.victorias=0
		self.perdidas=0
		self.numPartidas=0
		
'''---------------------------MENU-------------------------------------'''
salidaTotal=False
usuarios=[]
#While primer menu
while(True):
	print("------------------------------------")
	print("Bienvenido al Juego")
	print("1) Registrar")
	print("2) Iniciar sesión")

	eleccion=int(input("Escriba el número de la opción elegida  "))
	print("------------------------------------")

	if(eleccion==1):
		print("REGISTRO")
		usuario=str(input("Ingrese su nombre de usuario  "))
		password=str(input("Ingrese su contraseña  "))
		repPass=str(input("Confirme su contraseña  "))
		print("\n")
		users=shelve.open("Users.dat")
		jugador1=Jugador(usuario,password)
		llave=usuario
		if(password!=repPass):
			print("las contraseñas no coinciden")
		elif (llave in users.keys()):
			print ('Usuario creado anteriormente')
		else:
			users[llave]=jugador1
			print ('Usuario agregado')
			users.close()
		
	
			
		
	elif(eleccion==2):
		print("INICIAR SESION")
		usuario=str(input("Ingrese su nombre de usuario  "))
		password=str(input("Ingrese su contraseña  "))
		acceso=False
		users=shelve.open("Users.dat")
		if (usuario in users.keys()):
			jugador=users[usuario]
			if(jugador.password==password):
				acceso=True
		print("\n")
		if(acceso==True):
			print("Acceso permitido")
		else:
			print("Acceso denegado")
	
		if(acceso==True):
			#sub menu dentro del ciclo anterior
			while(True):
				print("------------------------------------")
				print("Bienvenido "+usuario)
				print("Las opciones son: ")
				print("1) Iniciar Partida ")
				print("2) Estadisticas")
				print("3) Borrar Historial ")
				print("4) Salir")
				print("------------------------------------")
				print("\n")
		

				opcion = int(input("Escriba el número de la opción elegida  "))

				if(opcion==1):
					print("¡A jugar!")
					puntuacion=juego()
					jugador.aumentarPartida()
					if(puntuacion==0):
						jugador.aumentarPerdida()
					else:
						jugador.aumentarVictoria()
					
						
					
				elif(opcion==2):
					print("Tu historial es: ")
					jugador.print_estadisticas()
				elif(opcion==3):
					print("Se borro tu historial")
					jugador.borrar_historial()
					jugador.print_estadisticas()
					
				elif(opcion==4):
					print("Hasta la proxima")
					salidaTotal=True
					break
					#salida sub menu, se asigna un booleano para cerrar
					#el primer ciclo
				else:
					print("No es valida la opción")
	else:
		print("La contraseña no coincide con el usuario,acceso denegado")
	
	if(salidaTotal==True):
		users[usuario]=jugador
		users.close()
		break
		#salida primer menu y fin del programa
		

	
	
			
	
