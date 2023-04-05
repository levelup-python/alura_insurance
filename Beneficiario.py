from Pessoa import Pessoa
from datetime import date

class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo

