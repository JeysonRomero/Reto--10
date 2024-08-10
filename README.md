# Reto--10

## Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_10 en slack.

### Punto 1 / Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```py
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
```

### Punto 2 / Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

```py
def calcular_producto_punto(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    
    producto_punto = sum(x * y for x, y in zip(arreglo1, arreglo2))
    
    return producto_punto


arreglo1 = [1, 2, 3]
arreglo2 = [4, 5, 6]
print("El producto punto es:", calcular_producto_punto(arreglo1, arreglo2))
```

### Punto 3 / Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```py
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


```
### Punto 4 / Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).

```py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
       
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
       
        if not swapped:
            break
    return arr

# Ejemplo de uso
arreglo = [64, 34, 25, 12, 22, 11, 90]
print("Arreglo ordenado:", bubble_sort(arreglo))


```
