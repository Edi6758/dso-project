from telas.TelaEndereco import TelaEndereco


class TelaEmpresa:
    def __init__(self):
        self.__tela_endereco = TelaEndereco()

    def mostra_cadastro_empresa(self):
        print("---------Cadastro Empresa-----------")

        nome = input("qual o nome da empresa?")
        cnpj = input("qual o cnpj da empresa")
        endereco = self.__tela_endereco.mostra_cadastro_endereco()

        return {'nome': nome, 'cnpj': cnpj, 'endereco': endereco}

    def menu_nomes_empresas(self):
        print('---------Menu das Empresas Cadastradas---------')

    def acessar_empresa(self):
        print("---------MENU DE ACESSO-----------")
        empresa_escolhida = input('qual o nome da empresa que deseja acessar?')
        return empresa_escolhida

    def empresa_acessada_com_sucesso(self):
        print('empresa acessada com sucesso')

    def excluir_empresa(self):
        print("---------MENU DE EXCLUSÃO-----------")
        empresa_escolhida = input('qual o nome da empresa que deseja excluir?')
        return empresa_escolhida

    def empresa_excluida_com_sucesso(self):
        print('empresa excluida com sucesso')
