from ModelosSeguradora.Apolice import *

def comissao_vida (apolice):
    comissao = (0.005 * apolice.valor_beneficio) + 100
    if apolice.valor_beneficio > 850000:
        comissao += 1000
    return comissao 

def comissao_carro (apolice):
    comissao = (0.0035 * apolice.valor_beneficio) + 75.50
    return comissao

def comissao_casa (apolice):
    comissao = 0.002 * apolice.valor_beneficio
    return comissao

def comissao_viagem (apolice):
    comissao = 200
    return comissao

class CalculadoraComissao:

    def __init__(self, apolices):
        self._apolices = apolices
        self._regra_calculo = {"VIDA": comissao_vida, "CARRO": comissao_carro, "CASA": comissao_casa, "VIAGEM": comissao_viagem}

    def calcula_comissao(self):
        soma = 0
        for apolice in self._apolices:
            soma += self._regra_calculo[apolice.tipo](apolice)
        return soma

