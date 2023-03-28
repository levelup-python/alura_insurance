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
