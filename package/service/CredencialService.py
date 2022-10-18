from datetime import date
import re

from typing import Pattern
from package.service.ValidacaoService import ValidacaoService


class CredencialService:
    def __init__(self):
        self.__validacao_service = ValidacaoService()

    def validar_cpf(self, text: str, reference: str) -> bool:
        pattern = re.compile(
            r"\b\d{3}[\.|\,|\s]?\d{3}[\.|\,|\s]?\d{3}[\-|\/|\.|\,|\s]?\d{2}"
        )
        return self.__validacao_service.validate(pattern, reference, text)

    def validar_rg(self, text: str, reference: str) -> bool:
        pattern = re.compile(r"\b\d[\.|\,|\s]?\d{3}[\.|\,|\s]?\d{3}")
        return self.__validacao_service.validate(pattern, reference, text)

    def validar_num_matricula(self, text: str, reference: str) -> bool:
        pattern = re.compile(r"\b\d{2}[\.]?\d{3}")
        return self.__validacao_service.validate(pattern, reference, text)

    def validar_padrao(self, text: str, pattern: Pattern[str]) -> bool:
        return self.__validacao_service.match(pattern, text)

    def validar_data(self, text, reference_date: date, format_string: str):
        match_string = reference_date.strftime(format_string)
        return self.__validacao_service.find(match_string, text)

    def validar_verbato(self, text, reference) -> bool:
        return self.__validacao_service.find(reference, text)
