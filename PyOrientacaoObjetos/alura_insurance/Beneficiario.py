
from enum import Enum

from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente


class TipoBeneficiario(Enum):
    parente = 1
    amigo = 2
    outros = 3


class Beneficiario:
    def __init__(self, cliente=Cliente, endereco=Endereco, contato=Contato, tipo=TipoBeneficiario):
        self._endereco = endereco
        self._contato = contato
        self._tipo = tipo
        self._cliente = cliente

    @property
    def tipo(self):
        return self._tipo

    @property
    def cliente(self):
        return self._cliente

    @property
    def endereco(self):
        return self._endereco

    @property
    def contato(self):
        return self._contato


dados = Beneficiario(('Ana', 'Barreto', '00/45/4466', '943892619278512'),
                     ('Cidade nova', '21', 'ap 1023',
                      '4320978', 'RJ', 'Rio de Janeiro'),
                     ('21 99985 3145', '21 3222 6666', '21 0000 9999', 'ana@hotmail.com'), 1)
print(dados)
print(
    f'dados pessoais: {dados.cliente}, {dados.endereco}, {dados.contato}, {dados.tipo}')
