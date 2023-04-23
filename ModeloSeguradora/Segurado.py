class Segurado:
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = datetime.date(int(data_nascimento[6:11]), int(data_nascimento[3:5]),
                                              int(data_nascimento[0:2]))
        self._cpf = cpf
        self._rg = rg

    def nome_completo(self):
        return ("{} {}".format(self._nome.title(), self._sobrenome.title()))

    def __str__(self):
        return (
            "Nome: {} - Data de Nascimento: {} - CPF: {} - RG: {}".format(self.nome_completo(), self._data_nascimento,
                                                                          self._cpf, self._rg))
