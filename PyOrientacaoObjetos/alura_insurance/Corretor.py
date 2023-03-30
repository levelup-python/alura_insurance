from typing import List

from Apolice import Apolice
from Contato import Contato


class Corretor:
    def __init__(
        self, nome_corretor, sobrenome_corretor, numero_susep, comissao_total, apolices=List[
            Apolice], contato=Contato):
        self._nome_corretor = nome_corretor
        self._sobrenome_corretor = sobrenome_corretor
        self._numero_susep = numero_susep
        self._apolices = apolices
        self._contato = contato
        self.comissao_total = comissao_total

    def calcular_comissao_total(self, apolices):
        for apolice in apolices:
            self.comissao_total += apolice.comissao

    @property
    def nome_corretor(self):
        return self._nome_corretor

    @property
    def sobrenome_corretor(self):
        return self._sobrenome_corretor

    @property
    def numero_susep(self):
        return self._numero_susep

    @property
    def contato(self):
        return self._contato
