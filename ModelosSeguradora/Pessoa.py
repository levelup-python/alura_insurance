import datetime
import re
import ModelosSeguradora.Valida

class Pessoa:
    
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg):
        self._nome = ModelosSeguradora.Valida.ValidaNome(nome)
        self._sobrenome = ModelosSeguradora.Valida.ValidaSobrenome(sobrenome)
        self._data_nascimento = ModelosSeguradora.Valida.ValidaDataNascimento(data_nascimento)
        self._cpf = ModelosSeguradora.Valida.ValidaCPF(cpf)
        self._rg = ModelosSeguradora.Valida.ValidaVazioNulo(rg, "rg")

    def nome_completo(self):
        return ("{} {}".format(self._nome.title(), self._sobrenome.title()))
    
    def __str__(self):
        return ("Nome: {} - Data de Nascimento: {} - CPF: {} - RG: {}".format(self.nome_completo(), self._data_nascimento, self._cpf, self._rg))