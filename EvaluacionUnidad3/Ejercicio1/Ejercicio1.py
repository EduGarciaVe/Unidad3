import Funciones_Ejercicio1 as func

"""Genere un programa donde el usuario ingrese un número N y luego llene una lista (arreglo)
con N números definidos por el usuario. Asuma que el usuario siempre ingresará números deferentes
(no ingresará números repetidos)."""
n = func.cant_elem()
lista = func.rellenaLista(n)

"""Recorrido de lista para obtener el tercer numero mayor"""
mayor_3 = func.recorrerLista(lista)

"""Recorrido de lista para obtener el tercer numero mayor aunque modifica lista ordenando la en ascendente"""
alt_may_3 = func.alt_mayor_3(lista)

"""Recorrido de lista y contabilizacion de numeros impares con modal"""
impar = func.impares(lista)

#Recorrer lista, comprobar si el numero esta entre numeros mayores a el, sumar en cantidad si
total_may = func.entre_mayores(lista)

#Imprimir el tercer mayor número en la lista.
print("El numero tercer mayor en la lista es: ",mayor_3)
print("===============================")
print("El numero tercer mayor alternativa que ordena lista en la lista es: ",alt_may_3)
print("===============================")
#Imprimir la cantidad de números impares que posee la lista.
print("La cantidad de numeros impares en la lista es: ",impar)
print("===============================")
#Imprimir la cantidad de números en la lista que cumplen con estar entre dos números mayores a él.
print("La cantidad de numeros que estan entre numeros mayores a el son: ",total_may)

