"""Crear una aplicación que simule ser un cajero automático,
del cual se pueda retirar y depositar dinero, además debe
ser posible ver el saldo."""

import os
import subprocess

class ATM:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount):
        try:
            float_amount = self.string_to_float(amount)

            if float_amount == None:
                raise ValueError("Monto incorrecto, intente nuevamente")
            
            if float_amount <= 0:
                raise ValueError("El monto a retirar debe ser mayor a 0")

            if float_amount > self.balance:
                raise Exception("Saldo insuficiente, intente con un monto menor")
            
            self.balance -= float_amount
            print("Monto retirado exitosamente")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def deposit(self, amount):
        try:
            float_amount = self.string_to_float(amount)

            if float_amount == None:
                raise ValueError("Monto incorrecto, intente nuevamente")
            
            if float_amount <= 0:
                raise ValueError("El monto a retirar debe ser mayor a 0")
            
            self.balance += float_amount
            print("Monto depositado exitosamente")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def show_balance(self):
        print(f"El saldo es: {self.balance}")

    def string_to_float(self, value):
        try:
            return float(value)
        except:
            return None

class App:
    def __init__(self, atm):
        self.atm = atm

    def show_menu(self):
        self.clear()
        print("==========================================")
        print("        🏦 BIENVENIDO AL CAJERO ATM        ")
        print(f"        Cliente: {self.atm.holder}      ")
        print("==========================================")
        print("  [1] 💸 Retirar dinero")
        print("  [2] 💰 Depositar dinero")
        print("  [3] 🗒️ Ver saldo")
        print("  [4] ❌ Salir")
        print("==========================================")


    def pause(self):
        print()
        input("Presione enter para continuar...")

    def clear(self):
        comando = "cls" if os.name == "nt" else "clear"
        subprocess.run(comando, shell=True)

def main():
    atm = ATM("John Doe", 1000)
    app = App(atm)

    while True:
        app.show_menu()
        option = input("Elegir opción: ")
        print()

        match option:
            case "1":
                amount = input("Ingrese el monto a retirar: ")
                atm.withdraw(amount)
                app.pause()
            case "2":
                amount = input("Ingrese el monto a depositar: ")
                atm.deposit(amount)
                app.pause()
            case "3":
                atm.show_balance()
                app.pause()
            case "4":
                app.clear()
                print("==========================================")
                print("    🖐️ Gracias por usar nuestro cajero    ")
                print("         ¡Que tenga un buen día!           ")
                print("==========================================")
                break
            case _:
                print("⚠️ Opción incorrecta, intente nuevamente...")
                app.pause()

if __name__ == '__main__':
    main()

