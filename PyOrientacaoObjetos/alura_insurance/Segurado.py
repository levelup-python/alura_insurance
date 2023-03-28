
from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente
from Beneficiario import Beneficiario


class Segurado:
    def __init__(self, cliente=Cliente, endereco=Endereco, contato=Contato,
                 beneficiario=Beneficiario):
        self.endereco = endereco
        self.contato = contato
        self.cliente = cliente
        self.beneficiario = beneficiario
