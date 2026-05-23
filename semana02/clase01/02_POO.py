class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola me llamo {self.nombre}")


john = Persona("John Doe", 30)
print(john.nombre)
john.saludar()

miguel = Persona("Miguel Doe", 25)
print(miguel.nombre)
print(miguel.edad)
miguel.saludar()


""" Herencia """
class Estudiante(Persona):
    def hablar(self):
        print("Hola amigos, soy un estudiante")

ana = Estudiante("Ana Doe", 20)
print(ana.nombre)
ana.hablar()

class Docente(Persona):
    def hablar(self):
        print("Mucho gusto, soy un docente")

raul = Docente("Raul Doe", 40)
print(raul.nombre)
raul.hablar()
raul.saludar()


""" Encapsulación """
class CuentaBancaria:
    def __init__(self, nombre):
        self.titular = nombre
        self.saldo = 1000
        self.__token = "iw82km3n12bi90s"

    def __validar_operacion(self):
        print("Validando operación")

    def mostrar_token(self):
        print(f"La token es: {self.__token}")

    def usar_metodo_validar_operacion(self):
        self.__validar_operacion()

cuenta = CuentaBancaria("John Doe")
print(f"Titular: {cuenta.titular}")
cuenta.mostrar_token()
cuenta.usar_metodo_validar_operacion()