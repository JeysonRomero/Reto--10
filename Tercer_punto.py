def mover_ceros_al_final(arreglo):
    j = 0 
    for i in range(len(arreglo)):
        if arreglo[i] != 0:
            arreglo[j] = arreglo[i]
            j += 1

    
    for k in range(j, len(arreglo)):
        arreglo[k] = 0

    return arreglo


arreglo = [0, 1, 0, 3, 12]
print("Arreglo después de mover ceros al final:", mover_ceros_al_final(arreglo))
