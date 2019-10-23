# PYTHON - LISTAS

Paises = ["Colombia","Peru","Chile","Argentina","Venezuela"]
longitud = len(Paises)

#---------------------------------------------
#Recorrer una lista usando la funcion range
print("\nUsando la funcion range: ")
for i in range(longitud):

    print(Paises[i])

#---------------------------------------------
#Recorrer una listta a partir del arreglo mismo
print("\nUsando el mismo arreglo: ")
for i in Paises:

    print(i)
