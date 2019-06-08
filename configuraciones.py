import os



class Configuracion():
    def __init__(self,):
        self.palabras = None

    @property
    def palabras(self):
        """
        lista de objetos(Palabra) de la sopa de letras
        """
        return self.palabras

    @palabras.setter
    def palabras(self, palabras):
        self.palabras = palabras


class validacion():
    def validar_con_wikcionario(self, palabra):
        pass

    def validar_con_pattern(self, palabra):
        pass


class Palabra():
    def __init__(self, nombre, definicion):
        self.nombre = nombre
        self.definicion = definicion

    @property
    def nombre(self):
        return self.nombre

    @property.setter
    def nombres(self, nombre):
        self.nombre = nombre

    @property
    def definicion(self):
        return self.definicion

    @property.setter
    def definicion(self, definicion):
        self.definicion = definicion
