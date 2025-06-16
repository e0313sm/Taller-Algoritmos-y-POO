from Ejercicio_2.cuenta import Cuenta

def main():
    while True:
        print("Bienvenido al sistema bancario.")
        dni_cuenta = input("Ingrese el DNI del cliente: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        interes_anual = float(input("Ingrese el interés anual (%): "))

        cuenta = Cuenta(dni_cuenta, saldo_inicial, interes_anual)

        while True:
            print("\nOpciones:")
            print("1. Mostrar datos de la cuenta")
            print("2. Ingresar dinero")
            print("3. Retirar dinero")
            print("4. Actualizar saldo")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                print(cuenta.mostrar_datos())
            elif opcion == '2':
                cantidad = float(input("Ingrese la cantidad a ingresar: "))
                cuenta.ingresar(cantidad)
            elif opcion == '3':
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
            elif opcion == '4':
                cuenta.actualizar_saldo()
                print("Saldo actualizado.")
            elif opcion == '5':
                print("Saliendo del sistema.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        continuar = input("¿Desea crear otra cuenta? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
