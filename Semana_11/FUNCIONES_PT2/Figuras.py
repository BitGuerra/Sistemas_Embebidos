# Este es un modulo 
# Contiene funciones y variables que pueden ser llamadas desde un script

#Definicion para calcular el perimetro y area de un triangulo
def Triangulo(base, altura):

    Perimetro = base + altura + math.sqrt(base**2+altura**2)
    Area = base*altura/2

    return(Perimetro,Area)

#Definicion para calcular el perimetro y area de un cuadrado
def Cuadrado(lado):

    Perimetro = lado*4
    Area = lado**2

    return(Perimetro,Area)
