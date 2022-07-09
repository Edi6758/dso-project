from telas.TelaSistema import TelaSistema
from controles.ControladorEmpresa import ControladorEmpresa


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_empresa = ControladorEmpresa()

    def inicia_sistema(self):
        self.abre_tela()

    def encerra(self):
        exit(0)

    def abre_tela(self):
        while True:
            if self.__tela_sistema.tela_login_sistema() == "admin" and "admin":
                while True:
                    opcao = self.__tela_sistema.mostra_opcoes_tela_inicial()
                    if opcao == 1:
                        self.__controlador_empresa.cadastrar_empresa()
                    elif opcao == 2:
                        self.__controlador_empresa.listar_nomes_empresas_cadastradas()
                        self.__controlador_empresa.acessar_empresa()
                    elif opcao == 3:
                        self.__controlador_empresa.listar_nomes_empresas_cadastradas()
                        self.__controlador_empresa.excluir_empresa()
                    elif opcao == 0:
                        self.encerra()
            else:
                self.__tela_sistema.tela_login_sistema_incorreto()
