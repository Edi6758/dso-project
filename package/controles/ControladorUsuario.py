from package.service.DocumentoService import DocumentoService
from package.service.ValidacaoService import ValidacaoService
from package.telas.TelaUsuario import TelaUsuario
from package.entidades.Usuario import Usuario
from package.telas.TelaDocumento import TelaDocumento
from package.telas.TelaExcessoes import TelaExcessoes
from package.excessoes.UsuarioJahCadastradoException import UsuarioJahCadastrado


class ControladorUsuario:
    def __init__(self):
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []
        self.__tela_documento = TelaDocumento()
        self.__usuario_atual = None
        self.__tela_exception = TelaExcessoes()
        self.__documento_service = DocumentoService()
        self.__validacao_service = ValidacaoService()


    @property
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, usuarios):
        self.__usuarios = usuarios

    def cadastrar_usuario(self):
        dados_usuario: dict = self.__tela_usuario.cadastrar_usuario()
        try:
            if dados_usuario['contrato']:
                val_contrato = self.__documento_service.validar_contrato(
                    document=self.__validacao_service.read_image_to_text(dados_usuario['contrato']),
                    nome=dados_usuario['nome'],
                    cpf=dados_usuario['cpf'],
                    rg=dados_usuario['rg'],
                    num_matricula=dados_usuario['num_matricula'])
            else: val_contrato = False

            if dados_usuario['matricula']:
                val_matricula = self.__documento_service.validar_matricula(
                    document=self.__validacao_service.read_image_to_text(dados_usuario['matricula']),
                    nome=dados_usuario['nome'])
            else: val_matricula = False

            if dados_usuario['procuracao']:
                val_procuracao = self.__documento_service.validar_procuracao(
                    document=self.__validacao_service.read_image_to_text(dados_usuario['procuracao']),
                    nome=dados_usuario['nome'])
            else: val_procuracao = False

            if dados_usuario['requerimento']:
                val_requerimento = self.__documento_service.validar_requerimento(
                    document=self.__validacao_service.read_image_to_text(dados_usuario['requerimento']),
                    nome=dados_usuario['nome'])
            else: val_requerimento = False

            if dados_usuario['cert_civil']:
                val_cert_civil = self.__documento_service.validar_cert_criminal(
                    document=self.__validacao_service.read_image_to_text(dados_usuario['cert_civil']),
                    nome=dados_usuario['nome'],
                    cpf=dados_usuario['cpf'])
            else: val_cert_civil = False

            if dados_usuario['cert_cnd']:
                val_cert_cnd = self.__documento_service.validar_cert_cnd(
                    document=self.__validacao_service.read_image_to_text(dados_usuario['cert_cnd']),
                    nome=dados_usuario['nome'],
                    cpf=dados_usuario['cpf'])
            else: val_cert_cnd = False

            if dados_usuario['cert_casamento']:
                val_cert_casamento = self.__documento_service.validar_cert_casamento(
                    document=self.__validacao_service.read_image_to_text(dados_usuario['cert_casamento']),
                    nome=dados_usuario['nome'],
                    cpf=dados_usuario['cpf'])
            else: val_cert_casamento = False

            usuario = Usuario(
                dados_usuario['nome'],
                dados_usuario['cpf'],
                dados_usuario['rg'],
                dados_usuario['titulo'],
                dados_usuario['email'],
                dados_usuario['senha'],
                val_contrato,
                val_matricula,
                val_procuracao,
                val_requerimento,
                val_cert_civil,
                val_cert_cnd,
                val_cert_casamento
            )

            if self.__usuarios:
                for i in self.__usuarios:
                    if i.cpf == usuario.cpf:
                        raise UsuarioJahCadastrado
                else:
                    self.__usuarios.append(usuario)
            else:
                self.__usuarios.append(usuario)
        except TypeError:
            self.__tela_exception.UsuarioVazio()
            pass
        except UsuarioJahCadastrado:
            self.__tela_exception.UsuarioJahCadastrado()

    def listar_usuario(self):
        lista_usuarios = []
        if self.__usuarios:
            for i in self.__usuarios:
                lista_usuarios.append(i.nome)
        self.__tela_usuario.listar_usuarios(lista=lista_usuarios)

    def editar_usuario(self):
        usuario_a_ser = self.__tela_usuario.qual_o_usuario_a_editar()
        if self.__usuarios:
            for i in self.__usuarios:
                if i.cpf == usuario_a_ser:
                    opcao = self.__tela_usuario.mostra_opcoes_para_alterar()
                    if opcao == 1:
                        i.nome = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == 2:
                        i.cpf = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == 3:
                        i.rg = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == 4:
                        i.email = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == 5:
                        i.senha = self.__tela_usuario.recebe_novo_dado()
            else:
                self.__tela_exception.UsuarioNaoExiste()

    def excluir_usuario(self):
        usuario_a_ser = self.__tela_usuario.qual_o_usuario_a_excluir()
        if self.__usuarios:
            for i in self.__usuarios:
                if i.cpf == usuario_a_ser:
                    self.__usuarios.remove(i)
            else:
                self.__tela_exception.UsuarioNaoExiste()

    def validar_cpf(self):
        usuario_a_acessar = self.__tela_usuario.acessar_usuario()
        for i in self.__usuarios:
            if i.cpf == usuario_a_acessar:
                self.__usuario_atual = i
                arquivo_cpf = self.__tela_documento.validacao_cpf()
                if self.__usuario_atual.cpf == arquivo_cpf:
                    self.__tela_documento.validado()
                else:
                    self.__tela_documento.nao_validado()
        else:
            pass

    def validar_rg(self):
        usuario_a_acessar = self.__tela_usuario.acessar_usuario()
        for i in self.__usuarios:
            if i.cpf == usuario_a_acessar:
                self.__usuario_atual = i
                arquivo_rg = self.__tela_documento.validacao_rg()
                if self.__usuario_atual.rg == arquivo_rg:
                    self.__tela_documento.validado()
                else:
                    self.__tela_documento.nao_validado()
        else:
            pass

    def validar_titulo(self):
        usuario_a_acessar = self.__tela_usuario.acessar_usuario()
        for i in self.__usuarios:
            if i.cpf == usuario_a_acessar:
                self.__usuario_atual = i
                arquivo_titulo = self.__tela_documento.validacao_titulo()
                if self.__usuario_atual.titulo == arquivo_titulo:
                    self.__tela_documento.validado()
                else:
                    self.__tela_documento.nao_validado()
        else:
            pass
