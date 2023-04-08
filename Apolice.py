from enum import Enum
from Segurado import Segurado
from datetime import date
from Corretor import Corretor

class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4

class StatusApolice(Enum):
    Ativa = 1
    Liquidada = 2
    Cancelada = 3
    Em_Sinistro = 4
        
class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado: Segurado, corretor: Corretor, vig: date, dt_criacao: date, status:StatusApolice):
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        if valor_premio < 0:
            raise print(f"Prêmio deve ser maior que zero")
        self._valor_benef = valor_benef
        if valor_benef < 0:
            raise print(f"Benefício deve ser maior que zero")
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        if vig < date.today():
            raise print("data de vigência tem que ser futura")
        self._dt_criacao = dt_criacao
        if dt_criacao >= date.today():
            raise print("data da criação não pode ser futura")
        self._status = status
        try:
            StatusApolice[status]
        except(KeyError):
            raise print("Digite um status válido")

    def __str__(self):
        return f"{self._numero} - {self._vig.strftime('%d/%m/%Y')} - {self._dt_criacao.strftime('%d/%m/%Y')}"

