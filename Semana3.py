from typing import List
from enum import Enum
from datetime import date

class Endereco():
    def __init__(self, rua, numero, complemento, cep, estado, cidade):
        self._rua = rua
        self._numero = numero
        self._complemento = complemento
        self._cep = cep
        self._estado = estado
        self._cidade = cidade

    def __str__(self):
        return f"{self._rua} - {self._numero}"


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
        return f"{self._primeiro_nome} {self._sobrenome} {self._data_nasc.strftime('%d/%m/%y')}"

class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4

class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado, corretor,
                 vig, dt_criacao: date, status):
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._valor_benef = valor_benef
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        self._dt_criacao = dt_criacao
        self._status = status

class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo


class Corretor():
    def __init__(self, primeiro_nome, sobrenome, contato, num_susep, apolice):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._contato = contato
        self._num_susep = num_susep
        self._apolice = apolice

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


class Calculadora():

    def __init__(self, apolice: List[Apolice]):
        self._apolice = apolice

    def calcula(self):
        valor = 0
        for i in self._apolice:
            if i._tipo.value == 1:
                valor += 0.005 * i._valor_premio + 100 + (1000 if i._valor_benef > 850000 else 0)
            elif i._tipo.value == 2:
                valor += 0.0035 * i._valor_premio + 75.50
            elif i._tipo.value == 3:
                valor += 0.002 * i._valor_premio
            else:
                valor += 200
        return valor


endereco1 = Endereco("Merces", 43, "casa", "123", "Rio de Janeiro", "RJ")
endereco2 = Endereco("Tres Rios", 172, "casa", "22745160", "Rio de janeiro", "RJ")
benef1 = Beneficiario("Erika", "Gascao", date(1992, 7, 1), "123456", "798", endereco1, "abc", "filha")
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 1), "45679", "9878", endereco2, "hdkhbd", "esposa")
corret1 = Corretor("Paloma", "Ferraz", "002", "999", "774")
apol1= Apolice("123", TipoApolice.Vida, 100.00, 100000.00, "Diego", "Paloma", "15anos", "30/03/2023", "ATIVA")
apol2= Apolice("456", TipoApolice.Vida, 100.00, 100000.00, "Diego", "Paloma", "15anos", "30/03/2023", "ATIVA")
seg1 = Segurado("Diego", "Guerrieri", "30/11/1987", "05878456", "21245", endereco2, "1254877", [benef1, benef2], corret1, [apol1, apol2])

calc1 = Calculadora([apol1, apol2])
calc1.calcula()




