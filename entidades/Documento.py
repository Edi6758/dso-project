from abc import ABC, abstractmethod


class Documento(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
