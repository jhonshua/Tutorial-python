# Lista que puede contener diferentes tipos de datos
mi_lista = [1, "hola", 3.14, True]

# Accediendo a un elemento
print(mi_lista[1])  # Imprime: hola

# Modificando un elemento
mi_lista[0] = 10
print(mi_lista)  # Imprime: [10, 'hola', 3.14, True]

# Agregando un elemento al final
mi_lista.append("nuevo elemento")
print(mi_lista)  # Imprime: [10, 'hola', 3.14, True, 'nuevo elemento']

#--------------------------------------------------------------------------

import array as arr

# Array de enteros
mi_array = arr.array('i', [1, 2, 3, 4])

# Accediendo a un elemento
print(mi_array[2])  # Imprime: 3

# Modificando un elemento
mi_array[0] = 10
print(mi_array)  # Imprime: array('i', [10, 2, 3, 4])

# Intentando agregar un elemento de otro tipo (error)
# mi_array.append("hola")  # Esto generaría un error

