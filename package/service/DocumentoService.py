import re
from package.entidades.ValidacaoDocumentoEnum import ValidacaoDocumentoEnum
from package.service.CredencialService import CredencialService
from package.service.ValidacaoService import ValidacaoService


class DocumentoService:
    def __init__(self):
        self.__credencial_service = CredencialService()
        self.__validacaoService = ValidacaoService()

    def getValidacaoByEnumEntry(self, e: ValidacaoDocumentoEnum):
        map = {
            ValidacaoDocumentoEnum.CONTRATO: self.validar_contrato,
            ValidacaoDocumentoEnum.MATRICULA: self.validar_matricula,
            ValidacaoDocumentoEnum.PROCURACAO: self.validar_procuracao,
            ValidacaoDocumentoEnum.REQUERIMENTO: self.validar_requerimento,
            ValidacaoDocumentoEnum.CERT_CIVIL: self.validar_cert_criminal,
            ValidacaoDocumentoEnum.CERT_CND: self.validar_cert_cnd,
            ValidacaoDocumentoEnum.CERT_CASAMENTO: self.validar_cert_casamento
        }
        return map[e]

    def verifyValidacoesByUserDto(self, validacoesDto: dict, userDto):
        documentos_validados = []
        validacoes = {
            'contrato': ValidacaoDocumentoEnum.CONTRATO,
            'matricula': ValidacaoDocumentoEnum.MATRICULA,
            'procuracao': ValidacaoDocumentoEnum.PROCURACAO,
            'requerimento': ValidacaoDocumentoEnum.REQUERIMENTO,
            'cert_civil': ValidacaoDocumentoEnum.CERT_CIVIL,
            'cert_cnd': ValidacaoDocumentoEnum.CERT_CND,
            'cert_casamento': ValidacaoDocumentoEnum.CERT_CASAMENTO
        }
        for key, value in validacoesDto.items():
            if key in validacoes.keys() and value:
                f = self.getValidacaoByEnumEntry(validacoes[key])
                if f(self.__validacaoService.read_image_to_text(value), userDto):
                    documentos_validados.append(validacoes[key])

        return documentos_validados

    def validar_contrato(self, document, dto) -> bool:
        return self.__credencial_service.validar_verbato(document, dto.nome)\
           and self.__credencial_service.validar_cpf(document, dto.cpf)\
           and self.__credencial_service.validar_rg(document, dto.rg)\
           and self.__credencial_service.validar_num_matricula(document, dto.num_matricula)

    def validar_matricula(self, document, dto) -> bool:
        return self.__credencial_service.validar_padrao(
            document, re.compile(r'\b[V|v]alidade[:]? \d* [D|d]ias')) and\
            self.__credencial_service.validar_verbato(document, dto.nome)

    def validar_procuracao(self, document, dto) -> bool:
        return self.__credencial_service.validar_verbato(document, dto.nome)

    def validar_requerimento(self, document, dto) -> bool:
        return self.__credencial_service.validar_verbato(document, dto.nome)

    def validar_cert_criminal(self, document, dto) -> bool:
        return self.__credencial_service.validar_verbato(document, dto.nome)\
            and self.__credencial_service.validar_verbato(document, "NADA CONSTA")\
            and self.__credencial_service.validar_cpf(document, dto.cpf)

    def validar_cert_cnd(self, document, dto):
        return self.__credencial_service.validar_verbato(document, dto.nome)\
            and self.__credencial_service.validar_padrao(document, re.compile(r'\b[V|v]alidade[:]? \d* [D|d]ias'))\
            and self.__credencial_service.validar_verbato(document, "NÃO constam registros de citações de ações reais")\
            and self.__credencial_service.validar_cpf(document, dto.cpf)

    def validar_cert_casamento(self, document, dto):
        return self.__credencial_service.validar_verbato(document, dto.nome) and\
               self.__credencial_service.validar_cpf(document, dto.cpf)

