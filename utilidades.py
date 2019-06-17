import random
from pattern.es import parse
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from wiktionaryparser import WiktionaryParser

from constantes import ALFABETO, AYUDA, DIRECCION, PALABRAS_TODAS, TAMANIO


__all__ = [
    'Configuracion',
    'Palabra',
    'Validacion',
    'generar_reporte',
]


class Configuracion():
    """
    clase de configuracion para la sopa de letras
    """

    __palabras_todas = {NOUN: [], VERB: [], ADJECTIVE: []}
    alfabeto = ALFABETO

    def __init__(self):
        # self.cantidad = cantidad
        self.palabras_juego = []
        self.__ayuda = ""
        self.__direccion = ""
        self.__tamanio = ""
        self.__posicion = ""

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, posicion):
        self.__posicion = posicion

    @property
    def palabras_todas(self):
        return self.__palabras_todas

    def agregar_palabras(self, palabra):
        """ Palabras agregadas por la profesora """
        self.__palabras_todas[palabra.tipo].append(palabra)

    @property
    def palabras(self):
        """
        lista de objetos(Palabra) de la sopa de letras
        """
        return self.palabras_juego

    @property
    def ayuda(self):
        return self.__ayuda

    @ayuda.setter
    def ayuda(self, ayuda):
        self.__ayuda = True

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @property
    def tamanio(self):
        return self.__tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    def seleccionar_palabras(self, evento):
        """ llega un diccionario con la cantidad de palabras
            verbos:3, adjetivos:2, sustantivos:1
            retorna una lista con N(5) palabras
        """
        cantidad_palabras = {}
        cantidad_palabras.update({VERB: evento[VERB]})
        cantidad_palabras.update({NOUN: evento[NOUN]})
        cantidad_palabras.update({ADJECTIVE: evento[ADJECTIVE]})

        for key, value in cantidad_palabras.items():
            for i in range(int(value)):
                self.palabras.append(random.choice(self.palabras_todas[key]))

    def set_opciones(self, valores):
        """ agarra los opciones seleccionadas y las setea
            a la instancia de configuracion.
            :valores: opciones seleccionadas por la profesora/alumno
        """
        opciones = {}
        for key, value in valores.items():
            if value is True:
                key = key.split('_')[1]
                opciones.update({key: value})

        self.tamanio = opciones[TAMANIO]
        self.direccion = opciones[DIRECCION]
        self.ayuda = opciones[AYUDA]


class Validacion():
    wiki = WiktionaryParser

    @classmethod
    def validar_con_wikcionario(cls, palabra):
        """:return (True, definicion, palabra ,tipo)
            False en caso que la palabra no se encuentre en
            wikcionacio
        """
        try:
            palabra = str(palabra.lower())
            word = cls.wiki().fetch(palabra, "spanish")
            if word[0].get('definitions'):
                definicion = word[0].get('definitions')
                return palabra, definicion
        except:
            print("Error inesperado al consultar con wikcionario")

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

    @classmethod
    def ganar(palabras_ganar, seleccionadas):
        """ Verifica si las palabras seleccionadas por el jugador
            coinciden con las palabras elejeridas por la profesora.
        """
        errores = []
        correctas = []
        for palabra in palabras_ganar:
            if palabra.tipo in seleccionadas[palabra.tipo]:
                correctas.append(palabra)
            else:
                errores.append(palabra)


def generar_palabras(palabras):
    for nombre in palabras:
        Palabra(nombre, "definicion")


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
        """ Verifica su tipo (adj, sus, verb) consuntando
            con Pattern
        """
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
