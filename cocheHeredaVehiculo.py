# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo():
    color = None
    ruedas = 4
    puertas = None

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self, velocidad, cilindrada, color, puertas):
        super().__init__(color, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

newCoche = Coche("250km/h", 150, "rojo", 4)

print(newCoche)
print(newCoche.color)
print(newCoche.ruedas)
print(newCoche.puertas)
print(newCoche.velocidad)
print(newCoche.cilindrada)
