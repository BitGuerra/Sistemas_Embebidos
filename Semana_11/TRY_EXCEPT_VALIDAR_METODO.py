
#Algoritmo para validar entradas

'''Este algoritmo captura las edad y
   el año actual para calcular el año
   de nacimiento'''

#Metodo para validad enteros positivos

def validaEntero(texto):

    while True:
        try:

            var = int(input(texto))

            if(var > 0):

                return var

            else:

                print("Dato invalido digite de nuevo ! ! !")

        except ValueError:

            print("Dato invalido digite de nuevo ! ! !")

            

#Inicio del algoritmo

edad = validaEntero("Digite su edad: ")

year =  validaEntero("El año actual: ")

nacimiento = year - edad

print("Su año de nacimiento es: {}".format(nacimiento))
