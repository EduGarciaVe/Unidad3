"""Funcion para OBTENER CANTIDAD DE ELEMENTO A INGRESAR EN LISTA"""
def cant_elem ():
    cant = int(input("Ingrese la cantidad de elementos que va a ingresar --> "))
    return cant

"""Funcion para RELLENAR LISTA EN BASE A LA CANTIDAD DE ELEMENTOS ANTERIORMENTE INGRESADOS"""
def rellenaLista (n):
    lista = []
    for i in range(0, n):
        fl = int(input("Ingrese numero entero --> "))
        lista.append(fl)
    print(lista)
    print("===============================")
    return lista

"""Funcion para RECORRER LISTA Y OBTENER EL TERCER NUMERO MAYOR"""
def recorrerLista(lista):
    max_if1 = 0
    max_if2 = 0
    max_if3 = 0
    for num in lista:
        if num > max_if3 and num > max_if2 and num > max_if1 and max_if1 == 0:
            max_if1 = num
        elif num > max_if3 and num > max_if2 and num > max_if1 and max_if1 != 0:
            if max_if2 == 0:
                max_if2 = max_if1
            elif max_if2 != 0:
                max_if3 = max_if2
                max_if2 = max_if1
            max_if1 = num
        elif num > max_if3 and num > max_if2 and num < max_if1:

            max_if3 = max_if2
            max_if2 = num
        elif num > max_if3 and num < max_if2:

            max_if3 = num
    return max_if3

"""Funcion ALTERNATIVA para RECORRER LISTA Y OBTENER EL TERCER NUMERO MAYOR, SOLO QUE AQUI SE MODIFICA LA LISTA ORDENANDOLA EN ASCENDENTE"""
def alt_mayor_3 (lista):
    orden = sorted(lista)
    may_3 = 0
    for i in range(0,len(orden)-1):
        may_3 = i
    return may_3

"""Funcion para ENCONTRAR LA CANTIDAD DE NUMEROS IMPARES PRESENTES EN LA LISTA"""
def impares(lista):
    cant_impar = 0
    for i in lista:
        if i % 2 != 0:
            cant_impar = cant_impar + 1

    return cant_impar

"""Funcion para ENCONTRAR CANTIDAD DE NUMEROS QUE ESTAN ENTRE NUMEROS MAYORES A EL, adicionalmente MUESTRA CUAL ES EL NUMERO DESTACADO Y LOS NUMERO QUE LO RODEAN"""
def entre_mayores(lista):
    largo_lista = len(lista)
    total_bt_may = 0
    for i in range(0, largo_lista -1):
        if lista[i - 1] > lista[i] and lista[i + 1] > lista[i]:
            total_bt_may = total_bt_may + 1
            print(lista[i] ,"es menor a ",lista[i - 1]," y a ",lista[i + 1])
    return total_bt_may
