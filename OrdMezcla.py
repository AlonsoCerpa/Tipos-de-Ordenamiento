#Ordenamiento por mezcla   
def mezcla(left,right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i = i + 1
        else:
            res.append(right[j])
            j = j + 1
    while i < len(left):
        res.append(left[i])
        i = i + 1
    while j < len(right):
        res.append(right[j])
        j = j + 1
    return res

def OrdenxMezcla(lista):
    if len(lista) < 2:
        return lista
    mitad = 1 + len(lista)//2
    left = OrdenxMezcla(lista[:mitad-1])
    right = OrdenxMezcla(lista[mitad+1:])
    return mezcla(left,right)
