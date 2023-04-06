from enum import Enum
<<<<<<< HEAD
from datetime import date

=======
from Segurado import Segurado
from datetime import date
from Corretor import Corretor
>>>>>>> a4403410edb3e7e5638198a8eb857276565068c7

class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4
<<<<<<< HEAD

class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado, corretor,
                 vig, dt_criacao: date, status):
=======
        
class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado: Segurado, corretor: Corretor, vig: date, dt_criacao: date, status):
>>>>>>> a4403410edb3e7e5638198a8eb857276565068c7
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._valor_benef = valor_benef
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        self._dt_criacao = dt_criacao
<<<<<<< HEAD
        self._status = status
=======
        self._status = status
    
    def __str__(self):
        return f"{self._numero} - {self._vig.strftime('%d/%m/%Y')} - {self._dt_criacao.strftime('%d/%m/%Y')}"
>>>>>>> a4403410edb3e7e5638198a8eb857276565068c7
