class Vehiculo:
    def __init__(self, ruedas:int, color:str) -> None:
        self.ruedas = ruedas
        self.color = color

    def informacion(self) -> None:
        print(self.ruedas, self.color)
