"""
Diseñe algoritmo que capture una cantidad de números enteros dados por el 
usuario e imprima los números registrados, cantidad de números impares y 
pares.
"""

cantidad = int(input("\nDigite la cantidad de numeros a registrar: "))

numeros = [0 for i in range(cantidad)]

texto ="\nNumeros registrados: "
pares = 0
impares = 0

for i in range(cantidad):

    numeros[i] = int(input("Digite el numero "+str(i)+":"))
    texto += "{} - ".format(numeros[i])

    if( numeros[i]%2 == 0):

        pares += 1

    else:

        impares += 1

print(texto)
print("Cantidad numeros pares: ",pares)
print("Cantidad numeros impares: ",impares)

