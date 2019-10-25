#FUNCIONES EN PYTHON
#Se declaran con la estrutura "def"
#Ejemplo para calcular el area y perimetro de un trianguo y un cuadrado.

import math

#****************************************************************
def Triangulo(base, altura):

    Perimetro = base + altura + math.sqrt(base**2+altura**2)
    Area = base*altura/2

    return(Perimetro,Area)

def Cuadrado(lado):

    Perimetro = lado*4
    Area = lado**2

    return(Perimetro,Area)
#****************************************************************

opcion = int(input("Selecione la figura:\n1.Triangulo\n2.Cuadrado\n?:"))

if opcion==1:

    base = float(input("\nDigite la medidad de la base del triangulo: "))
    altura = float(input("Digite la medidad de la altura del triangulo: "))

    [perimetro,area] = Triangulo(base, altura)

elif opcion==2:

    lado = float(input("\nDigite la medidad del lado del cuadrado: "))

    [perimetro,area] = Cuadrado(lado)

print("\nEl perimetro de la figura es: ",perimetro)
print("El area de la figura es: ",area)
