import PySimpleGUI as sg


class TelaUsuario:
    def cadastrar_usuario(self):
        layout = [
            [sg.Text('qual o nome?')],
            [sg.Input(key='nome')],
            [sg.Text('qual o cpf?')],
            [sg.Input(key='cpf')],
            [sg.Text('qual o rg?')],
            [sg.Input(key='rg')],
            [sg.Text('qual o num. matricula?')],
            [sg.Input(key='num_matricula')],
            [sg.Text('qual o titulo?')],
            [sg.Input(key='titulo')],
            [sg.Text('qual o email?')],
            [sg.Input(key='email')],
            [sg.Text('qual a senha?')],
            [sg.Input(key='senha')],
            [sg.Button('Cadastrar')]
        ]
        window = sg.Window('cadastro usuario', layout=layout)
        event, values = window.read()
        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'Cadastrar':
                if values['nome'] != '' and\
                   values['cpf'] != '' and\
                   values['titulo'] != '' and\
                   values['rg'] != '' and\
                   values['email'] != '' and\
                   values['senha'] != '' and\
                   values['num_matricula'] != '':
                    nome = values['nome']
                    cpf = values['cpf']
                    titulo = values['titulo']
                    rg = values['rg']
                    email = values['email']
                    senha = values['senha']
                    num_matricula = values['num_matricula']
                    window.close()

                    return {
                        'nome': nome,
                        'cpf': cpf,
                        'rg': rg,
                        'num_matricula': num_matricula,
                        'titulo': titulo,
                        'email': email,
                        'senha': senha,
                    }
                else:
                    window.close()
                    break

    def usuario_duplicado(self):
        print(' esse cpf já foi cadastrado')

    def qual_a_empresa(self):
        opcao = input('qual o cnpj da empresa que vc quer cadastrar o usuario?')
        return opcao

    def qual_o_usuario_a_excluir(self):
        layout = [
            [sg.Text('qual o cpf do usuario que você deseja excluir?')],
            [sg.Input(key='usuario')],
            [sg.Button('Excluir')]
        ]

        window = sg.Window('Exclusão Usuario', layout=layout)

        event, values = window.read()
        while True:
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Excluir':
                cpf = values['usuario']
                window.close()
                return cpf

    def qual_o_usuario_a_editar(self):
        layout = [
            [sg.Text('qual o cpf do usuario que você deseja Editar?')],
            [sg.Input(key='usuario')],
            [sg.Button('Editar')]
        ]

        window = sg.Window('Editar Usuario', layout=layout)

        event, values = window.read()
        while True:
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Editar':
                cpf = values['usuario']
                window.close()
                return cpf


    def mostra_opcoes_para_alterar(self):
        layout = [
            [sg.Text('Qual dado você deseja alterar?')],
            [sg.Button('NOME')],
            [sg.Button('CPF')],
            [sg.Button('RG')],
            [sg.Button('EMAIL')],
            [sg.Button('SENHA')],
        ]

        window = sg.Window('opções dados', layout=layout)

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
        elif event == 'NOME':
            window.close()
            return 1
        elif event == 'CPF':
            window.close()
            return 2
        elif event == 'RG':
            window.close()
            return 3
        elif event == 'EMAIL':
            window.close()
            return 4
        elif event == 'SENHA':
            window.close()
            return 5


    def recebe_novo_dado(self):
        layout = [
            [sg.Text('qual o novo dado?')],
            [sg.Input(key='dado')],
            [sg.Button('editar')]
        ]
        window = sg.Window('novo dado', layout=layout)
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
        elif event == 'editar':
            dados = values['dado']
            window.close()
            return dados

    def listar_usuarios(self, lista):
        lista = lista
        layout = [
            sg.popup_scrolled(*lista, title='lista usuarios')
        ]

    def acessar_usuario(self):
        layout = [
            [sg.Text('Qual o cpf do usuario a acessar?')],
            [sg.Input(key='cpf_acessar')],
            [sg.Button('ok')]
        ]

        window = sg.Window('usuario a acessar', layout=layout)
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            window.close()
        elif event == 'ok':
            cpf = values['cpf_acessar']
            window.close()
            return cpf
