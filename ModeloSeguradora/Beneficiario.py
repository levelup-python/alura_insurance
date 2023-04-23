from enum import Enum
from ModeloSeguradora.Beneficiario import *
import datetime

class TipoBeneficiario(Enum):
    PAI = 1
    MAE = 2
    FILHOS = 3
    OUTROS = 4
class Beneficiario:
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = datetime.date(int(data_nascimento[6:11]), int(data_nascimento[3:5]),
                                              int(data_nascimento[0:2]))
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._contato = contato

    @property
    def tipo(self):
        return self._tipo.name

    def __str__(self):
        return (super().__str__())
