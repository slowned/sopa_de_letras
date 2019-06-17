import random
from pattern.es import parse
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from wiktionaryparser import WiktionaryParser

from constantes import ALFABETO

__all__ = [
    'Configuracion',
    'Palabra',
    'Validacion',
    'generar_reporte',
]


class Palabra():
    def __init__(self, nombre, definicion):
        self.__nombre = nombre
        self.__definicion = definicion
        self.longitud = len(self.nombre)
        self.__tipo = self.get_tipo()
        self.__posicion = ""

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, posicion):
        self.__posicion = posicion

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


VERBOS = [
    'jugar',
    'llamar',
    'saltar',
    'correr',
    'buscar',
    'comer',
    'ver',
    'hablar',
]

ADJETIVOS = [
    'afortunado',
    'alto',
    'negro',
    'obsecuente',
    'paciente',
    'extremo',
    'famoso',
    'inteligente',
]

SUSTANTIVOS = [
    'animal',
    'libro',
    'aire',
    'esfera',
    'planta',
    'programa',
    'guitarra',
    'idea',
    'trabajo',
    'ciruela',
    'vaso',
]


VERBOS = [Palabra(sus, 'def') for sus in VERBOS]
SUSTANTIVOS = [Palabra(sus, 'def') for sus in SUSTANTIVOS]
ADJETIVOS = [Palabra(sus, 'def') for sus in ADJETIVOS]

PALABRAS_TODAS = {VERB: VERBOS, ADJECTIVE: ADJETIVOS, NOUN: SUSTANTIVOS}

class Configuracion():
    """
    clase de configuracion para la sopa de letras
    """

    # __palabras_todas = {NOUN: [], VERB: [], ADJECTIVE: []}
    __palabras_todas = PALABRAS_TODAS
    alfabeto = ALFABETO

    def __init__(self):
        # self.cantidad = cantidad
        self.palabras_juego = []
        self.__ayuda = ""
        self.__direccion = ""
        self.__tamanio = ""

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
        # valores = {
        #     '_ayuda_si_': True,
        #     '_ayuda_no_': False,
        #     '_direccion_vertical_': True,
        #     '_direccion_orizontal_': False,
        #     '_tamanio_mayuscula_': True,
        #     '_tamanio_minuscula_': False,
        # } 

        opciones = {}
        for key, value in valores.items():
            if value is True:
                opciones.update({key: value})

        if '_ayuda_si_' in opciones.keys():
            self.ayuda = True
        else:
            self.ayuda = False

        if '_direccion_vertical_' in opciones.keys():
            self.direccion = True
        else:
            self.direccion = False

        if '_tamanio_minuscula_' in opciones.keys():
            self.tamanio = True
        else:
            self.tamanio = False


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


