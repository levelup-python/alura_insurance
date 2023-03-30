
from enum import Enum

from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente


class TipoBeneficiario(Enum):
    parente = 1
    amigo = 2
    outros = 3


class Beneficiario():

    def __init__(self, cliente=Cliente, endereco=Endereco,
                 contato=Contato, tipo=TipoBeneficiario):
        self._contato = contato
        self._tipo = tipo
        self._endereco = endereco
        self._cliente = cliente

    @property
    def tipo(self):
        return self._tipo

    @property
    def contato(self):
        return self._contato
