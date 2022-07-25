from entidades.Documento import Documento


class TituloEleitor(Documento):
    def __init__(self, titulo_eleitor: str, nome: str):
        super().__init__(nome)
        self.__titulo_eleitor = titulo_eleitor

    @property
    def titulo_eleitor(self):
        return self.__titulo_eleitor

    @titulo_eleitor.setter
    def titulo_eleitor(self, titulo_eleitor: str):
        self.__titulo_eleitor = titulo_eleitor
