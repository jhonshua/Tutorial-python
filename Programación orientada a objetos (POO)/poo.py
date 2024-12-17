# Importamos la clase Animal desde poo2.py
from poo2 import Animal

class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamamos al constructor de la clase padre para inicializar el atributo nombre
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def maullar(self):
        print(f"{self.nombre} está maullando.")