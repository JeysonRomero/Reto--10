def calcular_promedio(arreglo):
    if len(arreglo) == 0:
        raise ValueError("El arreglo no puede estar vacío")
    
    suma = sum(arreglo)
    cantidad = len(arreglo)
    promedio = suma / cantidad
    
    return promedio

# Ejemplo de uso
arreglo = [1.5, 2.5, 3.5, 4.5]
print("El promedio es:", calcular_promedio(arreglo))
