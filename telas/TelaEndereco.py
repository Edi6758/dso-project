

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
