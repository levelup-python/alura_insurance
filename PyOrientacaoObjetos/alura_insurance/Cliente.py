class Cliente:
    def __init__(self, nome, sobrenome, cpf, rg, data_nascimento):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._rg = rg
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf

    @property
    def rg(self):
        return self._rg

    @property
    def data_nascimento(self):
        return self._data_nascimento
