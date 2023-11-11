"""Genere un programa donde el usuario ingrese un número N y luego llene una lista (arreglo)
con N números definidos por el usuario. Asuma que el usuario siempre ingresará números deferentes
(no ingresará números repetidos)."""
n = int(input("Ingrese la cantidad de elementos que va a ingresar --> "))
lista = []
for i in range(0, n):
    fl = int(input("Ingrese numero entero --> "))
    lista.append(fl)
print(lista)

#Recorrido de lista para obtener el tercer numero mayor
max_3 = 0
max_if1 = 0
max_if2 = 0
max_if3 = 0
for num in lista:
    if num > max_if3 and num > max_if2 and num > max_if1:
        max_if1 = num
    elif num > max_if3 and num > max_if2 and num < max_if1:
        max_if3 = max_if2
        max_if2 = num
    elif num > max_if3 and num < max_if2:
        max_if3 = num

    max_3 = max_if3

#Recorrido de lista y contabilizacion de numeros impares con modal
cant_impar =0
for i in lista:
    if i%2 != 0:
        cant_impar = cant_impar+1

#Recorrer lista, comprobar si el numero esta entre numeros mayores a el, sumar en cantidad si
total_bt_may = 0
for i in range(1,len(lista)-1):
    if lista[i-1] > lista [i] and lista[i+1] > lista[i]:
        total_bt_may = total_bt_may+1


#Imprimir el tercer mayor número en la lista.
print("El numero tercer mayor en la lista es: ",max_3)

#Imprimir la cantidad de números impares que posee la lista.
print("La cantidad de numeros impares en la lista es: ",cant_impar)

#Imprimir la cantidad de números en la lista que cumplen con estar entre dos números mayores a él.
print("La cantidad de numeros que estan entre numeros mayores a el son: ",total_bt_may)

