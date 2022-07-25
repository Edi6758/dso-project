from telas.TelaDocumento import TelaDocumento
from controles.ControladorUsuario import ControladorUsuario


class ControladorDocumento:
    def __init__(self):
        self.__tela_documento = TelaDocumento()
        self.__controlador_usuario = ControladorUsuario()

