import PySimpleGUI as sg
layout = [
    [sg.ReadButton("a", key = '_1_'),sg.ReadButton("v",key = '_2_'), sg.ReadButton("e", key = '_3_'),sg.ReadButton("r", key = '_4_'),sg.ReadButton("p", key = '_5_'),  sg.Button("Sustantivo",button_color=('white','#311380'), key='_NOUN_')],
    [sg.ReadButton("a",key = '_6_'),sg.ReadButton("h",key = '_7_'), sg.ReadButton("o",key = '_8_'),sg.ReadButton("l", key = '_9_'),sg.ReadButton("a", key = '_10_'), sg.Button("Verbo", button_color=('white','#007339'), key='_VERBO_')],
    [sg.ReadButton("b", key = '_11_'),sg.ReadButton("u", key = '_12_'), sg.ReadButton("e", key = '_13_'),sg.ReadButton("n", key = '_14_'),sg.ReadButton("o", key = '_15_'),  sg.Button("Adjetivo", button_color=('white','firebrick4'), key = '_ADJETIVE_')],
    [sg.Submit("Verificar"), sg.Button('OK')]
    ]
ventana = sg.Window("Esta es una ventana").Layout(layout)
abecedario = 'abcdefghijklmnopqrstuvwxyz'
nro= ['_1_','_2_','_3_','_4_','_5_','_6_','_7_','_8_','_9_','_10_','_11_','_12_','_13_','_14_','_15_']
while True:
    event, value = ventana.Read()

    lista_key_palabras = ['_NOUN_','_VERBO_', '_ADJETIVE_']
    #OBervacion: los colores viene desde configuracion, para la prueba harcodeamos de la sigueinte manera:
    dic_colores={'_NOUN_':'green','_VERBO_':'red', '_ADJETIVE_':'blue'}
    diccionario_palabras = {'verbo':[], 'sustantivo':[], 'adjetivo':[]}
    if event is None:
        break
    else:
        if(event in lista_key_palabras):
            print(type(event))
            lista_key_disable = lista_key_palabras[:]
            lista_key_disable.remove(event)
            for elemento in lista_key_disable:
                ventana.Element(elemento).Update(disabled=True)

        # letra=event[1]
        if(event in nro ):
            print(value)
            print(event)
            #print(ventana.Element(event).__dict__)
            print(ventana.Element(event).ButtonText)
            ventana.Element(event).Update( button_color=(('white', ('red', 'green')[True])))

        if(event == 'OK'):
            for elemento in lista_key_palabras:
                ventana.Element(elemento).Update(disabled=False)

ventana.Close()
