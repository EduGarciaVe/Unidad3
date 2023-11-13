"""Funcion para INDICAR LA CANTIDAD DE NOTAS A INGRESAR"""
def cant_notas():
    n = int(input("Indique la cantidad de notas a ingresar en sistema --> "))
    return n

"""Funcion para RELLENAR LISTA DE NOTAS SEGUN LA CANTIDAD INGRESADA ANTERIORMENTE POR EL USUARIO"""
def lista_notas(n):
    notas_ingresadas=[]
    for i in range (0,n):
        nota = float(input("Ingrese nota en formato decimal. Ej 7.0 -->"))
        notas_ingresadas.append(nota)

    return notas_ingresadas

"""Funcion para CALCULAR EL PROMEDIO DE NOTAS"""
def promedio_lista(notas):
    suma = sum(notas)
    largo = len(notas)
    promedio = suma / largo
    #REDONDEA SOLO A 1 DECIMAL
    redondeado = round(promedio,1)
    return redondeado

"""Funcion para CONTAR LA CANTIDAD DE NOTAS QUE SE ENCUENTRAN POR DEBAJO DEL 
    PROMEDIO CALCULADO EN LA LISTA"""
def inferior_promedio(notas):
    suma_notas = sum(notas)
    cantidad_notas = len(notas)
    promedio_notas = suma_notas / cantidad_notas
    #REDONDEA PROMEDIO DE NOTAS A SOLO 1 DECIMAL
    redondeado_notas = round(promedio_notas,1)
    notas_bajo_promedio = 0
    for i in notas:
        if i < redondeado_notas:
            notas_bajo_promedio = notas_bajo_promedio + 1
    print("el total de notas inferiores al promedio es: ", notas_bajo_promedio)
    return notas_bajo_promedio

