class carro:
    """clase definida"""
    ruedas = 4
    def __init__(self, color, aceleracion):
        self.color=color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def aceleracion(self):
        self.velocidad = self.velocidad+self.aceleracion

    def frena(self):
        velocidad=self.velocidad-self.aceleracion
        if velocidad < 0:
            velocidad = 0

            self.velocidad = velocidad

carro1 =carro("azul",40)
print("el color del carro  es: ",carro1.color)