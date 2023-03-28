from typing import List

from Apolice import Apolice
from Contato import Contato


class Corretor:
    def __init__(
        self, nome_corretor, sobrenome_corretor, numero_susep, apolice=List[
            Apolice], contato=Contato
    ):
        self.nome_corretor = nome_corretor
        self.sobrenome_corretor = sobrenome_corretor
        self.numero_susep = numero_susep
        self.apolice = apolice
        self.contato = contato
