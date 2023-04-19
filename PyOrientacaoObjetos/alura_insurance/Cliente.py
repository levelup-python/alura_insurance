import re
from datetime import date
from dateutil.relativedelta import relativedelta


class Cliente:
    def __init__(self, nome, sobrenome, cpf, rg, data_nascimento: date):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__rg = rg
        self.__data_nascimento = data_nascimento
        self.__set_nome(nome)
        self.__set_sobrenome(sobrenome)
        self.__set_cpf(cpf)
        self.__set_rg(rg)
        self.__set_data_nascimento(data_nascimento)
        self.nome_completo = self.calcular_nome_completo()

    @property
    def nome(self):
        return self.__nome

    def __set_nome(self, value):
        if value is None:
            raise ValueError("O nome não pode ser nulo", value)
        if len(value) < 2:
            raise ValueError(
                "O nome precisa ter no mínimo 2 caracteres", value)

        self.__nome = value

    @property
    def sobrenome(self):
        return self.__sobrenome

    def __set_sobrenome(self, value):
        if value is None:
            raise ValueError("O sobrenome não pode ser nulo", value)
        if len(value) < 2:
            raise ValueError("O sobrenome não pode ter menos de dois", value)

        self.__sobrenome = value

    @property
    def rg(self):
        return self.__rg

    def __set_rg(self, value):
        if value is None:
            raise ValueError("O rg não pode ser nulo", value)

        self.__rg = value

    @property
    def cpf(self):
        return self.__cpf

    def __set_cpf(self, value):
        padrao_cpf = re.compile(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$')
        if not padrao_cpf.match(value):
            raise ValueError(
                "CPF precisa ter o formato correto (ex: 123.456.789-10) ou (12345678910)", value)

        self.__cpf = value

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    def __set_data_nascimento(self, value):

        dt_nasc = date.fromisoformat(value)
        idade = relativedelta(date.today(), dt_nasc).years

        if idade < 18:
            raise ValueError("A idade precisa ser maior do que 18")

    def calcular_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


cliente = Cliente("Ana", "Silva", "123.456.78910", "", "1990-01-01")
cliente.calcular_nome_completo()
