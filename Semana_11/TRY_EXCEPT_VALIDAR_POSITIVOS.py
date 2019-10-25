
#Algoritmo para validar entradas

'''Este algoritmo captura las edad y
   el año actual para calcular el año
   de nacimiento'''

#Validaciion de la edad(entrada)

while True:
    try:
        edad = int(input("Digite su edad: "))

        if(edad>0):

            break

        else:
            
            print("Dato invalido digite de nuevo ! ! !")

    except ValueError:

        print("Dato invalido digite de nuevo ! ! !")

#Validacion del año actual

while True:
    try:

        year = int(input("Digite el año actual: "))

        if(year>0):
            
            break

        else:

            print("Dato invalido digite de nuevo ! ! !")

    except ValueError:

        print("Dato invalido digite de nuevo ! ! !")

nacimiento = year - edad

print("Su año de nacimiento es: {}".format(nacimiento))
