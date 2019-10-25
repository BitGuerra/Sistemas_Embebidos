"""
Diseñe un algoritmo que capture una cantidad de nombres dada
por el usuario, luego el algoritmo debe permitir buscar un
nombre e imprimir si este se encuentra registrado entre los
nombres dados al inicio.
"""
cantidad = int(input("Digite la cantidad de nombres a registrar: "))
nombres = [" " for i in range(cantidad)]

for i in range(cantidad):

    nombres[i] = input("Digite el nombre #{}: ".format(i))


buscar = input("Digite el nombre a buscar: ")

if buscar in nombres:

    print("El nombre {} se encuentra en la lista".format(buscar))

else:

    print("El nombre {} no se encuentra en la lista".format(buscar))
