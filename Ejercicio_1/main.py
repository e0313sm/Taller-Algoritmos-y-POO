from persona import Persona

def pedir_datos():
    documento = input("Ingrese documento: ")
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    sexo = input("Ingrese sexo (M/F): ").upper()
    peso = float(input("Ingrese peso (kg): "))
    altura = float(input("Ingrese altura (cm): "))
    return documento, nombre, edad, sexo, peso, altura

def mostrar_persona(persona):
    print(persona.listar_informacion())
    print(f"¿Es mayor de edad?: {'Sí' if persona.es_mayor_de_edad() else 'No'}")
    print("-" * 60)

def main():
    print("=== Ingreso de Persona 1 ===")
    doc, nom, edad, sexo, peso, alt = pedir_datos()
    persona1 = Persona(doc, nom, edad, sexo, peso, alt)

    print("\n=== Ingreso de Persona 2 (sin peso y altura) ===")
    doc2 = input("Ingrese documento: ")
    nom2 = input("Ingrese nombre: ")
    edad2 = int(input("Ingrese edad: "))
    sexo2 = input("Ingrese sexo (M/F): ").upper()
    persona2 = Persona.solo_datos_basicos(doc2, nom2, edad2, sexo2)

    print("\n=== Persona 3 por defecto ===")
    persona3 = Persona.por_defecto()
    persona3.set_documento("00000000")
    persona3.set_nombre("Persona Genérica")
    persona3.set_edad(20)
    persona3.set_sexo('F')
    persona3.set_peso(65)
    persona3.set_altura(160)

    print("\n=== Resultados ===")
    mostrar_persona(persona1)
    mostrar_persona(persona2)
    mostrar_persona(persona3)

    # Permitir agregar otra persona
    otra = input("¿Desea ingresar otra persona? (s/n): ").lower()
    if otra == 's':
        print("\n=== Nueva Persona ===")
        doc, nom, edad, sexo, peso, alt = pedir_datos()
        nueva = Persona(doc, nom, edad, sexo, peso, alt)
        mostrar_persona(nueva)

if __name__ == "__main__":
    main()
