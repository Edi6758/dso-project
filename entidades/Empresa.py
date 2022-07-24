from telas.TelaEndereco import TelaEndereco

class Empresa:
    def __init__(self, nome: str, cnpj: str):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__enderecos = []
        self.__usuarios = []
        self.__tela_endereco = TelaEndereco()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, usuarios: list):
        self.__usuarios = usuarios
