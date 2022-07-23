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
            elif event == 'Cadastrar':
                nome = values['nome']
                cpf = values['cpf']
                rg = values['rg']
                email = values['email']
                senha = values['senha']
                window.close()
                return {'nome': nome, 'cpf': cpf, 'rg': rg, 'email': email, 'senha': senha}

    def usuario_duplicado(self):
        print(' esse cpf já foi cadastrado')

    def qual_a_empresa(self):
        opcao = input('qual o cnpj da empresa que vc quer cadastrar o usuario?')
        return opcao

    def qual_o_usuario(self):
        opcao = input('qual o cpf do usuario que vc quer excluir ou editar?')
        return opcao

    def mostra_opcoes_para_alterar(self):
        print('------ ALTERAR ------'
              '\n1 - alterar nome '
              '\n2 - alterar cpf'
              '\n3 - alterar rg'
              '\n4 - alterar email'
              '\n5 - alterar senha')
        opcao = input('qual a opcao?')
        return opcao

    def recebe_novo_dado(self):
        return input('qual o novo dado')
