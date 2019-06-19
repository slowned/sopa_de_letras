import PySimpleGUI as sg 

def paleta_colores():
    
    colors = ['BLUE', 'GREEN2', 'RED1', 'YELLOW', 'CYAN', 'GREY', 'MAGENTA','DARKORANGE1','BLACK']

    sg.SetOptions(button_element_size=(12,1), element_padding=(0,0), auto_size_buttons=False, border_width=0)

    layout = [[sg.Text('ELIJA COLOR DESEADO:', text_color='black', font='Calibri 11')]]
    row = []
    layout = []
    # -- Create primary color viewer window --
    for rows in range(3):
        row = []
        for i in range(3):
            try:
                color = colors[rows+3*i]
                row.append(sg.Button(border_width=0, button_color=('black', color), key=color))
            except:
                pass
        layout.append(row)

    window = sg.Window('Color Viewer', grab_anywhere=False, font=('any 9')).Layout(layout)

    # -- Event loop --
    while True:
        event,values = window.Read()
        if event is None:
            break
        else:
            if(event in colors):
                window.Close()
                return(event)
     
#layout para elegir colores a los diferentes tipos de palabras!

dict_color = {}        

layout =[[sg.Button('Verbo',key='verb'), sg.Button('Sustantivo',key='noun'), sg.Button('Adjetivo',key='adjetive')]]

window = sg.Window('Color', grab_anywhere=False, font=('any 9')).Layout(layout)

# -- Event loop --
while True:
    event, values = window.Read()
    print(event)
    if event is None:
        break
    elif event == 'verb':
        color_select = paleta_colores()
        dict_color['Verbo']=color_select
        print(dict_color)
    elif event == 'noun':
        color_select = paleta_colores()
        dict_color['Sustantivo']=color_select
        print(dict_color)
    elif event == 'adjetive':
        color_select = paleta_colores()
        dict_color['Adjetivo']=color_select
        print(dict_color)
    window.Element(event).Update(button_color=(('black',('blue',color_select)[True])))