class circulo:
    def __init__(self, radio):
        self._radio = radio
        try:
            if self.radio <= 0:
                raise ValueError("El radio debe ser mayor que 0")
        except ValueError as error:
            print(error)
            exit()

    @property
    def radio(self):
        return self._radio    
    @radio.setter
    def radio(self, radio):
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
    def __mul__(self, n):
        try:
            if n <= 0:
                raise ValueError("no se puede multiplicar por 0, ingresé un numero mayor que 0")
        except ValueError as error:
            print(error)
            exit()
        return circulo (self.radio * n)
    def __str__(self):
        return "Hola, soy un circulo con un radio de: " + str(self.radio) + ". Mi area es: " + str(self.area()) + " y mi perimetro es: " + str(self.perimetro())