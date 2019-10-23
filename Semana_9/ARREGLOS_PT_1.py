
# PYTHON - LISTAS
# ALGUNAS FUNCIONES

#Formas de declarar una lista:

#Con contenido de un solo tipo
myLista1 = [1,2,3,4]

#Contenidos diferentes en cada indice
myLista2 = [1,"HELLO",3.1416,[1,2,3,4]]

#Lista vacia
myLista3 = []

#Consultar longitud de la lista
longitud = len(myLista1)
print("La longitud de la lista es: {}".format(longitud))

#Agregar contenido a la lista en la ultima posicion
myLista3.append("UTAP")
myLista3.append("2019")
print("La lista #3 es:",myLista3)

#Agregar contenido a la lista en una posicion especifica
#El metodo popo elimina el elemnto ubicado en posicion entre los parentesis
myLista3.pop(1)
print("La lista con el elemento de la posicion 1 eliminado es:",myLista3)

#Imprimir una lista una lista
print("Contenido de la lista: {}".format(myLista2[1]))

#Eliminar elemento de la lista
del myLista2[1]
print("Lista #2 con posicion 1 eliminada",myLista2)




