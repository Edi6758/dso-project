import PySimpleGUI as sg


class TelaExcessoes:

    def EmpresaNaoEncontrada(self):
        layout = [
            [sg.Text('Não foi possivel encontrar essa empresa')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Empresa Não Encontrada', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def EmpresaVazia(self):
        layout = [
            [sg.Text('Não foi possivel cadastrar pois os dados estão vazios')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Empresa Vazia', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def UsuarioVazio(self):
        layout = [
            [sg.Text('Não foi possivel cadastrar pois os dados estão vazios')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Usuario Vazio', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def UsuarioJahCadastrado(self):
        layout = [
            [sg.Text('Não foi possivel cadastrar pois um usuario com esse cpf ja existe')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Usuario Ja Existe', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def EnderecoVazio(self):
        layout = [
            [sg.Text('Não foi possivel cadastrar pois os dados estão vazios')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Endereco Vazio', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def EnderecoJahCadastrado(self):
        layout = [
            [sg.Text('Não foi possivel cadastrar pois um endereco com esse cep ja existe')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Endereco Ja Existe', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def UsuarioNaoExiste(self):
        layout = [
            [sg.Text('Não existe um usuario com esse cpf cadastrado')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Usuario', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break

    def EnderecoNaoExiste(self):
        layout = [
            [sg.Text('Não existe um Endereco com esse cep cadastrado')],
            [sg.Button('OK')],
        ]

        window = sg.Window('Endereco', layout=layout)
        event, values = window.read()

        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'OK':
                window.close()
                break
