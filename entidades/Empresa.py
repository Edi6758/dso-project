from entidades.Endereco import Endereco
from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario
from telas.TelaEndereco import TelaEndereco

class Empresa:
    def __init__(self, nome: str, cnpj: str):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__enderecos = []
        self.__usuarios = []
        self.__tela_endereco = TelaEndereco()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, usuarios: list):
        self.__usuarios = usuarios


    def cadastrar_endereco(self):
        dados_endereco = self.__tela_endereco.mostra_cadastro_endereco()
        endereco = Endereco(dados_endereco['estado'], dados_endereco['cidade'], dados_endereco['bairro'],
                            dados_endereco['rua'], dados_endereco['numero'], dados_endereco['cep'])
        if self.__enderecos:
            for i in self.__enderecos:
                if i.cep == endereco.cep:
                    print('cep já cadastrado')
                    break
            else:
                self.__enderecos.append(endereco)
                print('endereco cadastrado com sucesso1')
                print(self.__enderecos)
        else:
            self.__enderecos.append(endereco)
            print('endereco cadastrado com sucesso2')
            print(self.__enderecos)

    def listar_enderecos(self):
        lista_cpfs_cadastrados = []
        for endereco in self.__enderecos:
            lista_cpfs_cadastrados.append(endereco.cep)

        print(lista_cpfs_cadastrados)

    def excluir_endereco(self):
        endereco_a_excluir = self.__tela_endereco.endereco_a_excluir()
        for i in self.__enderecos:
            if i.cep == endereco_a_excluir:
                self.__enderecos.remove(i)
        else:
            print('esse cep não está cadastrado')
