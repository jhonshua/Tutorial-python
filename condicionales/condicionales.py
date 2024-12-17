# Operadores lógicos
edad = 18
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir.")

# Condicionales anidados
numero = 10

if numero > 0:
    if numero % 2 == 0:
        print("El número es positivo y par.")
    else:
        print("El número es positivo e impar.")
else:
    print("El número es negativo.")

# Ejemplo más complejo: calculadora simple
operacion = input("Ingrese la operación (+, -, *, /): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        print("Error: división por cero")
    else:
        resultado = num1 / num2
else:
    print("Operación inválida")

if "resultado" in locals():
    print("El resultado es:", resultado)