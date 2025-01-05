# Modulo aritmetica

def suma(numeroUno, numeroDos):
    resultado = numeroUno + numeroDos
    return resultado

def resta(numeroUno, numeroDos):
    resultado = numeroUno - numeroDos
    return resultado

def multiplicar(numeroUno, numeroDos):
    resultado = numeroUno * numeroDos
    return resultado

def dividir(numeroUno, numeroDos):
    try:
        resultado = numeroUno / numeroDos
        return resultado
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
