def factorial(n):
  """Calcula el factorial de un número de forma recursiva."""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Obtener el número del usuario
numero = int(input("Ingrese un número para calcular su factorial: "))

# Calcular y mostrar el factorial
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)