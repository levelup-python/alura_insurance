from ModelosSeguradora.Pessoa import *
import ModelosSeguradora.Valida

class Segurado(Pessoa):

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios):
        super().__init__(nome, sobrenome, data_nascimento, cpf, rg)
        self._data_nascimento = ModelosSeguradora.Valida.valida_maioridade(data_nascimento)
        self._endereco = endereco
        self._contato = contato
        self._beneficiarios = ModelosSeguradora.Valida.valida_qtd_beneficiarios(beneficiarios)
        self._apolices = []
    
    def __str__(self):
        return (super().__str__())


    def premio_total(self):
        soma = 0
        for apolice in self._apolices:
            soma += apolice.valor_premio 

        return soma
    
    def beneficio_total(self):
        soma = 0
        for apolice in self._apolices:
            soma += apolice.valor_beneficio 
            
        return soma
    
    def incluir_apolice(self, apolice):
        self._apolices.append(apolice.__str__()) 
    
    @property
    def apolices(self):
        return self._apolices
    