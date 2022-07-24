from telas.TelaEndereco import TelaEndereco
from entidades.Endereco import Endereco

class ControladorEndereco:

    def __init__(self):
        self.__enderecos = []
        self.__tela_endereco = TelaEndereco()

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
        if self.__enderecos:
            for endereco in self.__enderecos:
                lista_cpfs_cadastrados.append(endereco.cep)
        self.__tela_endereco.listar_endereco(lista=lista_cpfs_cadastrados)


    def excluir_endereco(self):
        endereco_a_excluir = self.__tela_endereco.endereco_a_excluir()
        for i in self.__enderecos:
            if i.cep == endereco_a_excluir:
                self.__enderecos.remove(i)
        else:
            print('esse cep não está cadastrado')
