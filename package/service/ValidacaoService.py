from typing import Pattern
import cv2
import pytesseract
import re

from package.Config import Config
from package.dao.ValidacaoDao import ValidacaoDao
from package.model.ValidacaoDBModel import ValidacaoDBModel


class ValidacaoService:
    def __init__(self):
        self.__validacaoDao = ValidacaoDao()

    def persist(self, model):
        self.__validacaoDao.create(model)

    def convertDictToModel(self, dto: dict) -> ValidacaoDBModel:
        return ValidacaoDBModel(usuario_id=dto["usuario_id"], tipo_validacao_id=dto["tipo_validacao_id"])

    def read_image_to_text(self, path: str) -> str:
        if Config.TESSERACT_CMD: pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_CMD 
        image = cv2.imread(path)
        return re.sub('\s+', ' ', pytesseract.image_to_string(image))

    def validate(self, pattern: Pattern[str], reference: str, text: str) -> bool:
        if not pattern.match(reference): return False

        filter = '.,-/ '
        result = []
        for char in filter: reference = reference.replace(char, '')

        for element in pattern.findall(text):
            for char in filter: element = element.replace(char, '')
            if element == reference: result.append(element)

        return bool(result)

    def match(self, pattern: Pattern[str], text: str) -> bool:
        result = bool(pattern.findall(text))
        return result

    def find(self, reference: str, text: str) -> bool:
        result = bool(re.compile(reference, re.IGNORECASE).findall(text))
        return result

