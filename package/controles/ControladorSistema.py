from package.telas.TelaSistema import TelaSistema
from package.controles.ControladorEmpresa import ControladorEmpresa
from package.controles.ControladorUsuario import ControladorUsuario
from package.controles.ControladorEndereco import ControladorEndereco
from package.service.DocumentoService import DocumentoService



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
                                    self.__controlador_usuario.cadastrar_usuario()
                                elif opcao_empresa_acessada == 2:
                                    self.__controlador_usuario.listar_usuarios()
                                elif opcao_empresa_acessada == 3:
                                    self.__controlador_usuario.editar_usuario()
                                elif opcao_empresa_acessada == 4:
                                    self.__controlador_usuario.excluir_usuario()
                                elif opcao_empresa_acessada == 5:
                                    self.__controlador_endereco.cadastrar_endereco()
                                elif opcao_empresa_acessada == 6:
                                    self.__controlador_endereco.excluir_endereco()
                                elif opcao_empresa_acessada == 7:
                                    self.__controlador_endereco.listar_enderecos()
                                elif opcao_empresa_acessada == 0:
                                    break
                    elif opcao == 3:
                        self.__controlador_empresa.excluir_empresa()
                    elif opcao == 0:
                        break
            else:
                break
