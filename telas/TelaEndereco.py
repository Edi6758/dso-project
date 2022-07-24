import PySimpleGUI as sg

class TelaEndereco:

    def mostra_cadastro_endereco(self):
            layout = [
                [sg.Text('qual o estado?')],
                [sg.Input(key='estado')],
                [sg.Text('qual o cidade?')],
                [sg.Input(key='cidade')],
                [sg.Text('qual o bairro?')],
                [sg.Input(key='bairro')],
                [sg.Text('qual a rua?')],
                [sg.Input(key='rua')],
                [sg.Text('qual o numero?')],
                [sg.Input(key='numero')],
                [sg.Text('qual o cep?')],
                [sg.Input(key='cep')],
                [sg.Button('Cadastrar')]
            ]
            window = sg.Window('cadastro endereço', layout=layout)

            event, values = window.read()

            while True:
                if event == sg.WINDOW_CLOSED:
                    window.close()
                elif event == 'Cadastrar':
                    estado = values['estado']
                    cidade = values['cidade']
                    bairro = values['bairro']
                    rua = values['rua']
                    numero = values['numero']
                    cep = values['cep']
                    window.close()
                    return {'estado': estado, 'cidade': cidade, 'bairro': bairro, 'rua': rua, 'numero': numero, 'cep': cep}

    def endereco_a_ser_editado(self):
        print('Menu de alteração de endereço')
        opcao = input('qual o cep do endereço a ser alterado?')
        return opcao

    def endereco_a_excluir(self):
        layout = [
            [sg.Text('qual o cep do endereço que você deseja excluir?')],
            [sg.Input(key='endereco')],
            [sg.Button('Excluir')]
        ]

        window = sg.Window('Exclusão Endereco', layout=layout)

        event, values = window.read()
        while True:
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Excluir':
                endereco = values['endereco']
                window.close()
                return endereco

    def listar_endereco(self, lista: []):
        lista = lista
        layout = [
            sg.popup_scrolled(*lista, title='lista endereco')
        ]
