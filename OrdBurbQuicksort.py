def ordBurbuja(lista):
    a = len(lista)
    b = True
    while b:
        b = False
        for i in range(0,a - 1):
            if lista[i] > lista[i+1]:
                x = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = x
                b = True
        a = a - 1
    return lista

def particion(sublista,primero,ultimo):
    indexPivote = primero
    valorPivote = sublista[indexPivote]
    temp = sublista[indexPivote]
    sublista[indexPivote] = sublista[ultimo]
    sublista[ultimo] = temp
    index = primero
    for i in range(primero, ultimo):
        if sublista[i] < valorPivote:
            temp1 = sublista[i]
            sublista[i] = sublista[index]
            sublista[index] = temp1
            index = index + 1
    temp2 = sublista[index]
    sublista[index] = sublista[ultimo]
    sublista[ultimo] = temp2
    return index

def quickSort(lista,inicio,fin):
    if inicio < fin:
        p = particion(lista,inicio,fin)
        quickSort(lista,inicio,p-1)
        quickSort(lista,p+1,fin)
