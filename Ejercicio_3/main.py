from Ejercicio_3.cafetera import Cafetera


def main():
    cafetera = Cafetera()  # Crear una cafetera con capacidad máxima por defecto

    while True:
        print("\nOpciones:")
        print("1. Llenar cafetera")
        print("2. Servir taza")
        print("3. Vaciar cafetera")
        print("4. Agregar café")
        print("5. Mostrar estado de la cafetera")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cafetera.llenar_cafetera()
        elif opcion == '2':
            cantidad_taza = int(input("Ingrese la cantidad de café para servir (c.c.): "))
            cafetera.servir_taza(cantidad_taza)
        elif opcion == '3':
            cafetera.vaciar_cafetera()
        elif opcion == '4':
            cantidad = int(input("Ingrese la cantidad de café a agregar (c.c.): "))
            cafetera.agregar_cafe(cantidad)
        elif opcion == '5':
            print(cafetera.estado_cafetera())
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
