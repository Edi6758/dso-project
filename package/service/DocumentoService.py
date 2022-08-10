import re
from package.service.CredencialService import CredencialService


class DocumentoService:
    def __init__(self):
        self.__credencial_service = CredencialService()

    def validar_contrato(self, document, nome, cpf, rg, num_matricula) -> bool:
        return self.__credencial_service.validar_verbato(document, nome)\
           and self.__credencial_service.validar_cpf(document, cpf)\
           and self.__credencial_service.validar_rg(document, rg)\
           and self.__credencial_service.validar_num_matricula(document, num_matricula)

    def validar_matricula(self, document, nome) -> bool:
        return self.__credencial_service.validar_padrao(
            document, re.compile(r'\b[V|v]alidade[:]? \d* [D|d]ias')) and\
            self.__credencial_service.validar_verbato(document, nome)

    def validar_procuracao(self, document, nome) -> bool:
        return self.__credencial_service.validar_verbato(document, nome)

    def validar_requerimento(self, document, nome) -> bool:
        return self.__credencial_service.validar_verbato(document, nome)

    def validar_cert_criminal(self, document, nome, cpf) -> bool:
        return self.__credencial_service.validar_verbato(document, nome)\
            and self.__credencial_service.validar_verbato(document, "NADA CONSTA")\
            and self.__credencial_service.validar_cpf(document, cpf)

    def validar_cert_cnd(self, document, nome, cpf):
        return self.__credencial_service.validar_verbato(document, nome)\
            and self.__credencial_service.validar_padrao(document, re.compile(r'\b[V|v]alidade[:]? \d* [D|d]ias'))\
            and self.__credencial_service.validar_verbato(document, "NÃO constam registros de citações de ações reais")\
            and self.__credencial_service.validar_cpf(document, cpf)

    def validar_cert_casamento(self, document, nome, cpf):
        return self.__credencial_service.validar_verbato(document, nome) and\
               self.__credencial_service.validar_cpf(document, cpf)

