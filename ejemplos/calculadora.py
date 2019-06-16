import PySimpleGUI as sg

# Demonstrates a number of PySimpleGUI features including:      
#   Default element size      
#   auto_size_buttons      
#   Button      
#   Dictionary return values      
#   Update of elements in window (Text, Input)    
#   do_not_clear of Input elements

layout = [[sg.Text('Enter Your Passcode')],      
          [sg.Input(size=(10, 1), do_not_clear=True, justification='right', key='input')],      
          [sg.Button('1'), sg.Button('2'), sg.Button('3')],      
          [sg.Button('4'), sg.Button('5'), sg.Button('6')],      
          [sg.Button('7'), sg.Button('8'), sg.Button('9')],      
          [sg.Button('Submit'), sg.Button('0'), sg.Button('Clear')],      
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='out')],      
          ]

window = sg.Window('Keypad', layout, default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)

# Loop forever reading the window's values, updating the Input field    
keys_entered = ''      
while True:      
    event, values = window.Read()  # read the window    
    if event is None:  # if the X button clicked, just exit      
        break      
    if event == 'Clear':  # clear keys if clear button      
        keys_entered = ''      
    elif event in '1234567890':  # os.ascii.all()      
        print(values)
        keys_entered = values['input']  # get what's been entered so far      
        keys_entered += event  # add the new digit      
    elif event == 'Submit':      
        keys_entered = values['input']      
        window.Element('out').Update(keys_entered)  # output the final string

    window.Element('input').Update(keys_entered)  # change the window to reflect current key string
