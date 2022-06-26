import PySimpleGUI as sg
import math

sg.change_look_and_feel('DarkAmber')

def matematika_menu():
    layout = [
        [sg.Button('Obvod Kruhu', size=(15, 1)), sg.Button('Obsah Kruhu', size=(15, 1))],
        [sg.Button('Povrch Válce', size=(15, 1)), sg.Button('Objem Válce', size=(15, 1))],
        [sg.Button('Zpět', key='-CLOSE-')]
    ]

    window = sg.Window('Matematika', layout, element_justification='center')

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == 'Obvod Kruhu':
            obvod_kružnice()
        elif event == 'Obsah Kruhu':
            obsah_kružnice()
        elif event == 'Povrch Válce':
            povrch_válce()
        elif event == 'Objem Válce':
            pass

    window.close()

def obvod_kružnice():
    obvod_kružnice_layout = [
        [sg.Text('Poloměr:'),sg.Input(key='-RADIUS-',size=10,),sg.Text('cm',justification='left')],
        [sg.Button('Vypočítat Obvod Kružnice', key='-CALCULATE-')],
        [sg.Text(key='-RESULT-'), sg.Text(key='-ROUND_RES-',justification='left')],
        [sg.VPush()],
        [sg.Push(),sg.Button('Zpět',key='-CLOSE-')]
        ]

    obvod_kružnice_window = sg.Window('Obvod Kružnice',obvod_kružnice_layout,size=(300,130),element_justification='center')

    while True:
        event, value = obvod_kružnice_window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == '-CALCULATE-':
            try:
                radius = float(value['-RADIUS-'])
                result = math.pi * (2 * radius)
                obvod_kružnice_window['-RESULT-'].update(f'{result} cm')
                obvod_kružnice_window['-ROUND_RES-'].update(f'≐ {round(result,1)} cm')
            except ValueError:
                obvod_kružnice_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                obvod_kružnice_window['-ROUND_RES-'].update('')

    obvod_kružnice_window.close()

def obsah_kružnice():
    obsah_kružnice_layout = [
        [sg.Text('Poloměr:'), sg.Input(key='-RADIUS-', size=10), sg.Text('cm',justification='left')],
        [sg.Button('Vypočítat Obsah Kružnice', key='-CALCULATE-')],
        [sg.Text(key='-RESULT-'), sg.Text(key='-ROUND_RES-', justification='left')],
        [sg.VPush()],
        [sg.Push(), sg.Button('Zpět', key='-CLOSE-')]
    ]

    obsah_kružnice_window = sg.Window('Obsah Kružnice',obsah_kružnice_layout,size=(300,130),element_justification='center')

    while True:
        event, value = obsah_kružnice_window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == '-CALCULATE-':
            try:
                radius = float(value['-RADIUS-'])
                result = math.pi * (radius ** 2)
                obsah_kružnice_window['-RESULT-'].update(f'{result} cm2')
                obsah_kružnice_window['-ROUND_RES-'].update(f'≐ {round(result,1)} cm2')
            except ValueError:
                obsah_kružnice_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                obsah_kružnice_window['-ROUND-RES-'].update('')

    obsah_kružnice_window.close()

def povrch_válce():
    povrch_válce_layout = [
        [sg.Text('Poloměr podstavy:'),sg.Input(size=10,key='-RADIUS-'),sg.Text('cm')],
        [sg.Text('Výška válce:        '),sg.Input(size=10,key='-HEIGHT-'),sg.Text('cm')],
        [sg.Button('Vypočítat Povrch Válce',key='-CALCULATE-')],
        [sg.Text(key='-RESULT-'),sg.Text(key='-ROUND_RES-',justification='left')],
        [sg.VPush()],
        [sg.Push(), sg.Button('Zpět', key='-CLOSE-')]
    ]

    povrch_válce_window = sg.Window('Povrch Válce',povrch_válce_layout,size=(300,155))

    while True:
        event, value = povrch_válce_window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == '-CALCULATE-':
            try:
                radius = float(value['-RADIUS-'])
                height = float(value['-HEIGHT-'])
                podstavy = 2 * (math.pi * (radius**2))
                plášť = height * (math.pi * (radius * 2))
                result = podstavy + plášť
                povrch_válce_window['-RESULT-'].update(f'{result} cm2 ')
                povrch_válce_window['-ROUND_RES-'].update(f'≐ {round(result,1)} cm2')
            except ValueError:
                povrch_válce_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                povrch_válce_window['-ROUND_RES-'].update('')

    povrch_válce_window.close()

