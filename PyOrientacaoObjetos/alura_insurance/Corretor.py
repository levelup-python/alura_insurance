from typing import List
from Apolice import Apolice
from Contato import Contato


class Corretor:
    def __init__(
            self, nome_corretor, sobrenome_corretor, numero_susep, apolices=List[Apolice], contato=Contato):
        self._nome_corretor = nome_corretor
        self._sobrenome_corretor = sobrenome_corretor
        self._numero_susep = numero_susep
        self._apolices = apolices
        self._contato = contato
        self.comissao_total = self.calcular_comissao_total()

    def __getitem__(self, item):
        return self._apolices[item]

    def calcular_comissao_total(self):
        comissao_total = 0
        for apolice in self._apolices:
            comissao_total += apolice.comissao
        return comissao_total

    @property
    def nome_corretor(self):
        return self._nome_corretor

    @property
    def sobrenome_corretor(self):
        return self._sobrenome_corretor

    @property
    def apolices(self):
        return self._apolices

    @property
    def contato(self):
        return self._contato

    # @property
    # def comissao_total(self):
    #     return self._comissao_total


apolice1 = Apolice('238575', 5000, 'segurado1', '23/04/2020',
                   '22/04/1999', 'VIDA', 'ativo')
apolice2 = Apolice('000000', 5000, 'segurado1', '00/00/2020',
                   '22/04/1999', 'VIAGEM', 'ativo')

contato_corretor = Contato(
    '21 9875 9845', '21 2345 6778', '21 4567 2324', 'antonio@gmail.com')
Corretor1 = Corretor('Antonio', 'goncalves', '234567', [
                     apolice1, apolice2], contato_corretor)
# Corretor1._apolices

# len(Corretor1._apolices)

# Corretor1._apolices[0].comissao

# Corretor1.comissao_total
