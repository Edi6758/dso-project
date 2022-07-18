import PySimpleGUI as sg


class TelaSistema:
    def mostra_opcoes_tela_inicial(self):
        print("---------MENU-----------"
              "\nEscolha a opcao"
              "\n1 - Cadastrar Empresa"
              "\n2 - Acessar Empresa"
              "\n3 - Deletar Empresa"
              "\n0 - Encerrar")
        opcao = int(input("qual a sua opção?"))
        return opcao

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
                    return True
                else:
                    window['mensagem'].update('login ou senha incorretos')

    def mostra_opcoes_tela_empresa_acessada(self):
        print("---------MENU-----------"
              "\nEscolha a opcao"
              "\n1 - Cadastrar Usuario"
              "\n2 - Listar Usuarios"
              "\n3 - Editar Usuario"
              "\n4 - Deletar Usuario"
              "\n5 - Cadastrar Endereço"
              "\n6 - Deletar Endereco"
              "\n7 - Listar Enderecos"
              "\n0 - retornar")
        opcao = int(input("qual a sua opção?"))
        return opcao

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
                break
