from Pessoa import Pessoa
<<<<<<< HEAD
from datetime import date

class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo

=======

class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo

    def __repr__(self):
        return self.__str__()
>>>>>>> a4403410edb3e7e5638198a8eb857276565068c7
