from package.service.DocumentoService import DocumentoService
from package.service.UsuarioService import UsuarioService
from package.telas.TelaExcessoes import TelaExcessoes
from package.telas.TelaValidacao import TelaValidacao


class ControladorValidacao:
    def __init__(self):
        self.__usuarioService = UsuarioService()
        self.__documento_service = DocumentoService()
        self.__tela = TelaValidacao()
        self.__tela_excessoes = TelaExcessoes()

    def cadastrar_validacoes(self):
        usuario = self.__usuarioService.getUsuarioByCpf(self.__tela.getUsuarioCpf())
        if not usuario:
            self.__tela_excessoes.UsuarioNaoExiste()
            return 
        arquivosValidacao = self.__tela.menu_principal()
        validacoes = self.__documento_service.verifyValidacoesByUserDto(
                arquivosValidacao,
                usuario)
        self.__usuarioService.saveValidacoesByUsuarioId(usuario.id, validacoes)
        self.__tela.documentos_validados(validacoes)
