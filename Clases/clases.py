class circulo:
    def __init__(self, radio):
        self._radio = radio
        try:
            if self.radio <= 0:
                raise ValueError("El radio debe ser mayor que 0")
        except ValueError as error:
            print(error)
            exit()    
    def area(self):
        return self.radio ** 2 * 3.14
    def perimetro(self):
        return self.radio * 2 * 3.14