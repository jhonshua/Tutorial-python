def es_primo(numero):
    """
    Determina si un número es primo.

    Args:
        numero: El número entero a verificar.

    Returns:
        True si el número es primo, False en caso contrario.
        Devuelve None si la entrada no es un entero positivo.
    """

    if not isinstance(numero, int) or numero <= 0:
        return None  # Manejo de entradas no válidas

    if numero <= 1:
        return False # 0 y 1 no son primos
    
    if numero <= 3:
      return True # 2 y 3 son primos

    if numero % 2 == 0 or numero % 3 == 0:
      return False # divisible entre 2 o 3 no es primo

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i = i + 6
    return True

def main():
    try:
        num_str = input("Ingrese un número entero positivo: ")
        numero = int(num_str)
        resultado = es_primo(numero)

        if resultado is None:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")
        elif resultado:
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")


if __name__ == "__main__":
    main()