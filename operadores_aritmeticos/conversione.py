#Convertir un entero a un decimal

# 1. import decimal:

# ¿Qué hace? Esta línea importa el módulo decimal de Python. Este módulo proporciona una clase Decimal que nos permite realizar operaciones aritméticas de punto flotante con una precisión arbitraria. Esto es especialmente útil cuando necesitamos realizar cálculos exactos con números decimales, ya que la representación de números de punto flotante en computadoras puede ser inexacta en algunos casos.
# 2. numero = 10:

# ¿Qué hace? Se crea una variable llamada numero y se le asigna el valor entero 10.
# 3. print(decimal.Decimal(numero)):

# ¿Qué hace?
# decimal.Decimal(numero): Esta expresión crea un objeto Decimal a partir del valor entero 10. Es decir, convierte el número entero en un número decimal con precisión arbitraria.
# print(): Imprime el valor del objeto Decimal en la consola. En este caso, se imprimirá 10.0.
# 4. print(type(decimal.Decimal(numero))):

# ¿Qué hace?
# type(): Esta función devuelve el tipo de dato de un objeto.
# print() imprime el tipo de dato del objeto Decimal. En este caso, se imprimirá algo como <class 'decimal.Decimal'>.

import decimal

numero = 10
print(decimal.Decimal(numero))
print(type(decimal.Decimal(numero)))


string = '123456'
print(decimal.Decimal(string))