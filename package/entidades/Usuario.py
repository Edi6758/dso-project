

from typing import List, Optional


class Usuario:
    def __init__(self,
            nome: str,
            cpf: str,
            rg: str,
            titulo: str,
            email: str,
            senha: str,
            num_matricula: str = '',
            id: Optional[int] = None,
            validacoes: Optional[List] = None):

        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__titulo = titulo
        self.__email = email
        self.__senha = senha
        self.__num_matricula = num_matricula
        self.__validacoes = validacoes

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def num_matricula(self):
        return self.__num_matricula

    @num_matricula.setter
    def num_matricula(self, num_matricula):
        self.__num_matricula = num_matricula

    @property
    def validacoes(self):
        return self.__validacoes

    @validacoes.setter
    def validacoes(self, validacoes):
        self.__validacoes = validacoes
