

class TelaSistema:
    def mostra_opcoes_tela_inicial(self):
        print("---------MENU-----------"
              "\nEscolha a opcao"
              "\n1 - Cadastrar Empresa"
              "\n2 - Acessar Empresa"
              "\n3 - Deletar Empresa"
              "\n0 - Encerrar")
        opcao = int(input("qual a sua opção?"))
        return opcao

    def tela_login_sistema(self):
        print("---------LOGIN SISTEMA-----------")
        usuario_sistema = input("qual o usuario?")
        senha_sistema = input("qual a senha?")
        return usuario_sistema and senha_sistema

    def tela_login_sistema_incorreto(self):
        print("usuario e/ou senha incorretos")

