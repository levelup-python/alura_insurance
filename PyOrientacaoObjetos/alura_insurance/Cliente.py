from datetime import date


class Cliente:
    def __init__(self, nome: str, sobrenome: str, cpf: str, rg: str, data_nascimento: date):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._rg = rg
        self._data_nascimento = data_nascimento
        self.nome_completo = self.calcular_nome_completo

    def calcular_nome_completo(self):
        print(f"{self.nome} {self.sobrenome}")

    @ property
    def nome(self):
        return self._nome

    @ property
    def sobrenome(self):
        return self._sobrenome


segurado1 = Cliente('João', 'Silva', '111.111.111-11', '2222222', '01/01/1980')
segurado1.nome_completo()
