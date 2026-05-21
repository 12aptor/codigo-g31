class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola!!! Que tal!")


john = Persona("John Doe", 30)
print(john.nombre)
john.saludar()