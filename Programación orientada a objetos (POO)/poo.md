La POO es un paradigma de programación que organiza el código en torno a objetos. Estos objetos representan entidades del mundo real o conceptos abstractos, y tienen atributos (características) y métodos (acciones que pueden realizar).

¿Por qué usar POO en Python?

Reutilización de código: Al crear clases, se definen plantillas que pueden ser usadas para crear múltiples objetos con las mismas características y comportamientos.
Organización del código: La POO ayuda a estructurar el código de manera más lógica y fácil de entender, especialmente en proyectos grandes.
Modularidad: Cada objeto se puede desarrollar y probar de forma independiente.
Abstracción: Permite modelar problemas complejos de una manera más sencilla, ocultando la complejidad interna de los objetos.
Conceptos clave en POO:

Clase: Es el plano o plantilla para crear objetos. Define los atributos y métodos que tendrán los objetos de esa clase.
Objeto: Es una instancia de una clase. Tiene sus propios valores para los atributos y puede ejecutar los métodos definidos en la clase.
Atributo: Es una característica o propiedad de un objeto. Por ejemplo, un objeto "Perro" puede tener atributos como "nombre", "raza" y "edad".
Método: Es una función asociada a una clase. Define el comportamiento de los objetos de esa clase. Por ejemplo, un método "ladrar" para un objeto "Perro".

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando!")

# Creamos un objeto de la clase Perro
mi_perro = Perro("Firulais", "Labrador")

# Acceder a un atributo
print(mi_perro.nombre)  # Imprime: Firulais

# Llamar a un método
mi_perro.ladrar()  # Imprime: Firulais está ladrando!

Herencia: Permite crear nuevas clases a partir de clases existentes, heredando sus atributos y métodos.
Polimorfismo: Permite que objetos de diferentes clases respondan de manera diferente al mismo mensaje.
Encapsulamiento: Oculta la implementación interna de un objeto, exponiendo solo una interfaz para interactuar con él.