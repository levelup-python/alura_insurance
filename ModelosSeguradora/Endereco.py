import ModelosSeguradora.Valida

class Endereco:

    def __init__(self, rua, numero, complemento, bairro, cidade, estado, pais):
        self._rua = ModelosSeguradora.Valida.ValidaVazioNulo(rua, "rua")
        self._numero = ModelosSeguradora.Valida.ValidaVazioNulo(numero, "numero")
        self._complemento = complemento
        self._bairro = ModelosSeguradora.Valida.ValidaVazioNulo(bairro, "bairro")
        self._cidade = ModelosSeguradora.Valida.ValidaVazioNulo(cidade, "cidade")
        self._estado = estado
        self._pais = ModelosSeguradora.Valida.ValidaVazioNulo(pais, "pais")

    def endereco_completo(self):
        return ({"Rua":self._rua, "Numero": self._numero, "Complemento": self._complemento, "Bairro": self._bairro, "Cidade": self._cidade, "Estado": self._estado, "Pais": self._pais})
        
