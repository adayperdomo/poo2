class Vehiculo:
    def __init__(self, ruedas:int, color:str) -> None:
        self.ruedas = ruedas
        self.color = color

    def informacion(self) -> None:
        print("El automovil tiene", self.ruedas, "y es de color", self.color)
        print("la bicicleta tiene", self.ruedas, "y es de color", self.color)
        print("El camion tiene", self.ruedas, "y es de color", self.color)
        print("la moto tiene", self.ruedas, "y es de color", self.color)