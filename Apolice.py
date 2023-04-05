from enum import Enum
from datetime import date


class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4

class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado, corretor,
                 vig, dt_criacao: date, status):
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._valor_benef = valor_benef
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        self._dt_criacao = dt_criacao
        self._status = status