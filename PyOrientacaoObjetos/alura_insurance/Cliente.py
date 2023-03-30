class Cliente:
    def __init__(self, nome, sobrenome, cpf, rg, data_nascimento):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._rg = rg
        self._data_nascimento = data_nascimento

    def calcular_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome
