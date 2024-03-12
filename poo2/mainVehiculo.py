from automovil import Automovil
from automovil import Bicicleta
from moto import Moto
from camion import Camion

set = Automovil(4, "blanco")
set.info()

trek = Bicicleta(2, "roja") 
trek.info()

kawasaki = Moto(2, "verde")
kawasaki.info()

rover = Camion(6, "negro")
rover.info()