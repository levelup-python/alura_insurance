<<<<<<< HEAD
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
=======
from Pessoa import Pessoa
from typing import List
from Beneficiario import Beneficiario
from Corretor import Corretor
from datetime import date
from Endereco import Endereco
from Contato import Contato

class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios: List[Beneficiario], corretor: List[Corretor], apolice):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._beneficiarios = beneficiarios
        if len(self._beneficiarios) > 10:
            return print("Rever os beneficiários")
        
        self._corretor = corretor
        self._apolice = apolice
        
    def __str__(self):
        lista = [str(p) for p in self._beneficiarios]
        return f"{lista}"
    
endereco1 = Endereco("Merces", "43", "casa", "123", "Rio de Janeiro", "RJ")
endereco2 = Endereco("Tres Rios", "172", "casa", "22745160", "Rio de janeiro", "RJ")
Contato1 = Contato("123","123","123","erikagascao@gmail.com")
benef1 = Beneficiario("Erika", "Gascao", date(2000, 1, 1), "112.367.805-97", "798", endereco1, Contato1, "filha")
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "112.367.805-97", "9878",endereco2, Contato1, "esposa")
corret1 = Corretor("Paloma", "Ferraz", Contato1, "999", "774")
seg1 = Segurado ("Diego", "Guerrieri", date(1987,11,30), "112.367.805-97", "1254877", endereco2, Contato1, [benef1, benef2], corret1, "apol1")


>>>>>>> a4403410edb3e7e5638198a8eb857276565068c7
