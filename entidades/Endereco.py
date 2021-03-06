

class Endereco:

    def __init__(self, estado: str, cidade: str, bairro: str, rua: str, numero: int, cep: int):
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero
        self.__cep = cep

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep
