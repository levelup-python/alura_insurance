from Pessoa import Pessoa
from typing import List
from Beneficiario import Beneficiario
from Corretor import Corretor

class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios: List[Beneficiario], corretor: List[Corretor], apolice):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._beneficiarios = beneficiarios
        self._corretor = corretor
        self._apolice = apolice
        
    def __str__(self):
        lista = [str(p) for p in self._beneficiarios]
        return f"{lista}"