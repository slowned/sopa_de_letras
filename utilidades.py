import random
import PySimpleGUI as sg
from pattern.es import parse
from pattern.text.es.inflect import NOUN, VERB, ADJECTIVE
from wiktionaryparser import WiktionaryParser
import string






__all__ = [
    'Configuracion',
    'Palabra',
    'Validacion',
    'Notificacion'
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

# --------- Constantes para mokear datos ------
ALFABETO = string.ascii_letters
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

    __palabras_todas = {NOUN: [], VERB: [], ADJECTIVE: []}
    # __palabras_todas = PALABRAS_TODAS
    alfabeto = ALFABETO

    def __init__(self):
        # self.cantidad = cantidad
        self.palabras_juego = []
        self.__ayuda = ""
        self.colores = {}
        self.__direccion = ""
        self.__errores = {}
        self.__keys = ""
        self.__tamanio = False
        self.json_datos = False
        self.oficina = ""
    @property
    def errores(self):
        return self.__errores

    @errores.setter
    def errores(self, error):
        """
            error[0]: Tipo de error
            error[1]: Mensage a mostrar
        """
        self.__errores.update({error[0]: error[1]})

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, keys):
        self.__keys = keys

    @property
    def palabras_todas(self):
        return self.__palabras_todas

    @palabras_todas.setter
    def palabras_todas(self, palabras):
        self.__palabras_todas = palabras

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
        self.__ayuda = ayuda

    @property
    def direccion(self):
        # TODO: prodria ser una tupla
        # ((True, "vertical"), (False, "horizontal"))
        """ valores: True o False
        representacion: True = vertical
                        False = horizontal
        """
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

    def sin_palabras(self):
        sin_palabras = True
        for lista_palabras in self.palabras_todas.values():
            if len(lista_palabras) > 0:
                sin_palabras = False
        return sin_palabras

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
        if self.sin_palabras():
            self.palabras_todas = PALABRAS_TODAS

        opciones = {}
        for key, value in valores.items():
            if value is True:
                opciones.update({key: value})

        if '_ayuda_si' in opciones.keys():
            self.ayuda = True
        elif '_ayuda_no' in opciones.keys():
            self.ayuda = False

        if '_vertical_si' in opciones.keys():
            self.direccion = True
        elif '_vertical_no':
            self.direccion = False

        if '_tamanio_minuscula_' in opciones.keys():
            self.tamanio = True

        else:
            self.tamanio = False

        if '__oficina1__' in opciones.keys():
            self.oficina = 'oficina1'

        elif '__oficina2__' in opciones.keys():
            self.oficina = 'oficina2'

        elif '__oficina3__' in opciones.keys():
            self.oficina = 'oficina3'

        elif '__oficina4__' in opciones.keys():
            self.oficina = 'oficina4'

        elif '__oficina5__' in opciones.keys():
            self.oficina = 'oficina5'
        else:
            self.oficina = False

    def agregar_color(self, tipo, color):
        """
            tipo: sustantivo, adjetivo, verbo
            color: color de cuando se va seleccionando la palabra
        """
        if color in self.colores.values():
            # TODO: pop up NO PUEDE REPETIR LOS COLORES
            mensaje = ("ERROR", "Tenes que elejir un color distinto para cada tip[o de palabra")
            Notificacion.aviso(mensaje)
        else:
            self.colores.update({tipo: color})


class Notificacion():
    @classmethod
    def aviso(cls, mensaje):
        """
            mensaje[0] encabezado del error
            mensaje[1] mensaje a mostrar
        """
        sg.Popup(mensaje[0], mensaje[1])

    @classmethod
    def generar_reporte(cls, palabra):
        """
        genera reporte de palabras no existentes
        """
        reporte = open("reporte.txt", "a+")
        reporte.write(palabra)

    @classmethod
    def instrucciones(cls):
        sg.Popup('Instructivo',
        '1) Elegir el tipo de palabra a buscar:',
        'SUSTANTIVO-VERBO-ADJETIVO',
        '2) Presionar sobre las letras hasta colorear la palabra',
        '3) Puede presionar el boton "Deshacer" si usted cree que se equivoco de letra/palabra',
        '4) Presionar tecla "Agregar" cuando usted crea que coloreo la palabra correcta',
        '5) Volver al paso 1) hasta que crea que haya seleccionado todas las palabras en la sopa',
        '6) Presionar "Verificar" y usted sabrá si gano o perdio el juego')


class Validacion():
    wiki = WiktionaryParser


    @classmethod
    def validar_con_wikcionario(cls, palabra):
        """:return (True, definicion)
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
            Al instanciar una palabra se valida con pattern en tipo (Verbo, Sustantivo, Adjetivo)
            ------------------
        """
        pass

    @classmethod
    def ganar(cls, palabras_ganar, seleccionadas):
        """ Verifica si las palabras seleccionadas por el jugador
            coinciden con las palabras elejeridas por la profesora.
        """
        # print(palabras_ganar)  # lista Palabras
        # print(seleccionadas)  # { ver: [], susb: [], adj: [] }

        faltantes = [palabra.nombre for palabra in palabras_ganar]

        bien = 0
        correctas = []
        for palabra in palabras_ganar:
            if palabra.tipo in seleccionadas[palabra.tipo]:
                bien += 1
                correctas.append(palabra.nombre)
                faltantes.remove(palabra)

        if len(palabras_ganar) == bien:
            sg.Popup('GANASTE',
                     'Felicitaciones has ganado!!')
        else:
            sg.Popup(
                'perdiste',
                'Lo siento, pero perdiste',
                'palabras totales: {}'.format([palabra.nombre for palabra in palabras_ganar]),
                'palabras correctas: {}'.format(correctas),
                'palabras restantes: {}'.format(faltantes)
            )

    @classmethod
    def verificar_colores(cls, dict_colores):
        """ Controla que sustantivos, adjetivos y verbos
            tengan un color asociado
        """
        print(dict_colores)
        print(len(dict_colores))
        if len(dict_colores) == 3:
            return True
        return False

    @classmethod
    def validar_color_usado(cls, color, lista_colores):
        return (color in lista_colores)

    @classmethod
    def verificar_cantidad_palabras(cls, valores):
        """ Controla que se hallan selecionados al menos un verbo, adjetivo o sustantivo
        """
        verbos = int(valores.get(VERB))
        sustantivos = int(valores.get(NOUN))
        adjetivos = int(valores.get(ADJECTIVE))
        if verbos or sustantivos or adjetivos:
            return True
        return False


def generar_palabras(palabras):
    for nombre in palabras:
        Palabra(nombre, "definicion")
