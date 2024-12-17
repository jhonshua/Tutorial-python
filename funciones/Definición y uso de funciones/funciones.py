
#funcion
def saludar(nombre):
    print("Hola,", nombre, "!")

saludar("Juan")  # Llama a la función y pasa el nombre "Juan"


#llamar a uyna funcion
def sumar(a, b):
    resultado = a + b
    return resultado

suma = sumar(3, 5)
print(suma)  # Imprime 8


#Funciones con múltiples parámetros:
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area



# Funciones sin parámetros:
def mostrar_mensaje():
    print("Este es un mensaje.")



# Funciones con parámetros por defecto:
def saludar(nombre="Invitado"):
    print("Hola,", nombre, "!")