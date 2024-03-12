class Transporte:
    def __init__(self, *, ruedas:int, asientos:int) -> None:
        self.ruedas = ruedas
        self.asientos = asientos

    def desplazar(self, x:int, y:int = 0) -> None:
        print("Has sido desplazado a", x, y)

    def informacion(self) -> None:
        print("La guagua tiene:", self.ruedas, "y", self.asientos, "asientos,")
    
