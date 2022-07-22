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
                break
            elif event == 'Cadastrar':
                nome = values['nome']
                cnpj = values['cnpj']
                window.close()
                return {'nome': nome, 'cnpj': cnpj}

    def menu_nomes_empresas(self):
        print('---------Menu das Empresas Cadastradas---------')

    def acessar_empresa(self):
        print("---------MENU DE ACESSO-----------")
        empresa_escolhida = input('qual o nome da empresa que deseja acessar?')
        return empresa_escolhida

    def empresa_acessada_com_sucesso(self):
        print('empresa acessada com sucesso')

    def excluir_empresa(self, lista: list):
        lista_empresa = lista
        layout = [
            [sg.Text('Escreva o nome da Empresa a ser excluída:')],
            [sg.Input(key='empresa')],
            [sg.Button('excluir'), sg.Button('Listar')]
        ]


        window = sg.Window('Menu Exclusão', layout=layout, size=(250,200))
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
        print('empresa excluida com sucesso')

    def empresa_duplicada(self):
        print('essa empresa já foi cadastrada')
