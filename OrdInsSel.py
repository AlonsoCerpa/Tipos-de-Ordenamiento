# Tipos-de-Ordenamiento
# Ejemplos de los diferentes tipos de ordenamiento en Python

def ordIns(lista):
    for i in range (1,len(lista)):
        j = lista[i]
        cont = i - 1
        while j < lista[cont] and cont > -1:
            lista[cont + 1] = lista[cont]
            cont = cont - 1
        lista[cont + 1] = j
    return lista
    
def ordSel(lista):
    for i in range (0,len(lista)-1):
        x = i
        for j in range(i+1,len(lista)):
            if lista[x] > lista[j]:
                x = j 
        if x != i:
            c = lista[i]
            lista[i] = lista[x]
            lista[x] = c
    return lista
