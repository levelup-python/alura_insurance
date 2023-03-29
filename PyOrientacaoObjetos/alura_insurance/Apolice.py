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

    @property
    def numero(self):
        return self._numero

    @property
    def valor_do_premio(self):
        return self._valor_do_premio

    @property
    def segurado(self):
        return self._segurado

    @property
    def corretor(self):
        return self._corretor

    @property
    def fim_vigencia(self):
        return self._fim_vigencia

    @property
    def criacao_apolice(self):
        return self._criacao_apolice

    @property
    def status(self):
        return self._status

    @staticmethod
    def tipo_apolice():
        return "VIDA"


Apolice.tipo_apolice()
