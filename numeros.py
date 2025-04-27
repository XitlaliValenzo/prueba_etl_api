class Numeros:

    def __init__(self):
        self.numeros = list(range(1,101))

    def extract(self,numero):
        if numero<=100 and numero>0:
            self.numeros.remove(numero)
        else:
            raise ValueError("El número debe estar entre 1 a 100")
    
    def calcular_numero_extraido(self):
        for i in range(1, 101):
            if i not in self.numeros:
                return i
        raise False