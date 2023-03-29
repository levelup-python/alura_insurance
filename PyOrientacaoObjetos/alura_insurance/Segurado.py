from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente
from Beneficiario import Beneficiario
from Apolice import Apolice


class Segurado(Cliente, Endereco):
    def __init__(self, nome, sobrenome, cpf, rg, data_nascimento, rua, numero, complemento,
                 cep, estado, cidade, contato=Contato,
                 beneficiario=Beneficiario, apolice=Apolice):
        self._contato = contato
        self._beneficiario = beneficiario
        self._apolice = apolice
        super(Cliente).__init__(self, nome,
                                sobrenome, cpf, rg, data_nascimento)
        super(Endereco).__init__(
            rua, numero, complemento, cep, estado, cidade)

    def nome_completo(self):
        print(f' nome completo: {self.nome} {self.sobrenome}')

    @ property
    def contato(self):
        return self._contato

    @ property
    def beneficiario(self):
        return self._beneficiario

    @ property
    def apolice(self):
        return self._apolice


# cliente1 = Cliente()
# cliente1._nome
