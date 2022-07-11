from entidades.Endereco import Endereco
from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario

class Empresa:
    def __init__(self, nome: str, cnpj: str, endereco: Endereco):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__endereco = endereco
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def usuarios(self):
        return self.__usuarios

    def cadastrar_usuario(self):
        dados_usuario = self.__tela_usuario.cadastrar_usuario()
        usuario = Usuario(dados_usuario['nome'],dados_usuario['cpf'], dados_usuario['rg'],dados_usuario['email'], dados_usuario['senha'])

        if self.__usuarios:
            for i in self.__usuarios:
                if i.cpf == usuario.cpf:
                    print('cpf cadastrado')
            else:
                self.__usuarios.append(usuario)
        else:
            self.__usuarios.append(usuario)

    def listar_usuario(self):
        if self.__usuarios:
            for i in self.__usuarios:
                print(i.nome)


    def editar_usuario(self):
        usuario_a_ser = self.__tela_usuario.qual_o_usuario()
        if self.__usuarios:
            for i in self.__usuarios:
                if i.cpf == usuario_a_ser:
                    opcao = self.__tela_usuario.mostra_opcoes_para_alterar()
                    if opcao == '1':
                        i.nome = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == '2':
                        i.cpf = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == '3':
                        i.rg = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == '4':
                        i.email = self.__tela_usuario.recebe_novo_dado()
                    elif opcao == '5':
                        i.senha = self.__tela_usuario.recebe_novo_dado()

    def excluir_usuario(self):
        usuario_a_ser = self.__tela_usuario.qual_o_usuario()
        if self.__usuarios:
            for i in self.__usuarios:
                if i.cpf == usuario_a_ser:
                    self.__usuarios.remove(i)
                    print('usuario excluido com sucesso')



