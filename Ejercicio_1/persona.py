from enum import Enum

class Persona:
    class IMC(Enum):
        BAJO_PESO = -1
        PESO_IDEAL = 0
        SOBREPESO = 1
        OBESIDAD = 2
        OBESIDAD_EXTREMA = 3

    _dni_counter = 0  # Atributo de clase para DNI auto-incrementable

    # Constructor por defecto
    def __init__(self, documento="", nombre="", edad=0, sexo='M', peso=0.0, altura=0.0):
        self.__documento = documento
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = self.__comprobar_sexo(sexo)
        self.__peso = peso
        self.__altura = altura
        self.__DNI = self.__genera_dni()

    # Constructor con documento, nombre, edad y sexo
    @classmethod
    def solo_datos_basicos(cls, documento, nombre, edad, sexo):
        return cls(documento, nombre, edad, sexo)

    # Constructor vacío
    @classmethod
    def por_defecto(cls):
        return cls()

    def __comprobar_sexo(self, sexo):
        return sexo if sexo in ['M', 'F'] else 'M'

    def __genera_dni(self):
        Persona._dni_counter += 1
        return Persona._dni_counter

    def calcular_imc(self):
        if self.__altura <= 0:
            return None
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

    def mensaje_imc(self):
        estado = self.calcular_imc()
        if estado is None:
            return "No se puede calcular el IMC (altura no válida)"
        mensajes = {
            self.IMC.BAJO_PESO: "Por debajo del peso",
            self.IMC.PESO_IDEAL: "Normal",
            self.IMC.SOBREPESO: "Con sobrepeso",
            self.IMC.OBESIDAD: "Obesidad",
            self.IMC.OBESIDAD_EXTREMA: "Obesidad extrema o de alto riesgo"
        }
        return mensajes[estado]

    def es_mayor_de_edad(self):
        return self.__edad >= 18

    def listar_informacion(self):
        genero = "Masculino" if self.__sexo == 'M' else "Femenino"
        info = (f"""Hola {self.__nombre}, tu código dentro del sistema es {self.__DNI}. 
                Tu identificación es {self.__documento}. 
                Tu edad es {self.__edad} años. 
                Tu género es {genero}. Tu Peso es {self.__peso} kg.
                Tu Altura es {self.__altura} cm.
                Al calcular tu IMC concluimos que tu peso está: {self.mensaje_imc()}.""")
        return info

    # Getters y setters
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
