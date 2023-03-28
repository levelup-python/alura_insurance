from enum import Enum


class Status(Enum):
    ATIVA = 1
    LIQUIDADA = 2
    CANCELADA = 3
    EM_SINISTRO = 4


class Apolice:
    def __init__(self, numero, valor_do_premio,
                 segurado, corretor, fim_vigencia, criacao_apolice, status: Status,
                 ):
        self._numero = numero
        self._valor_do_premio = valor_do_premio
        self._segurado = segurado
        self._corretor = corretor
        self._fim_vigencia = fim_vigencia
        self._criacao_apolice = criacao_apolice
        self._status = status

    @staticmethod
    def tipo_apolice():
        return {"VIDA"}
