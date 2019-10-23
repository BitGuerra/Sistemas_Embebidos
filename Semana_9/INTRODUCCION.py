
#INTRODUCCION A PYTHON

#Captura de dator en pantalla:
Peso = float(input("Digite su peso: "))
Altura = float(input("Digite su altura: "))
clasificacion = " "

IMC = Peso/Altura**2

#Estrutura de los condicionales.

if( IMC>=0 and IMC <=18.5 ):

    clasificacion = "Bajo de peso"

elif( IMC>18.5 and IMC<=24.9 ):

    clasificacion = "Normal"

elif( IMC>24.9 and IMC<29.9 ):

    clasificacion = "Sobre peso"

elif( IMC>29.9):

    clasificacion = "Obesidad"

#Salida de datos 
print("Su IMC es {} y esta clasificado como: {} ".format(IMC,clasificacion))
