def calcular_producto_punto(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    
    producto_punto = sum(x * y for x, y in zip(arreglo1, arreglo2))
    
    return producto_punto


arreglo1 = [1, 2, 3]
arreglo2 = [4, 5, 6]
print("El producto punto es:", calcular_producto_punto(arreglo1, arreglo2))
