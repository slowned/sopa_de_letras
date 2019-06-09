from wiktionaryparser import WiktionaryParser
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from constantes import LISTA_PALABRAS


from pattern.es import parse

__all__ = (
    'Configuracion',
    'Palabra',
    'Validacion',
    'generar_reporte',
)


class Configuracion():
    """
    clase de configuracion para la sopa de letras
    """

    def __init__(self):
        self.palabras = []

    def palabras(self):
        """
        lista de objetos(Palabra) de la sopa de letras
        """
        return self.palabras

    def agregar_palabra(self, palabra):
        self.palabras.append(palabra)


class Validacion():
    parser = WiktionaryParser

    @classmethod
    def validar_con_wikcionario(cls, palabra):
        """:return (True, definicion, palabra ,tipo)
            False en caso que la palabra no se encuentre en
            wikcionacio
        """
        palabra = str(palabra.lower())
        word = cls.parser().fetch(palabra, "spanish")
        if word[0].get('definitions'):
            definicion = word[0].get('definitions')
            return palabra, definicion

        return False, False

    @classmethod
    def validar_con_pattern(cls, palabra):
        """ Retorna el tipo de la palabra
            verbo(VB=verb), adjetivo(JJ=adjetive), sustantivo(NN=noun)
            -------------------
            No se que validar..
            ------------------
        """
        pass


class Palabra():
    def __init__(self, nombre, definicion):
        self.__nombre = nombre
        self.__definicion = definicion
        self.longitud = len(self.nombre)
        self.__tipo = self.get_tipo()

    def __str__(self):
        return self.__nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def definicion(self):
        return self.__definicion

    @definicion.setter
    def definicion(self, definicion):
        self.__definicion = definicion

    @property
    def tipo(self):
        return self.__tipo

    def get_tipo(self):
        parsed = parse(self.nombre)
        parsed = parsed.split('/')
        return parsed[1]

    def posicion(self):
        pass


def generar_reporte(palabra):
    """
    genera reporte de palabras no existentes
    """
    pass

