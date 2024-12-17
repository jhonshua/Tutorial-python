Aunque a primera vista puedan parecer lo mismo, hay algunas diferencias importantes entre listas y arrays en Python.

Listas en Python:

Versatilidad: Son la estructura de datos más versátil en Python. Puedes almacenar cualquier tipo de objeto dentro de una lista: números, cadenas, otras listas, incluso funciones.
Mutable: Puedes modificar una lista después de su creación, agregando, eliminando o cambiando elementos.
Heterogénea: Los elementos de una lista no tienen que ser del mismo tipo. Puedes mezclar enteros, cadenas y otros objetos.
Creación sencilla: Se crean usando corchetes [].
Ejemplo:

Python

mi_lista = [1, "hola", 3.14, True]

Arrays en Python:

Homogeneidad: Los elementos de un array deben ser del mismo tipo de dato (por ejemplo, todos enteros o todos flotantes).
Eficiencia: Los arrays suelen ser más eficientes en términos de memoria y velocidad de acceso que las listas, especialmente cuando se trabaja con grandes cantidades de datos numéricos.
Módulo array: Para utilizar arrays, debes importar el módulo array.
Creación: Se crean especificando el tipo de dato de los elementos y luego los elementos mismos.
Python

import array as arr

mi_array = arr.array('i', [1, 2, 3, 4])  # Array de enteros

¿Cuándo usar listas y cuándo usar arrays?

Listas:

Cuando necesitas una estructura de datos flexible y versátil.
Cuando los elementos de la lista pueden ser de diferentes tipos.
Cuando la eficiencia no es una prioridad absoluta.

Arrays:

Cuando necesitas almacenar grandes cantidades de datos numéricos del mismo tipo.
Cuando la eficiencia es importante, especialmente en cálculos numéricos.
Cuando necesitas realizar operaciones vectoriales o matriciales (en este caso, es más común usar NumPy, que proporciona arrays multidimensionales y muchas funciones matemáticas).
En resumen:

Si bien ambos son estructuras de datos para almacenar colecciones de elementos, las listas son más generales y fáciles de usar, mientras que los arrays son más eficientes para trabajar con datos numéricos homogéneos.