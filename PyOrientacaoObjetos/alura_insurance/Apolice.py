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
        self.numero = numero
        self.valor_do_premio = valor_do_premio
        self.segurado = segurado
        self.corretor = corretor
        self.fim_vigencia = fim_vigencia
        self.criacao_apolice = criacao_apolice
        self.status = status

    @staticmethod
    def tipo_apolice():
        return {"VIDA"}
