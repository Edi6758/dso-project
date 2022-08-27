from package.controles.ControladorValidacao import ControladorValidacao
from package.telas.TelaSistema import TelaSistema
from package.controles.ControladorUsuario import ControladorUsuario


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_usuario = ControladorUsuario()
        self.__controlador_validacao = ControladorValidacao()

    def inicia_sistema(self):
        self.abre_tela()

    def encerra(self):
        exit(0)

    def abre_tela(self):
        map = {
            1: self.__controlador_usuario.cadastrar_usuario,
            2: self.__controlador_usuario.listar_usuarios,
            3: self.__controlador_usuario.editar_usuario,
            4: self.__controlador_usuario.excluir_usuario,
            5: self.__controlador_validacao.cadastrar_validacoes,
            0: self.encerra
        }
        if self.__tela_sistema.tela_login_sistema() is True:
            self.__tela_sistema.logado_com_sucesso()
            while True:
                opcao = self.__tela_sistema.menu_principal()
                map[opcao]()
