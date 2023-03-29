class Endereco:
    def __init__(self, rua, numero, complemento, cep, estado, cidade):
        self._rua = rua
        self._numero = numero
        self._complemento = complemento
        self._cep = cep
        self._estado = estado
        self._cidade = cidade

    @property
    def rua(self):
        return self._rua

    @property
    def numero(self):
        return self._numero

    @property
    def complemento(self):
        return self._complemento

    @property
    def cep(self):
        return self._cep

    @property
    def estado(self):
        return self._estado

    @property
    def cidade(self):
        return self._cidade
