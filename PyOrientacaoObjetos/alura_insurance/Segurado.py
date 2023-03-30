from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente
from Beneficiario import Beneficiario
from Apolice import Apolice
from Corretor import Corretor


class Segurado():

    def __init__(self, cliente=Cliente, endereco=Endereco, contato=Contato,
                 beneficiario=Beneficiario, apolice=Apolice,
                 corretor=Corretor):
        self._cliente = cliente
        self._beneficiario = beneficiario
        self._apolice = apolice
        self._corretor = corretor
        self._endereco = endereco
        self._contato = contato

    @ property
    def contato(self):
        return self._contato

    @ property
    def beneficiario(self):
        return self._beneficiario

    @ property
    def apolice(self):
        return self._apolice
