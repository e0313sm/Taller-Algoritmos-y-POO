class Cafetera:
    def __init__(self, capacidad_maxima=1000, cantidad_actual=0):
        self.capacidad_maxima = capacidad_maxima
        self.cantidad_actual = min(cantidad_actual, capacidad_maxima)  # Ajustar si es necesario

    def llenar_cafetera(self):
        self.cantidad_actual = self.capacidad_maxima
        print("Cafetera llena.")

    def servir_taza(self, cantidad_taza):
        if self.cantidad_actual >= cantidad_taza:
            self.cantidad_actual -= cantidad_taza
            print(f"Se ha servido una taza de {cantidad_taza} c.c. de café.")
        else:
            print(f"No hay suficiente café. Se ha servido lo que queda: {self.cantidad_actual} c.c.")
            self.cantidad_actual = 0  # Vaciar la cafetera

    def vaciar_cafetera(self):
        self.cantidad_actual = 0
        print("Cafetera vacía.")

    def agregar_cafe(self, cantidad):
        if cantidad < 0:
            print("No se puede agregar una cantidad negativa de café.")
            return
        self.cantidad_actual += cantidad
        if self.cantidad_actual > self.capacidad_maxima:
            self.cantidad_actual = self.capacidad_maxima  # Ajustar al máximo
        print(f"Se han agregado {cantidad} c.c. de café. Cantidad actual: {self.cantidad_actual} c.c.")

    def estado_cafetera(self):
        return (f"Capacidad máxima: {self.capacidad_maxima} c.c., "
                f"Cantidad actual: {self.cantidad_actual} c.c.")
