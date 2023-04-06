import datetime
import re

class Pessoa:
    
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg):
        self.__set_nome(nome)
        self.__set_sobrenome(sobrenome)
        self._data_nascimento = datetime.date(int(data_nascimento[6:11]), int(data_nascimento[3:5]),int(data_nascimento[0:2]))
        self.__set_cpf(cpf)
        self.__set_rg(rg)

    @property
    def nome(self):
        return self.__nome
    

    def __set_nome(self, value):
        if not isinstance(value, str):
            raise ValueError("O atributo nome deve ser uma string")
        if len(value) < 2:
            raise ValueError("O atributo nome deve conter no mínimo 2 caracteres")
                    
        self.__nome = value

    @property
    def sobrenome(self):
        return self.__sobrenome

    def __set_sobrenome(self, value):
        if not isinstance(value, str):
            raise ValueError("O atributo nome deve ser uma string")
        if len(value) < 2:
            raise ValueError("O atributo nome deve conter no mínimo 2 caracteres")
                    
        self.__sobrenome = value

    @property
    def rg(self):
        return self.__rg

    def __set_rg(self, value):
        if value == None or len(value) == 0:
            raise ValueError("O atributo não pode ser nulo")
        self.__rg = value

    @property
    def cpf(self):
        return self.__cpf

    def __set_cpf(self, value):
        padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        valida = re.match(padrao, value)

        if valida == None:
            raise ValueError("CPF não está na formatação correta")
        self.__cpf = value

    def nome_completo(self):
        return ("{} {}".format(self.nome.title(), self.sobrenome.title()))
    
    def __str__(self):
        return ("Nome: {} - Data de Nascimento: {} - CPF: {} - RG: {}".format(self.nome_completo(), self._data_nascimento, self._cpf, self._rg))