#Importa el modulo Arduino de la libreria  pyfirmata
from pyfirmata import Arduino
#Importa la libreria de tiempo
from time import sleep

#Objeto de tipo Arduino
tarjeta = Arduino('/dev/ttyACM0')

#Referencia al pin digital 2 como salida
pinLed = tarjeta.get_pin('d:2:o');

try:
	while True:
		#Envia un 1 al pin vinculado a la referencia 'd:2:0'
		pinLed.write(1)
		sleep(0.5)
		#Envia un 0 al pin vinculado a la referencia 'd:2:0'
		pinLed.write(0)
		sleep(0.5)

#Interrupcion por teclado
except KeyboardInterrupt:

	pinLed.write(0)
	tarjeta.exit()
	print("\nSaliendo")

#NOTA: CON ESTE PROTOCOLO JAMAS USAR LOS PINES 0 Y 1
