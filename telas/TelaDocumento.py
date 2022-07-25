import PySimpleGUI as sg


class TelaDocumento:
    def __init__(self):
        pass

    def validacao_cpf(self):
        layout = [
            [sg.Text('qual o cpf/arquivo do usuario a ser validado?')],
            [sg.Input(key='cpf')],
            [sg.Button('Validar')]
        ]

        window = sg.Window('validar cpf', layout=layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Validar':
                cpf = values['cpf']
                window.close()
                return cpf

    def validacao_rg(self):
        layout = [
            [sg.Text('qual o rg/arquivo do usuario a ser validado?')],
            [sg.Input(key='rg')],
            [sg.Button('Validar')]
        ]

        window = sg.Window('validar rg', layout=layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Validar':
                rg = values['rg']
                window.close()
                return rg

    def validacao_titulo(self):
        layout = [
            [sg.Text('qual o titulo/arquivo do usuario a ser validado?')],
            [sg.Input(key='titulo')],
            [sg.Button('Validar')]
        ]

        window = sg.Window('validar titulo', layout=layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Validar':
                titulo = values['titulo']
                window.close()
                return titulo

    def validado(self):
        layout = [
            [sg.Text('Documento validado com sucesso')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Validado', layout=layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def nao_validado(self):
        layout = [
            [sg.Text('Não foi possivel validar o documento')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Validado', layout=layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break
