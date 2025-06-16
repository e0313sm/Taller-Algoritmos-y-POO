from Ejercicio_1.persona import Persona

def main():
    while True:
        # Solicitar datos de la persona
        documento = input("Ingrese el documento: ")
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        sexo = input("Ingrese el sexo (M/F): ")
        peso = float(input("Ingrese el peso (kg): "))
        altura = float(input("Ingrese la altura (cm): "))

        # Crear objetos de la clase Persona
        persona1 = Persona(documento, nombre, edad, sexo, peso, altura)
        persona2 = Persona(documento, nombre, edad, sexo)  # Sin peso y altura
        persona3 = Persona()  # Por defecto
        persona3.set_documento(documento)
        persona3.set_nombre(nombre)
        persona3.set_edad(edad)
        persona3.set_sexo(sexo)
        persona3.set_peso(peso)
        persona3.set_altura(altura)

        # Comprobar IMC y mostrar mensaje
        for persona in [persona1, persona2, persona3]:
            imc_resultado = persona.calcular_imc()
            imc_categoria = {
                -1: "Por debajo del peso",
                0: "Normal",
                1: "Con sobrepeso",
                2: "Obesidad",
                3: "Obesidad extrema o de alto riesgo"
            }.get(imc_resultado, "No calculable")

            print(f"{persona.listar_informacion()} Al calcular tu IMC concluimos que tu peso está: {imc_categoria}.")
            print(f"Es mayor de edad: {'Sí' if persona.es_mayor_de_edad() else 'No'}")

        # Preguntar si desea ingresar otra persona
        continuar = input("¿Desea ingresar otra persona? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
