import random

def mergesort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Ordenamiento recursivo de las mitades
        mergesort(izquierda)
        mergesort(derecha)

        # Mezcla de las mitades ordenadas
        i = j = k = 0

        # Copiar datos a las listas temporales izquierda[] y derecha[]
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Comprobación de elementos restantes
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
lista = random.sample(range(1, 10000000), 150)
mergesort(lista)
print("Lista ordenada:", lista)