from package.service.UsuarioService import UsuarioService
from package.telas.TelaUsuario import TelaUsuario
from package.telas.TelaExcessoes import TelaExcessoes
from package.excessoes.UsuarioJahCadastradoException import UsuarioJahCadastrado


class ControladorUsuario:
    def __init__(self):
        self.__tela_usuario = TelaUsuario()
        self.__tela_exception = TelaExcessoes()
        self.__usuarioService = UsuarioService()

    @property
    def usuarios(self):
        return self.__usuarioService.getUsuarios()

    def cadastrar_usuario(self):
        dados_usuario: dict | None = self.__tela_usuario.cadastrar_usuario()
        try:
            model = self.__usuarioService.convertDictToEntity(dados_usuario)
            validacoes = self.__usuarioService.getValidacoesFromUsuarioDto(dados_usuario)
            usuarios = self.__usuarioService.getUsuarios()

            for usuario in usuarios:
                if usuario.cpf == model.cpf:
                    raise UsuarioJahCadastrado

            self.__usuarioService.persist(model)

            usuario_id = self.__usuarioService.getUsuarioByCpf(model.cpf).id
            self.__usuarioService.saveValidacoesByUsuarioId(usuario_id, validacoes)

        # except TypeError:
        #     self.__tela_exception.UsuarioVazio()
        #     pass
        except UsuarioJahCadastrado:
            self.__tela_exception.UsuarioJahCadastrado()

    def listar_usuarios(self):
        usuarios = self.__usuarioService.getUsuarios()
        nomes = [usuario.nome for usuario in usuarios]
        self.__tela_usuario.listar_usuarios(lista=nomes)

    def editar_usuario(self):
        cpf = self.__tela_usuario.qual_o_usuario_a_editar()
        usuarios = self.__usuarioService.getUsuarios()

        for usuario in usuarios:
            if usuario.cpf == cpf:
                opcao = self.__tela_usuario.mostra_opcoes_para_alterar()
                if opcao == 1:
                    usuario.nome = self.__tela_usuario.recebe_novo_dado()
                elif opcao == 2:
                    usuario.cpf = self.__tela_usuario.recebe_novo_dado()
                elif opcao == 3:
                    usuario.rg = self.__tela_usuario.recebe_novo_dado()
                elif opcao == 4:
                    usuario.email = self.__tela_usuario.recebe_novo_dado()
                elif opcao == 5:
                    usuario.senha = self.__tela_usuario.recebe_novo_dado()
        else:
            self.__tela_exception.UsuarioNaoExiste()

    def excluir_usuario(self):
        cpf = self.__tela_usuario.qual_o_usuario_a_excluir()
        usuarios = self.__usuarioService.getUsuarios()
        for usuario in usuarios:
            if usuario.cpf == cpf:
                self.__usuarioService.deleteUsuarioById(usuario.id)
                return
        self.__tela_exception.UsuarioNaoExiste()
