

class TelaEndereco:

    def mostra_cadastro_endereco(self):
        print("---------Cadastro Endereço-----------")

        estado = input('qual o estado?')
        cidade = input('qual a cidade?')
        bairro = input('qual o bairro')
        rua = input('qual a rua?')
        numero = input('qual o numero')
        cep = input('qual o cep')

        return {'estado': estado, 'cidade': cidade, 'bairro': bairro, 'rua': rua, 'numero': numero, 'cep': cep}

    def endereco_a_ser_editado(self):
        print('Menu de alteração de endereço')
        opcao = input('qual o cep do endereço a ser alterado?')
        return opcao

    def endereco_a_excluir(self):
        opcao = input('qual o cep do endereço a ser excluido?')
        return opcao