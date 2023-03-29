from ModelosSeguradora.Pessoa import *

class Segurado(Pessoa):

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios, apolices):
        super().__init__(nome, sobrenome, data_nascimento, cpf, rg)
        self._endereco = endereco
        self._contato = contato
        self._beneficiarios = beneficiarios
        self._apolices = apolices

    def nome_completo(self): 
       return ("{} {}".format(self._nome.title(), self._sobrenome.title()))
    
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