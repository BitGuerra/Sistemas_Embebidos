#FUNCIONES EN PYTHON
#Ejemplo para calcular el area y perimetro de un trianguo y un cuadrado.

import math

#Importa el modulo Figuras para poder acceder a las definiciones
'''Se nombra al modulo Figuras como fig para llamarlo de manera
mas corta dentro del codigo'''

import Figuras as fig


opcion = int(input("Selecione la figura:\n1.Triangulo\n2.Cuadrado\n?:"))

if opcion==1:

    base = float(input("\nDigite la medidad de la base del triangulo: "))
    altura = float(input("Digite la medidad de la altura del triangulo: "))

    [perimetro,area] = fig.Triangulo(base, altura)

elif opcion==2:

    lado = float(input("\nDigite la medidad del lado del cuadrado: "))

    [perimetro,area] = fig.Cuadrado(lado)

print("\nEl perimetro de la figura es: ",perimetro)
print("El area de la figura es: ",area)
