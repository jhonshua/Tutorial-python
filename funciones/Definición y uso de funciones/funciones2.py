def saludar(nombre):
    print ("Hola",  nombre)
    
    
saludar("Marko")

#-------------------------------------------------------------

#PESO kg / altura2

def calcularIMC(peso, altura):
    imc = peso  / (altura**2)
    return imc

print(calcularIMC(80, 1.80))

#-------------------------------------------------------------
#son metodos nativos de python que nos permiten buscvar el min y el max de una lista 

def CalcularMaxMin(lista):
    return max(lista), min(lista)

valMax, valMin = CalcularMaxMin([5,6,8,23,9,10,1,56])

print(valMax, valMin)

