from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario
from telas.TelaDocumento import TelaDocumento

class ControladorUsuario:
    def __init__(self):
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []
        self.__tela_documento = TelaDocumento()


    @property
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, usuarios):
        self.__usuarios = usuarios

    def cadastrar_usuario(self):
        dados_usuario = self.__tela_usuario.cadastrar_usuario()
        usuario = Usuario(dados_usuario['nome'], dados_usuario['cpf'],dados_usuario['rg'], dados_usuario['titulo'], dados_usuario['email'],
                          dados_usuario['senha'])

        if self.__usuarios:
            for i in self.__usuarios:
                if i.cpf == usuario.cpf:
                    print('cpf cadastrado')
            else:
                self.__usuarios.append(usuario)
        else:
            self.__usuarios.append(usuario)

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

    def excluir_usuario(self):
        usuario_a_ser = self.__tela_usuario.qual_o_usuario_a_excluir()
        if self.__usuarios:
            for i in self.__usuarios:
                if i.cpf == usuario_a_ser:
                    self.__usuarios.remove(i)

    def validar_cpf(self):
        arquivo_cpf = self.__tela_documento.validacao_cpf()
        oi = True
        if oi is True:
            for i in self.__usuarios:
                if i.cpf == arquivo_cpf:
                    self.__tela_documento.validado()
                    return True
            else:
                self.__tela_documento.nao_validado()

    def validar_rg(self):
        arquivo_rg = self.__tela_documento.validacao_rg()
        oi = True
        if oi is True:
            for i in self.__usuarios:
                if i.rg == arquivo_rg:
                    self.__tela_documento.validado()
                    return True
            else:
                self.__tela_documento.nao_validado()

    def validar_titulo(self):
        arquivo_titulo = self.__tela_documento.validacao_titulo()
        oi = True
        if oi is True:
            for i in self.__usuarios:
                if i.titulo == arquivo_titulo:
                    self.__tela_documento.validado()
                    return True
            else:
                self.__tela_documento.nao_validado()
