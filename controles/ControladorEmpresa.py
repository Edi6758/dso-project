from telas.TelaEmpresa import TelaEmpresa
from entidades.Empresa import Empresa


class ControladorEmpresa:

    def __init__(self):
        self.__empresas_cadastradas = []
        self.__tela_empresa = TelaEmpresa()

    def cadastrar_empresa(self):
        dados_empresa = self.__tela_empresa.mostra_cadastro_empresa()
        empresa = Empresa(dados_empresa['nome'], dados_empresa['cnpj'], dados_empresa['endereco'])
        if self.__empresas_cadastradas:
            for i in self.__empresas_cadastradas:
                if i.cnpj == empresa.cnpj:
                    self.__tela_empresa.empresa_duplicada()
                    break
            else:
                self.__empresas_cadastradas.append(empresa)
        else:
            self.__empresas_cadastradas.append(empresa)
        print(self.__empresas_cadastradas)

    def listar_nomes_empresas_cadastradas(self):
        self.__tela_empresa.menu_nomes_empresas()
        for i in self.__empresas_cadastradas:
            print('   ', i.nome)

    def acessar_empresa(self):
        empresa_a_ser_acessada = self.__tela_empresa.acessar_empresa()

        if self.__empresas_cadastradas:
            for i in self.__empresas_cadastradas:
                if i.nome == empresa_a_ser_acessada:
                    self.__tela_empresa.empresa_acessada_com_sucesso()
                    return i
            else:
                return False


    def excluir_empresa(self):
        empresa_a_ser_excluida = self.__tela_empresa.excluir_empresa()
        if self.__empresas_cadastradas:
            for i in self.__empresas_cadastradas:
                if i.nome == empresa_a_ser_excluida:
                    self.__empresas_cadastradas.remove(i)
                    self.__tela_empresa.empresa_excluida_com_sucesso()
                    return True
            else:
                return False
