from typing import Union #se importa para poder usar diferentes tipos de datos.

class Apartamento():
    def __init__(self, metro: int, piso: int, orientacion: str, precio: Union[int, float], vendido: bool):
        
        self.metro = metro # metro: int (metros cuadrados)
        self.piso = piso # piso: int (número de piso)
        self.orientacion = orientacion # orientacion: str ("Norte", "Sur", "Este", "Oeste")
        self.precio = precio # precio: float (precio en moneda)
        self.venddo = vendido   # vendido: bool (True si está vendido, False si no)
        
    def __str__(self):
        return f"Apartamento: {self.metro}m2, piso {self.piso}, {self.orientacion}, ${self.precio}, {'Vendido' if self.venddo else 'No Vendido'}"

    def __repr__(self):
        return f"Apartamento({self.metro}, {self.piso}, '{self.orientacion}', {self.precio}, {self.venddo})"


apartamento_1 = Apartamento(150, 1, "Sur", 1500000.0, False)

print(apartamento_1)  # Imprime usando __str__
print(str(apartamento_1)) # Imprime usando __str__
print([apartamento_1]) # Imprime usando __repr__ porque esta dentro de una lista
print(repr(apartamento_1)) # Imprime usando __repr__

apartamento_2=eval(repr(apartamento_1))#crea un nuevo objeto usando repr
