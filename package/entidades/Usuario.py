

class Usuario:
    def __init__(self,
            nome: str,
            cpf: str,
            rg: str,
            titulo: str,
            email: str,
            senha: str,
            validacao_contrato: bool = False,
            validacao_matricula: bool = False,
            validacao_procuracao: bool = False,
            validacao_requerimento: bool = False,
            validacao_cert_civil: bool = False,
            validacao_cert_cnd: bool = False,
            validacao_cert_casamento: bool = False):

        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__titulo = titulo
        self.__email = email
        self.__senha = senha
        self.__validacao_contrato = validacao_contrato
        self.__validacao_matricula = validacao_matricula 
        self.__validacao_procuracao = validacao_procuracao 
        self.__validacao_requerimento = validacao_requerimento 
        self.__validacao_cert_civil = validacao_cert_civil 
        self.__validacao_cert_cnd = validacao_cert_cnd 
        self.__validacao_cert_casamento = validacao_cert_casamento 

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
    def validacao_contrato(self):
        return self.__validacao_contrato

    @property
    def validacao_matricula(self):
        return self.__validacao_matricula

    @property
    def validacao_procuracao(self):
        return self.__validacao_procuracao

    @property
    def validacao_requerimento(self):
        return self.__validacao_requerimento

    @property
    def validacao_cert_civil(self):
        return self.__validacao_cert_civil

    @property
    def validacao_cert_cnd(self):
        return self.__validacao_cert_cnd

    @property
    def validacao_cert_casamento(self):
        return self.__validacao_cert_casamento

