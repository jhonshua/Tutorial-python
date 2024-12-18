
#Creación de conjuntos:
#Usando llaves {}:
mi_conjunto = {1, 2, 3, 4, 5}
conjunto_con_duplicados = {1, 2, 2, 3, 3, 3} # Se convierte a {1, 2, 3}
conjunto_vacio = {} # ¡Ojo! Esto crea un diccionario vacío, no un conjunto vacío.


#---------------------------------------------
#Usando set()
conjunto_vacio = set() # Forma correcta de crear un conjunto vacío

conjunto_desde_lista = set([1, 2, 3, 3, 4]) # Se convierte a {1, 2, 3, 4}
print(conjunto_desde_lista)


conjunto_desde_tupla = set((1, 2, 3)) # Se convierte a {1, 2, 3}
print(conjunto_desde_tupla)

conjunto_desde_cadena = set("hola") # Se convierte a {'h', 'o', 'l', 'a'}
print(conjunto_desde_cadena)

#---------------------------------------------
#Operaciones con conjuntos:
#in (pertenencia): Verifica si un elemento está presente en el conjunto.

mi_conjunto = {1, 2, 3}
print(2 in mi_conjunto)  # True
print(4 in mi_conjunto)  # False

#---------------------------------------------
#add() (agregar): Agrega un elemento al conjunto.

mi_conjunto = {1, 2}
mi_conjunto.add(3) # mi_conjunto ahora es {1, 2, 3}
mi_conjunto.add(2) # No hace nada porque 2 ya existe

#---------------------------------------------
#discard() (descartar): Elimina un elemento del conjunto si existe. No hace nada si el elemento no está presente.

mi_conjunto = {1, 2, 3}
mi_conjunto.discard(2) # mi_conjunto ahora es {1, 3}
mi_conjunto.discard(4) # No hace nada


#---------------------------------------------
#Unión (| o union()): Combina todos los elementos de dos conjuntos.

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2 # {1, 2, 3, 4, 5}
union = conjunto1.union(conjunto2) # {1, 2, 3, 4, 5}

#---------------------------------------------
#Intersección (& o intersection()): Encuentra los elementos comunes a dos conjuntos.
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1 & conjunto2 # {3}
interseccion = conjunto1.intersection(conjunto2) # {3}

#---------------------------------------------
#Diferencia (- o difference()): Encuentra los elementos que están en el primer conjunto pero no en el segundo.

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia = conjunto1 - conjunto2 # {1, 2}
diferencia = conjunto1.difference(conjunto2) # {1, 2}

#---------------------------------------------
#Diferencia simétrica (^ o symmetric_difference()): Encuentra los elementos que están en uno u otro conjunto, pero no en ambos.

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia_simetrica = conjunto1 ^ conjunto2 # {1, 2, 4, 5}
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2) # {1, 2, 4, 5}

