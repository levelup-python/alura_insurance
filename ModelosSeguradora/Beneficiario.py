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
        self.__set_data_nascimento(data_nascimento)
        self._tipo = tipo
        self._endereco = endereco
        self._contato = contato
    
    @property
    def tipo(self):
        return self._tipo.name
    
    def __str__(self):
        return (super().__str__())

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    def __set_data_nascimento(self, value):

        value = datetime.date(int(value[6:11]), int(value[3:5]),int(value[0:2]))
        data_atual = datetime.date.today()
        
        if value > data_atual:
            raise ValueError("Data de nascimento não pode ser uma data futura")
    
        self._data_nascimento = value
    
