from entidades.Documento import Documento


class Cpf(Documento):
    def __init__(self, cpf: str, nome: str):
        super().__init__(nome)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
