class Endereco:
    def __init__(self, rua, numero, complemento, cep, estado, cidade):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.estado = estado
        self.cidade = cidade


dados = Endereco('Cidade nova', '21',
                 'ap 1023', '4320978', 'RJ', 'Rio de Janeiro')
