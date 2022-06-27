from entidades.Endereco import Endereco


class Empresa:
    def __init__(self, nome: str, cnpj: str, endereco: Endereco):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__endereco = endereco

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
