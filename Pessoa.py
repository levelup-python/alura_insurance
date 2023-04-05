from Endereco import Endereco
from datetime import date

class Pessoa():
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco: Endereco, contato):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._data_nasc = data_nasc
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._contato = contato

    def nome_completo(self):
        return f"{self._primeiro_nome.title()} {self._sobrenome.title()}"

    def __str__(self):
        return f"{self._primeiro_nome} {self._sobrenome} - {self._data_nasc.strftime('%d/%m/%Y')}"

