#Creación de listas:
#Usando corchetes []:

mi_lista = [1, 2, 3, 4, 5]  # Lista de números enteros
otra_lista = ["manzana", "banana", "cereza"]  # Lista de cadenas
lista_mixta = [1, "hola", 3.14, True]  # Lista con diferentes tipos de datos
lista_vacia = []  # Lista vacía
lista_con_duplicados = [1, 2, 2, 3, 3, 3]
    
#---------------------------------------------
#Usando la función list():

lista_desde_tupla = list((1, 2, 3))  # Convierte una tupla a lista
lista_desde_cadena = list("hola")  # Convierte una cadena a lista de caracteres

#---------------------------------------------
#Acceso a los elementos:
#Se accede a los elementos de una lista mediante su índice, utilizando corchetes []:

mi_lista = ["manzana", "banana", "cereza"]
print(mi_lista[0])  # Imprime "manzana" (primer elemento)
print(mi_lista[1])  # Imprime "banana" (segundo elemento)
print(mi_lista[2])  # Imprime "cereza" (tercer elemento)

# Índices negativos: acceden desde el final de la lista
print(mi_lista[-1])  # Imprime "cereza" (último elemento)
print(mi_lista[-2])  # Imprime "banana" (penúltimo elemento)

#---------------------------------------------
#Modificación de listas:
#Asignación directa: Se puede cambiar el valor de un elemento accediendo a su índice

mi_lista = [1, 2, 3]
mi_lista[1] = 10  # Cambia el segundo elemento a 10
print(mi_lista)  # Imprime [1, 10, 3]mi_lista = [1, 2, 3]
mi_lista[1] = 10  # Cambia el segundo elemento a 10
print(mi_lista)  # Imprime [1, 10, 3]


#---------------------------------------------
#append() (agregar al final): Añade un elemento al final de la lista:

mi_lista = [1, 2]
mi_lista.append(3)  # mi_lista ahora es [1, 2, 3]

#---------------------------------------------
#insert() (insertar en una posición): Inserta un elemento en una posición específica:

mi_lista = [1, 3]
mi_lista.insert(1, 2)  # Inserta 2 en la posición 1
print(mi_lista) # Imprime [1, 2, 3]

#---------------------------------------------
#extend() (extender con otra lista): Añade los elementos de otra lista al final de la lista actual:

lista1 = [1, 2]
lista2 = [3, 4]
lista1.extend(lista2)  # lista1 ahora es [1, 2, 3, 4]

#---------------------------------------------
#remove() (eliminar por valor): Elimina la primera aparición de un valor específico:

mi_lista = [1, 2, 3, 2]
mi_lista.remove(2)  # Elimina el primer 2
print(mi_lista) # Imprime [1, 3, 2]

#---------------------------------------------
#pop() (eliminar por índice): Elimina el elemento en una posición específica y lo retorna. Si no se especifica el índice, elimina y retorna el último elemento:


mi_lista = [1, 2, 3]
elemento_eliminado = mi_lista.pop(1)  # Elimina el elemento en la posición 1 (el 2)
print(mi_lista) # Imprime [1, 3]
print(elemento_eliminado) # Imprime 2

ultimo_elemento = mi_lista.pop() # Elimina y retorna el ultimo elemento
print(mi_lista) # Imprime [1]
print(ultimo_elemento) # Imprime 3

#---------------------------------------------
#len() (longitud): Devuelve el número de elementos en la lista:

mi_lista = [1, 2, 3]
print(len(mi_lista))  # Imprime 3

#---------------------------------------------
#sort() (ordenar): Ordena los elementos de la lista en orden ascendente (por defecto). Se puede usar reverse=True para ordenar en orden descendente:

mi_lista = [3, 1, 4, 2]
mi_lista.sort()  # Ordena la lista
print(mi_lista) # Imprime [1, 2, 3, 4]

mi_lista.sort(reverse=True) # Ordena la lista en orden descendente
print(mi_lista) # Imprime [4, 3, 2, 1]

#---------------------------------------------
#index() (índice de un elemento): Devuelve el índice de la primera aparición de un valor específico:

mi_lista = [1, 2, 3, 2]
print(mi_lista.index(2)) # Imprime 1


#---------------------------------------------
#Slicing (rebanado): Permite obtener una porción de la lista:

mi_lista = [0, 1, 2, 3, 4, 5]
print(mi_lista[1:4])  # Imprime [1, 2, 3] (desde el índice 1 hasta el 3, sin incluir el 4)
print(mi_lista[:3])  # Imprime [0, 1, 2] (desde el principio hasta el índice 3, sin incluir el 3)
print(mi_lista[2:])  # Imprime [2, 3, 4, 5] (desde el índice 2 hasta el final)
print(mi_lista[:])  # Imprime toda la lista
print(mi_lista[::2]) # Imprime [0, 2, 4] (desde el principio hasta el final con pasos de 2)

