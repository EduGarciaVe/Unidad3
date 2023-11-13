import Funciones_Ejercicio2 as fc

"""Una función que reciba un numero “N” como parámetro y que retorne un arreglo (lista) 
    con “N” notas ingresadas por el usuario."""
n= fc.cant_notas()
notas = fc.lista_notas(n)
print("Las notas de la lista son: ",notas)
print("===============================")

"""Una función que reciba como parámetro una lista (arreglo) que siempre tendrá elementos
    numéricos (nunca estará vacía) y que retorne el promedio de los elementos de dicha lista."""
promedio = fc.promedio_lista(notas)
print ("El promedio de notas ingresadas y rendondeadas es: ",promedio)
print("===============================")

"""Una función que reciba como parámetro una lista (arreglo) que siempre tendrá elementos 
    numéricos (nunca estará vacía) y que retorne la cantidad de elementos que posee dicha 
    lista que están por debajo del promedio de todos los elementos en dicha lista."""
fc.inferior_promedio(notas)


