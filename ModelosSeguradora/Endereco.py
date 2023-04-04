class Endereco:

    def __init__(self, rua, numero, bairro, cidade, estado, pais):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._pais = pais

    def endereco_completo(self):
        return ({"Rua":self._rua, "Numero": self._numero, "Bairro": self._bairro, "Cidade": self._cidade, "Estado": self._estado, "Pais": self._pais})
        
