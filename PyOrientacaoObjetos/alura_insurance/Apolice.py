class Apolice:

    def __init__(self, numero_susep, valor_do_premio, segurado,
                 fim_vigencia, inicio_vigencia, tipo, status):
        self._numero_susep = numero_susep
        self._valor_do_premio = valor_do_premio
        self._segurado = segurado
        self._fim_vigencia = fim_vigencia
        self._inicio_vigencia = inicio_vigencia
        self.tipo = tipo
        self.comissao = self.calcular_comissao()
        self.status = status

    @property
    def valor_do_premio(self):
        return self._valor_do_premio

    def calcular_comissao(self):
        if self.tipo == 'VIDA':
            comissao = 0.05 * self.valor_do_premio + 100 + \
                (1000 if self.valor_do_premio > 10000 else 0)
        elif self.tipo == 'CARRO':
            comissao = 75.50 + 0.0035 * self.valor_do_premio
        elif self.tipo == 'CASA':
            comissao = 0.002 * self.valor_do_premio
        elif self.tipo == 'VIAGEM':
            comissao = 200
        else:
            comissao = 0
        return comissao
