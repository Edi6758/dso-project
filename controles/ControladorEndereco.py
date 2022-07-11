from telas.TelaEndereco import TelaEndereco
from entidades.Endereco import Endereco

class ControladorEndereco:

    def __init__(self):
        self.__enderecos_cadastrados = []
        self.__tela_endereco = TelaEndereco()

    def cadastra_endereco(self):
        dados_endereco = self.__tela_endereco.mostra_cadastro_endereco()
        endereco = Endereco(dados_endereco['estado'], dados_endereco['cidade'], dados_endereco['bairro'], dados_endereco['rua'], dados_endereco['numero'], dados_endereco['cep'])
        if self.__enderecos_cadastrados:
            for i in self.__enderecos_cadastrados:
                if i.cep == endereco.cep:
                    print('cep já cadastrado')
                    break
            else:
                self.__enderecos_cadastrados.append(endereco)
                print('endereco cadastrado com sucesso1')
                print(self.__enderecos_cadastrados)
        else:
            self.__enderecos_cadastrados.append(endereco)
            print('endereco cadastrado com sucesso2')
            print(self.__enderecos_cadastrados)

    def editar_endereco(self):
        endereco_a_alterar = self.__tela_endereco.endereco_a_ser_editado()
        for i in self.__enderecos_cadastrados:
            if i.cep == endereco_a_alterar:
                self.cadastra_endereco()

    def excluir_endereco(self):
        endereco_a_excluir = self.__tela_endereco.endereco_a_excluir()
        for i in self.__enderecos_cadastrados:
            if i.cep == endereco_a_excluir:
                self.__enderecos_cadastrados.remove(i)
        else:
            print('esse cep não está cadastrado')



    def listar_enderecos(self):
        lista_cpfs_cadastrados = []
        for endereco in self.__enderecos_cadastrados:
            lista_cpfs_cadastrados.append(endereco.cep)

        print(lista_cpfs_cadastrados)
