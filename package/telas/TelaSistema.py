import PySimpleGUI as sg


class TelaSistema:
    def tela_login_sistema(self):
        layout = [
            [sg.Text('usuario')],
            [sg.Input(key='usuario')],
            [sg.Text('senha')],
            [sg.Input(key='senha')],
            [sg.Button('login')],
            [sg.Text('', key='mensagem')],
        ]

        window = sg.Window('login', layout=layout)
        resultado = False
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'login':
                senha_correta = 'admin'
                usuario_correto = 'admin'
                usuario = values['usuario']
                senha = values['senha']
                if usuario == usuario_correto and senha == senha_correta:
                    window['mensagem'].update('login feito com sucesso')
                    resultado = True
                    window.close()
                    return resultado
                else:
                    window['mensagem'].update('login ou senha incorretos')

    def menu_principal(self) -> int:
        layout = [
            [sg.Text(' O que você deseja fazer?')],
            [sg.Button('Cadastrar Usuario', size=(30, 3))],
            [sg.Button('Listar Usuario', size=(30, 3))],
            [sg.Button('Editar Usuario', size=(30, 3))],
            [sg.Button('Deletar Usuario', size=(30, 3))],
            [sg.Button('Validar Documentos', size=(30, 3))],
            [sg.Button('Sair', size=(30, 3))],
        ]

        window = sg.Window('Menu Empresa', layout=layout,)

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            return 0
        elif event == 'Cadastrar Usuario':
            window.close()
            return 1
        elif event == 'Listar Usuario':
            window.close()
            return 2
        elif event == 'Editar Usuario':
            window.close()
            return 3
        elif event == 'Deletar Usuario':
            window.close()
            return 4
        elif event == 'Validar Documentos':
            window.close()
            return 5
        else: return 0

    def logado_com_sucesso(self):
        layout = [
            [sg.Text('logado com sucesso')],
            [sg.Button('OK')],
        ]

        window = sg.Window('login', layout=layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'OK':
                window.close()
                break

    def mostrar_opcoes_documentos(self):
        layout = [
            [sg.Button('Validar cpf', size=(30, 3))],
            [sg.Button('Validar rg', size=(30, 3))],
            [sg.Button('Validar titulo', size=(30, 3))],
        ]

        window = sg.Window('Menu Empresa', layout=layout,)

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            return 0
        elif event == 'Validar cpf':
            window.close()
            return 1
        elif event == 'Validar rg':
            window.close()
            return 2
        elif event == 'Validar titulo':
            window.close()
            return 3
