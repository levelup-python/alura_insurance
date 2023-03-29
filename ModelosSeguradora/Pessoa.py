class Pessoa:
    
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._rg = rg

    def nome_completo(self):
        return ("{} {}".format(self._nome.title(), self._sobrenome.title()))