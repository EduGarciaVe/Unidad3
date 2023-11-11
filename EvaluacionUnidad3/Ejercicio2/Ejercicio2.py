import funcion as fc

#Una función que reciba un numero “N” como parámetro y que retorne un arreglo (lista) con “N” notas ingresadas por el usuario.
n=int(input("Indique la cantidad de notas a ingresar en sistema --> "))
print("===============================")
#Una función que reciba como parámetro una lista (arreglo) que siempre tendrá elementos numéricos (nunca estará vacía) y
#que retorne el promedio de los elementos de dicha lista.
arreglo = fc.completar_arreglo(n)
print("Los elementos del arreglo son: ",arreglo)
fc.promedio_arreglo(arreglo)
print("===============================")
#Una función que reciba como parámetro una lista (arreglo) que siempre tendrá elementos numéricos (nunca estará vacía)
# y que retorne la cantidad de elementos que posee dicha lista que están por debajo del promedio de todos los elementos
# en dicha lista.
fc.inferior_promedio(arreglo)


