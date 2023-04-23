import datetime
from enum import Enum

class StatusApolice(Enum):
    ATIVA = 1
    LIQUIDADA = 2
    CANCELADA = 3
    EM_SINISTRO = 4
class TipoApolice(Enum):
    VIDA = 1

class Apolice:
    def __init__(self, numero_identificador, tipo, valor_premio, valor_beneficio, segurado, corretor, inicio_vigencia, fim_vigencia, data_criacao, status):
        self._numero_identificador = numero_identificador
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._valor_beneficio = valor_beneficio
        self._segurado = segurado
        self._corretor = corretor
        self._inicio_vigencia = datetime.date(int(inicio_vigencia[6:11]), int(inicio_vigencia[3:5]),
                                              int(inicio_vigencia[0:2]))
        self._fim_vigencia = datetime.date(int(fim_vigencia[6:11]), int(fim_vigencia[3:5]),
                                              int(fim_vigencia[0:2]))
        self.data_criacao = datetime.date(int(data_criacao[6:11]), int(data_criacao[3:5]),
                                              int(data_criacao[0:2]))
        self._status = status

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

    def __str__(self):
        return ("Apólice: {} - Status: {} - Tipo: {} - Segurado: {} - Corretor: {} - Prêmio: {} - Benefício: {}".
                format(str(self.numero_identificador), str(self.status), str(self.tipo), str(self._segurado.nome_completo()),
                       str(self._corretor.nome_completo()), str(self.valor_premio), str(self.valor_beneficio)))