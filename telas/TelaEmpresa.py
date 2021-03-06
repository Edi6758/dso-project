from telas.TelaEndereco import TelaEndereco
from controles.ControladorEndereco import ControladorEndereco
import PySimpleGUI as sg


class TelaEmpresa:
    def __init__(self):
        self.__tela_endereco = TelaEndereco()
        self.__controlador_endereco = ControladorEndereco()

    def mostra_cadastro_empresa(self):
        layout = [
            [sg.Text('qual o nome da empresa?')],
            [sg.Input(key='nome')],
            [sg.Text('qual o cnpj da empresa?')],
            [sg.Input(key='cnpj')],
            [sg.Button('Cadastrar')]
        ]

        window = sg.Window('Cadastro Empresa', layout=layout)

        event, values = window.read()
        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == 'Cadastrar':
                if values['nome'] != '' and values['cnpj'] != '':
                    nome = values['nome']
                    cnpj = values['cnpj']
                    window.close()
                    return {'nome': nome, 'cnpj': cnpj}
                else:
                    window.close()
                    break

    def acessar_empresa(self, lista: list):
        lista_empresa = lista
        layout = [
            [sg.Text('Escreva o nome da Empresa a ser acessada:')],
            [sg.Input(key='empresa')],
            [sg.Button('acessar'), sg.Button('Listar')]
        ]

        window = sg.Window('Menu de Acesso', layout=layout, size=(300, 150))
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Listar':
                sg.popup_scrolled(*lista_empresa, title='Lista de Empresas')
            elif event == 'acessar':
                empresa_selecionada = values['empresa']
                window.close()
                return empresa_selecionada

    def empresa_acessada_com_sucesso(self):
        layout = [
            [sg.Text('acessado com sucesso')],
            [sg.Button('OK')],
        ]

        window = sg.Window('acesso', layout=layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'OK':
                window.close()
                break
    def excluir_empresa(self, lista: list):
        lista_empresa = lista
        layout = [
            [sg.Text('Escreva o nome da Empresa a ser exclu??da:')],
            [sg.Input(key='empresa')],
            [sg.Button('excluir'), sg.Button('Listar')]
        ]

        window = sg.Window('Menu Exclus??o', layout=layout, size=(300, 150))
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Listar':
                sg.popup_scrolled(*lista_empresa, title='Lista de Empresas')
            elif event == 'excluir':
                empresa_selecionada = values['empresa']
                window.close()
                return empresa_selecionada


    def empresa_excluida_com_sucesso(self):
        layout = [
            [sg.Text('excluido com sucesso')],
            [sg.Button('OK')],
        ]

        window = sg.Window('excluido', layout=layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'OK':
                window.close()
                break

    def empresa_duplicada(self):
            layout = [
                [sg.Text('Empresa j?? cadastrada')],
                [sg.Button('OK')],
            ]

            window = sg.Window('Empresa j?? cadastrada', layout=layout)
            event, values = window.read()

            while True:
                if event == sg.WINDOW_CLOSED:
                    window.close()
                    break
                elif event == 'OK':
                    window.close()
                    break


