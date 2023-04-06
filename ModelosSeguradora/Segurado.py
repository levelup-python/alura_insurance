from ModelosSeguradora.Pessoa import *
import datetime
from dateutil.relativedelta import relativedelta

class Segurado(Pessoa):

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios):
        super().__init__(nome, sobrenome, data_nascimento, cpf, rg)
        self.__set_data_nascimento(data_nascimento)
        self._endereco = endereco
        self._contato = contato
        self.__set_beneficiarios(beneficiarios)
        self._apolices = []
    
    def __str__(self):
        return (super().__str__())
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    def __set_data_nascimento(self, value):

        value = datetime.date(int(value[6:11]), int(value[3:5]),int(value[0:2]))
        data_atual = datetime.date.today()
        idade = relativedelta(data_atual, value).years
        
        if idade < 18:
            raise ValueError("Segurado precisa ter pelo menos 18 anos")
    
        self._data_nascimento = value

    @property
    def beneficiarios(self):
        return self.__beneficiarios 
    
    def __set_beneficiarios(self, value):

        if len(value) > 10:
            raise ValueError("Não pode ter mais que 10 beneficiários")
        
        self.__beneficiarios = value


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
    