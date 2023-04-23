import datetime

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
        return ("Nome: {} - Data de Nascimento: {} - CPF: {} - RG: {}".format(self.nome_completo(),self._data_nascimento,self._cpf, self._rg))

class Endereco:
    def __init__(self, rua, numero, complemento, cep, estado, cidade, pais):
        self._rua = rua
        self.numero = numero
        self._complemento = complemento
        self._cep = cep
        self._estado = estado
        self._cidade = cidade
        self.pais = pais

    def endereco_completo(self):
        return ({"Rua": self._rua, "Numero": self._numero, "Bairro": self._bairro, "Cidade": self._cidade,
                 "Estado": self._estado, "Pais": self._pais})


class Contato:
    def __init__(self, celular, telefone_residencial, telefone_comercial, email):
        self._celular = celular
        self._telefone_residencial = telefone_residencial
        self._telefone_comercial = telefone_comercial
        self._email = email

    def contato(self):
        return ({"Celular": self._celular, "Telefone Residencial": self._telefone_residencial,
                 "Telefone Comercial": self._telefone_comercial, "Email": self._email})
