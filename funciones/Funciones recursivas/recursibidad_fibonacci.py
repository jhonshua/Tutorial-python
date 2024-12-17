def fibonacci(n):
  """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
  if n <= 0:
    print("El número debe ser positivo")
    return -1  # Indicamos un error
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número para calcular su término en la serie de Fibonacci: "))

# Calcular y mostrar el resultado
resultado = fibonacci(numero)
if resultado != -1:
  print("El término", numero, "de la serie de Fibonacci es:", resultado)