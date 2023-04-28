from enum import Enum
from enum import auto
import datetime
import ModelosSeguradora.Valida

class StatusApolice(Enum):
    ATIVA = auto() 
    LIQUIDADA = auto() 
    CANCELADA = auto()
    EM_SINISTRO = auto()

class TipoApolice(Enum):
    VIDA = auto()
    CARRO = auto()
    CASA = auto()
    VIAGEM = auto()

class Apolice:

    def __init__(self, numero, valor_premio, valor_beneficio, segurado, corretor, inicio_vigencia, fim_vigencia, data_criacao, status, tipo):
        self._numero = numero
        self._valor_beneficio = ModelosSeguradora.Valida.valida_valor_maior_zero(valor_beneficio, valor_beneficio)
        self._valor_premio = ModelosSeguradora.Valida.valida_valor_maior_zero(valor_premio, valor_premio)
        self._segurado = segurado
        self._corretor = corretor
        self._inicio_vigencia = ModelosSeguradora.Valida.valida_data_futura(inicio_vigencia, inicio_vigencia)
        self._fim_vigencia = ModelosSeguradora.Valida.valida_data_futura(fim_vigencia, fim_vigencia)
        self._data_criacao = ModelosSeguradora.Valida.valida_data_passado(data_criacao)
        self._status = status
        self._tipo = tipo

    @property
    def valor_premio(self):
        return self._valor_premio
    
    @property
    def valor_beneficio(self):
        return self._valor_beneficio
    
    @property
    def status(self):
        return self._status.name
    
    @property
    def tipo(self):
        return self._tipo.name
    
