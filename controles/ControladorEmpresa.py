from telas.TelaEmpresa import TelaEmpresa
from entidades.Empresa import Empresa
from DAO.EmpresaDAO import EmpresaDAO
from excessoes.EmpresaNaoEncontradaException import EmpresaNaoEncontrada
from telas.TelaExcessões import TelaExcessoes


class ControladorEmpresa:

    def __init__(self):
        self.__empresas_cadastradas = []
        self.__tela_empresa = TelaEmpresa()
        self.__empresa_acessada = None
        self.__empresaDao = EmpresaDAO()
        self.__tela_exception = TelaExcessoes()

    def cadastrar_empresa(self):
        dados_empresa = self.__tela_empresa.mostra_cadastro_empresa()
        try:
            empresa = Empresa(dados_empresa['nome'], dados_empresa['cnpj'])
            if self.__empresas_cadastradas:
                for i in self.__empresas_cadastradas:
                    if i.cnpj == empresa.cnpj:
                        self.__tela_empresa.empresa_duplicada()
                        break
                else:
                    self.__empresas_cadastradas.append(empresa)
            else:
                self.__empresas_cadastradas.append(empresa)
        except TypeError:
            self.__tela_exception.EmpresaVazia()
            pass

    def listar_nomes_empresas_cadastradas(self):
        lista = []
        for i in self.__empresas_cadastradas:
            lista.append(i.nome)
        return lista

    def acessar_empresa(self):
        empresa_a_ser_acessada = self.__tela_empresa.acessar_empresa(lista=self.listar_nomes_empresas_cadastradas())
        contador = 0

        try:
            if self.__empresas_cadastradas:
                for i in self.__empresas_cadastradas:
                    if i.nome == empresa_a_ser_acessada:
                        self.__tela_empresa.empresa_acessada_com_sucesso()
                        contador += 1
                        self.__empresa_acessada = i
                        return i
                else:
                    raise EmpresaNaoEncontrada
        except EmpresaNaoEncontrada:
            self.__tela_exception.EmpresaNaoEncontrada()


    def excluir_empresa(self):
        empresa_a_ser_excluida = self.__tela_empresa.excluir_empresa(lista=self.listar_nomes_empresas_cadastradas())
        if self.__empresas_cadastradas:
            for i in self.__empresas_cadastradas:
                if i.nome == empresa_a_ser_excluida:
                    self.__empresas_cadastradas.remove(i)
                    self.__tela_empresa.empresa_excluida_com_sucesso()
                    return True
            else:
                return False

    @property
    def empresa_acessada(self):
        return self.__empresa_acessada
