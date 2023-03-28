
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
