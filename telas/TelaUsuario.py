

class TelaUsuario:
    def cadastrar_usuario(self):
        print('------CADASTRO USUARIO')
        nome = input('qual o nome?')
        cpf = input('qual o cpf?')
        rg = input('qual o rg?')
        email = input('qual o email?')
        senha = input('qual a senha?')

        return {'nome': nome, 'cpf': cpf, 'rg': rg, 'email': email, 'senha': senha}

    def usuario_duplicado(self):
        print(' esse cpf já foi cadastrado')

    def qual_a_empresa(self):
        opcao = input('qual o cnpj da empresa que vc quer cadastrar o usuario?')
        return opcao

    def qual_o_usuario(self):
        opcao = input('qual o cpf do usuario que vc quer excluir ou editar?')
        return opcao

    def mostra_opcoes_para_alterar(self):
        print('------ ALTERAR ------'
              '\n1 - alterar nome '
              '\n2 - alterar cpf'
              '\n3 - alterar rg'
              '\n4 - alterar email'
              '\n5 - alterar senha')
        opcao = input('qual a opcao?')
        return opcao

    def recebe_novo_dado(self):
        return input('qual o novo dado')
