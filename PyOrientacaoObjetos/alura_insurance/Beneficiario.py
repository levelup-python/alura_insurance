
from enum import Enum

from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente


class TipoBeneficiario(Enum):
    parente = 1
    amigo = 2
    outros = 3


class Beneficiario(Cliente, Endereco):
    def __init__(self, nome, sobrenome, cpf, rg, data_nascimento, rua, numero, complemento,
                 cep, estado, cidade, contato=Contato, tipo=TipoBeneficiario):
        self._contato = contato
        self._tipo = tipo
        super(Cliente).__init__(self, nome,
                                sobrenome)
        super(Endereco).__init__(
            rua, numero)

    def nome_completo(self):
        print(f' nome completo: {self._nome} {self._sobrenome}')

    @property
    def tipo(self):
        return self._tipo

    @property
    def contato(self):
        return self._contato


dados = Beneficiario('Ana', 'Barreto', '00/45/4466', '943892619278512',
                     'Cidade nova', '21', 'ap 1023',
                     '4320978', 'RJ', 'Rio de Janeiro',
                     '21 99985 3145', '21 3222 6666',  1)
print(dados)
print(
    f'dados pessoais: {dados.nome}, {dados.rua}, {dados.contato}, {dados.tipo}')
