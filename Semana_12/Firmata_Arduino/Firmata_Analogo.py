from pyfirmata import Arduino,util

# Crea un objeto de tipo Arduino especificando el puerto de conexion
tarjeta = Arduino('/dev/ttyACM0')

#Inicia el iterador para evitar el overflow en el puerto serial
it = util.Iterator(tarjeta)
it.start()

#Crea un referencia para leer el pin analogo A0
analogo_0 = tarjeta.get_pin('a:0:i')


try:
	while True:

		print("Cana analogo A0: ",analogo_0.read())

except KeyboardInterrupt:

	tarjeta.exit()
	print("\nSaliendo.....")
