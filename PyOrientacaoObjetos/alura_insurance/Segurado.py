
from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente
from Beneficiario import Beneficiario
from Apolice import Apolice


class Segurado:
    def __init__(self, cliente=Cliente, endereco=Endereco, contato=Contato,
                 beneficiario=Beneficiario, apolice=Apolice):
        self.endereco = endereco
        self.contato = contato
        self.cliente = cliente
        self.beneficiario = beneficiario
        self.apolice = apolice
