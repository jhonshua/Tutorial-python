# Función lambda para sumar dos números
sumar = lambda x, y: x + y

resultado = sumar(3, 5)
print(resultado)  # Imprime 8



numeros = [1, 2, 3, 4, 5]
# Multiplicar cada número por 2 usando una función lambda
resultado = list(map(lambda x: x * 2, numeros))
print(resultado)  # Imprime [2, 4, 6, 8, 10]