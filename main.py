import PySimpleGUI as sg
from windows import *

sg.change_look_and_feel('DarkAmber')

layout = [
    [sg.Button('Matematika',size=(15,1)), sg.Button('Fyzika',size=(15,1))]
]

window = sg.Window('Calculator',
                   layout,
                   element_justification='center')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Matematika':
        matematika_menu()
    elif event == 'Fyzika':
        pass

window.close()

