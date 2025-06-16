class Persona:
    class IMC:
        BAJO_PESO = -1
        PESO_IDEAL = 0
        SOBREPESO = 1
        OBESIDAD = 2
        OBESIDAD_EXTREMA = 3

    def __init__(self, documento="", nombre="", edad=0, sexo='M', peso=0.0, altura=0.0):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.__comprobar_sexo(sexo)
        self.__peso = peso
        self.__altura = altura
        self.__DNI = self.__genera_dni()

    def __comprobar_sexo(self, sexo):
        return sexo if sexo in ['M', 'F'] else 'M'

    def __genera_dni(self):
        if not hasattr(Persona, '_dni_counter'):
            Persona._dni_counter = 100000  # Inicia el contador de DNI
        Persona._dni_counter += 1
        return Persona._dni_counter

    def calcular_imc(self):
        if self.__altura > 0:
            imc = self.__peso / ((self.__altura / 100) ** 2)
            if imc < 18.5:
                return self.IMC.BAJO_PESO
            elif 18.5 <= imc <= 24.9:
                return self.IMC.PESO_IDEAL
            elif 25.0 <= imc <= 29.9:
                return self.IMC.SOBREPESO
            elif 30.0 <= imc <= 39.9:
                return self.IMC.OBESIDAD
            else:
                return self.IMC.OBESIDAD_EXTREMA
        return None

    def es_mayor_de_edad(self):
        return self.__edad >= 18

    def listar_informacion(self):
        return (f"Hola {self.__nombre}, tu código dentro del sistema es {self.__DNI}. "
                f"Tu identificación es {self.__documento}. Tu edad es {self.__edad} años. "
                f"Tu género es {'Masculino' if self.__sexo == 'M' else 'Femenino'}. "
                f"Tu Peso es {self.__peso} kg y tu Altura es {self.__altura} cm.")

    # Métodos get y set
    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = self.__comprobar_sexo(sexo)

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura
