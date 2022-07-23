from telas.TelaSistema import TelaSistema
from controles.ControladorEmpresa import ControladorEmpresa
from controles.ControladorUsuario import ControladorUsuario
from controles.ControladorEndereco import ControladorEndereco


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_empresa = ControladorEmpresa()
        self.__controlador_usuario = ControladorUsuario()
        self.__controlador_endereco = ControladorEndereco()

    def inicia_sistema(self):
        self.abre_tela()

    def encerra(self):
        exit(0)

    def valida_login(self, dados_login):
        if dados_login == ("admin", "admin"):
            return True
        else:
            pass
            #pegar o controlador de empresas, a lista de empresas
            #para cada empresa pegar a lista de usuarios
            #comparar login e senha com cada usuario de cada empresa

    def abre_tela(self):
        while True:
            if self.__tela_sistema.tela_login_sistema() is True:
                self.__tela_sistema.logado_com_sucesso()
                while True:
                    opcao = self.__tela_sistema.mostra_opcoes_tela_inicial()
                    if opcao == 1:
                        self.__controlador_empresa.cadastrar_empresa()
                    elif opcao == 2:
                        empresa_acessada = self.__controlador_empresa.acessar_empresa()
                        if empresa_acessada:
                            while True:
                                opcao_empresa_acessada = self.__tela_sistema.mostra_opcoes_tela_empresa_acessada()
                                if opcao_empresa_acessada == 1:
                                    empresa_acessada.cadastrar_usuario()
                                elif opcao_empresa_acessada == 2:
                                    empresa_acessada.listar_usuario()
                                elif opcao_empresa_acessada == 3:
                                    empresa_acessada.editar_usuario()
                                elif opcao_empresa_acessada == 4:
                                    empresa_acessada.excluir_usuario()
                                elif opcao_empresa_acessada == 5:
                                    empresa_acessada.cadastrar_endereco()
                                elif opcao_empresa_acessada == 6:
                                    empresa_acessada.excluir_endereco()
                                elif opcao_empresa_acessada == 7:
                                    empresa_acessada.listar_enderecos()
                                elif opcao_empresa_acessada == 0:
                                    break
                    elif opcao == 3:
                        self.__controlador_empresa.excluir_empresa()
                    elif opcao == 0:
                        break
            else:
                break
