from typing import List
from Pessoa import Pessoa
from datetime import date
from Beneficiario import Beneficiario
from Corretor import Corretor
from Apolice import Apolice


class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco, contato,
                       beneficiarios: List[Beneficiario], corretor: List[Corretor], apolices: List[Apolice]):

        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._beneficiarios = beneficiarios
        self._corretor = corretor
        self._apolices = apolices

    def __str__(self):
        lista = []
        for x in self._beneficiarios:
            lista += [x._primeiro_nome]
        return f"{lista}"

    def calcula_premio(self):
        return sum(x._valor_premio for x in self._apolices)