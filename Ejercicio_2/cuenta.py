class Cuenta:
    def __init__(self, dni="", saldo=0.0, interes=0.0):
        self.__numero_cuenta = self.__genera_numero_cuenta()
        self.__dni = dni
        self.__saldo = saldo
        self.__interes = interes
        
    def __genera_numero_cuenta(self):
        if not hasattr(Cuenta, '_cuenta_counter'):
            Cuenta._cuenta_counter = 100000  # Inicia el contador de cuentas
        Cuenta._cuenta_counter += 1
        return Cuenta._cuenta_counter

    def actualizar_saldo(self):
        interes_diario = self.__interes / 365
        self.__saldo += self.__saldo * interes_diario

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han ingresado {cantidad:.2f} a la cuenta.")
        else:
            print("La cantidad a ingresar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad:.2f} de la cuenta.")
        else:
            print("No hay suficiente saldo para retirar o la cantidad es inválida.")

    def mostrar_datos(self):
        return (f"Número de cuenta: {self.__numero_cuenta}, "
                f"DNI: {self.__dni}, "
                f"Saldo actual: {self.__saldo:.2f}, "
                f"Interés anual: {self.__interes:.2f}%")
