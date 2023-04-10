from enum import Enum
from ModelosSeguradora.Pessoa import *
import datetime
from dateutil.relativedelta import relativedelta

class TipoBeneficiario(Enum):
    PAI = 1
    MÃE = 2
    FILHOS = 3
    OUTROS = 4


class Beneficiario(Pessoa):

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, tipo):
        super().__init__(nome, sobrenome, data_nascimento, cpf, rg)
        self._tipo = tipo
        self._endereco = endereco
        self._contato = contato
    
    @property
    def tipo(self):
        return self._tipo.name
    
    def __str__(self):
        return (super().__str__())

