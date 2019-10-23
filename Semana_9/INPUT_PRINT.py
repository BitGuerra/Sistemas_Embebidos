#CAPTURAR INFORMACION POR TECLADO

#Capturar un entero
Dato1 = int(input("Digite un numero entero: "))

#Capturar un dato de tipo real
Dato2 = float(input("Digite un numero de tipo real: "))

#Capturar un dato de tipo cadena
Dato3 = input("Digite una cadena: ")

#IMPRECION EN PANTALLA

'''A continuacion se precsentan diversas formas
 de imprimir informacion en pantalla'''

#1
print("Este es un entero: "+str(Dato1)+", Este es un numero real: "+str(Dato2))

#2
print("Este es un entero:",Dato1,",Este es un numero real:",Dato2)

#3
print("Este es un entero: {},Este es un numero real:{}".format(Dato1,Dato2))
