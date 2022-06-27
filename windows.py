import PySimpleGUI as sg
import math

sg.theme('Topanga')

def matematika_menu():
    matematika_layout = [
        [sg.Button('Obvod Kruhu', size=(15, 1)), sg.Button('Obsah Kruhu', size=(15, 1))],
        [sg.Button('Povrch Válce', size=(15, 1)), sg.Button('Objem Válce', size=(15, 1))],
        [sg.Button('Zpět', key='-CLOSE-')]
    ]

    matematika_window = sg.Window('Matematika', matematika_layout, element_justification='center')

    while True:
        event, values = matematika_window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == 'Obvod Kruhu':
            obvod_kružnice()
        elif event == 'Obsah Kruhu':
            obsah_kružnice()
        elif event == 'Povrch Válce':
            povrch_válce()
        elif event == 'Objem Válce':
            objem_válce()

    matematika_window.close()

def fyzika_menu():
    fyzika_layout = [
        [sg.Button('Kinetická Energie',size=(15, 1)),sg.Button('Frekvence',size=(15, 1))],
        [sg.Button('Zpět', key='-CLOSE-')]
    ]

    fyzika_window = sg.Window('Fyzika',fyzika_layout,element_justification='center')

    while True:
        event, value = fyzika_window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == 'Kinetická Energie':
            kinetická_energie()
        elif event == 'Frekvence':
            frekvence()

    fyzika_window.close()

# Matematika
def obvod_kružnice():
    obvod_kružnice_layout = [
        [sg.Text('Poloměr:'),sg.Input(key='-RADIUS-',size=15,),sg.Text('cm',justification='left')],
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
                obvod_kružnice_window['-RESULT-'].update(f'O = {result} cm')
                obvod_kružnice_window['-ROUND_RES-'].update(f'≐ {round(result,1)} cm')
            except ValueError:
                obvod_kružnice_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                obvod_kružnice_window['-ROUND_RES-'].update('')

    obvod_kružnice_window.close()

def obsah_kružnice():
    obsah_kružnice_layout = [
        [sg.Text('Poloměr:'), sg.Input(key='-RADIUS-', size=15), sg.Text('cm',justification='left')],
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
                obsah_kružnice_window['-RESULT-'].update(f'S ={result} cm2')
                obsah_kružnice_window['-ROUND_RES-'].update(f'≐ {round(result,1)} cm2')
            except ValueError:
                obsah_kružnice_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                obsah_kružnice_window['-ROUND-RES-'].update('')

    obsah_kružnice_window.close()

def povrch_válce():
    povrch_válce_layout = [
        [sg.Text('Poloměr podstavy:'),sg.Input(size=15,key='-RADIUS-'),sg.Text('cm')],
        [sg.Text('Výška válce:        '),sg.Input(size=15,key='-HEIGHT-'),sg.Text('cm')],
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
                povrch_válce_window['-RESULT-'].update(f'S = {result} cm2 ')
                povrch_válce_window['-ROUND_RES-'].update(f'≐ {round(result,1)} cm2')
            except ValueError:
                povrch_válce_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                povrch_válce_window['-ROUND_RES-'].update('')

    povrch_válce_window.close()

def objem_válce():
    objem_válce_layout = [
        [sg.Text('Poloměr podstavy:'), sg.Input(key='-RADIUS-',size=15), sg.Text('cm')],
        [sg.Text('Výška válce:        '), sg.Input(key='-HEIGHT-',size=15), sg.Text('cm')],
        [sg.Button('Vypočítat Objem Válce', key='-CALCULATE-')],
        [sg.Text(key='-RESULT-'),sg.Text(key='-ROUND_RES-')],
        [sg.VPush()],
        [sg.Push(),sg.Button('Zpět', key='-CLOSE-')]
    ]

    objem_válce_window = sg.Window('Objem Válce', objem_válce_layout, size=(300,155))

    while True:
        event, value = objem_válce_window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == '-CALCULATE-':
            try:
                radius = float(value['-RADIUS-'])
                height = float(value['-HEIGHT-'])
                result = math.pi * (radius**2) * height
                objem_válce_window['-RESULT-'].update(f'V = {result} cm3')
                objem_válce_window['-ROUND_RES-'].update(f'≐ {round(result,1)} cm3')
            except ValueError:
                objem_válce_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                objem_válce_window['-ROUND_RES-'].update('')

    objem_válce_window.close()

# Fyzika

def kinetická_energie():
    kinetická_energie_layout = [
        [sg.Text('Hmotnost:'),sg.Input(key='-WEIGHT-',size=20),sg.Text('kg')],
        [sg.Text('Rychlost: '),sg.Input(key='-SPEED-',size=20),sg.Text('km/h')],
        [sg.Button('Vypočítat Kinetickou energii',key='-CALCULATE-')],
        [sg.Text(key='-RESULT-'),sg.Text(key='-ROUND_RES-',justification='left')],
        [sg.VPush()],
        [sg.Push(), sg.Button('Zpět', key='-CLOSE-')]
    ]

    kinetická_energie_window = sg.Window('Kinetická Energie',kinetická_energie_layout,size=(300,155))

    while True:
        event, value = kinetická_energie_window.read()

        if event in (sg.WIN_CLOSED, '-CLOSE-'):
            break
        elif event == '-CALCULATE-':
            try:
                weight = float(value['-WEIGHT-'])
                speed_kmh = float(value['-SPEED-'])
                speed_ms = speed_kmh * 0.27777777777778
                result = (1/2) * weight * (speed_ms**2)

                kinetická_energie_window['-RESULT-'].update(f'Ek = {result} J')
                kinetická_energie_window['-ROUND_RES-'].update(f'≐ {round(result,1)} J')
            except ValueError:
                kinetická_energie_window['-RESULT-'].update('DO KOLONKY JSTE NEZADALI ČÍSLA')
                kinetická_energie_window['-ROUND_RES-'].update('')


    kinetická_energie_window.close()

def frekvence():
    pass
