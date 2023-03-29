from typing import List

from Apolice import Apolice
from Contato import Contato


class Corretor:
    def __init__(
        self, nome_corretor, sobrenome_corretor, numero_susep, apolice=List[
            Apolice], contato=Contato
    ):
        self._nome_corretor = nome_corretor
        self._sobrenome_corretor = sobrenome_corretor
        self._numero_susep = numero_susep
        self._apolice = apolice
        self._contato = contato

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
    def apolice(self):
        return self._apolice

    @property
    def contato(self):
        return self._contato
