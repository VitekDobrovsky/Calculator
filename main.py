import PySimpleGUI as sg
from windows import *

sg.theme('Topanga')

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
        fyzika_menu()

window.close()

