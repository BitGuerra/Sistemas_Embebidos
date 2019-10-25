"""
Diseñe un algoritmo que permita capturar cinco notas, las guarde en un 
arreglo e imprima con el promedio, además el código deberá preguntar por 
la posición de la nota que desea cambiar, tras realizar el cambio deberá 
imprimir nuevamente el promedio.
"""

notas = [0 for i in range(5)]
texto = "Las notas registradas son:\n"
suma = 0

for i in range(5):

    notas[i] = float(input("Digite la nota #{}: ".format(i)))
    suma += notas[i]
    texto += "{}.Nota: {}  \n".format(i,notas[i])

promedio = suma/5
print(texto)
print("el promedio es: ",promedio)

Pos = int(input("Digite la posicion de la nota a cambiar: "))
nuevaNota = float(input("Digite la nota a cambiar: "))
suma = 0
notas[Pos] = nuevaNota
texto = "\nLas notas registradas son:\n"

for i in range(5):

    suma += notas[i]
    texto += "{}.Nota: {}  \n".format(i,notas[i])

promedio = suma/5
print(texto)
print("el promedio es: ",promedio)
