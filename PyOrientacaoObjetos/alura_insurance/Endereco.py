class Endereco:
    def __init__(self, rua: str, numero, complemento, cep, estado, cidade):
        self._rua = rua
        self._numero = numero
        self._complemento = complemento
        self._cep = cep
        self._estado = estado
        self._cidade = cidade
        self.__set_rua(rua)
        self.__set_numero(numero)
        self.__set_cep(cep)
        self.__set_estado(estado)
        self.__set_cidade(cidade)

    @property
    def rua(self):
        return self.__rua

    def __set_rua(self, value):
        if value is None:
            raise ValueError("O rua não pode ser nulo", value)

        self.__rua = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if value is None:
            raise ValueError("O numero não pode ser nulo", value)

        self.__numero = value

    @property
    def cep(self):
        return self.__cep

    def __set_cep(self, value):
        if value is None:
            raise ValueError("O cep não pode ser nulo", value)

        self.__cep = value

    @property
    def cidade(self):
        return self.__cidade

    def __set_cidade(self, value):
        if value is None:
            raise ValueError("O cidade não pode ser nulo", value)

        self.__cidade = value

    @property
    def estado(self):
        return self.__estado

    def __set_estado(self, value):
        if value is None:
            raise ValueError("O estado não pode ser nulo", value)
        if len(value) != 2:
            raise ValueError("estado precisa ter um formato valido", value)

        self.__estado = value


endereco1 = Endereco('rah gyg', '76', 'ap 56', '234873856', 'SP', 'dorhe')
