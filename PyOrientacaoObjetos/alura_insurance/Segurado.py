
from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente
from Beneficiario import Beneficiario
from Apolice import Apolice


class Segurado:
    def __init__(self, cliente=Cliente, endereco=Endereco, contato=Contato,
                 beneficiario=Beneficiario, apolice=Apolice):
        self._endereco = endereco
        self._contato = contato
        self._cliente = cliente
        self._beneficiario = beneficiario
        self._apolice = apolice

    @property
    def cliente(self):
        return self._cliente

    @property
    def endereco(self):
        return self._endereco

    @property
    def contato(self):
        return self._contato

    @property
    def beneficiario(self):
        return self._beneficiario

    @property
    def apolice(self):
        return self._apolice


dados = Segurado(('Ana', 'Barreto', '00/45/4466', '943892619278512'),
                 ('Cidade nova', '21', 'ap 1023',
                  '4320978', 'RJ', 'Rio de Janeiro'),
                 ('21 99985 3145', '21 3222 6666', '21 0000 9999', 'ana@hotmail.com'), 1)
print(dados)
print(
    f'dados pessoais: {dados.cliente}, {dados.endereco}, {dados.contato}, {dados.beneficiario}')
