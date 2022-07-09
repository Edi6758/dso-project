from telas.TelaEndereco import TelaEndereco
from entidades.Endereco import Endereco

class ControladorEndereco:

    def __init__(self):
        self.__enderecos_cadastrados = []
        self.__tela_endereco = TelaEndereco()
        self.__endereco_atual = None

    def cadastra_endereco(self):
        dados_endereco = self.__tela_endereco.mostra_cadastro_endereco()
        endereco = Endereco(dados_endereco['estado'], dados_endereco['cidade'], dados_endereco['bairro'], dados_endereco['rua'], dados_endereco['numero'], dados_endereco['cep'])
        self.__enderecos_cadastrados.append(endereco)