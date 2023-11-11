
def completar_arreglo(n):
    notas_ingresadas=[]
    for i in range (0,n):
        nota = float(input("Ingrese nota en formato decimal. Ej 7.0 -->"))
        notas_ingresadas.append(nota)

    return notas_ingresadas

def promedio_arreglo(arreglo):
    suma = sum(arreglo)
    largo = len(arreglo)
    promedio = suma / largo
    redondeado = round(promedio,1)


    print(redondeado)

def inferior_promedio(arreglo_2):
    suma_arr2 = sum(arreglo_2)
    largo_arr2 = len(arreglo_2)
    promedio_arr2 = suma_arr2 / largo_arr2
    print("el promedio es", promedio_arr2)
    redondeado_arr2 = round(promedio_arr2,1)
    print("promedio redondeado", redondeado_arr2)
    total_num_min_promedio = 0
    for i in arreglo_2:
        if i < redondeado_arr2:
            total_num_min_promedio = total_num_min_promedio + 1
    print("el total de numeros inferiores al promedio es: ", total_num_min_promedio)
    return total_num_min_promedio

