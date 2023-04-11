import ModelosSeguradora.Valida

class Endereco:

    def __init__(self, rua, numero, complemento, bairro, cidade, estado, pais):
        self._rua = ModelosSeguradora.Valida.valida_vazio_ou_nulo(rua, "rua")
        self._numero = ModelosSeguradora.Valida.valida_vazio_ou_nulo(numero, "numero")
        self._complemento = complemento
        self._bairro = ModelosSeguradora.Valida.valida_vazio_ou_nulo(bairro, "bairro")
        self._cidade = ModelosSeguradora.Valida.valida_vazio_ou_nulo(cidade, "cidade")
        self._estado = ModelosSeguradora.Valida.valida_estado(estado)
        self._pais = ModelosSeguradora.Valida.valida_vazio_ou_nulo(pais, "pais")

    def endereco_completo(self):
        return ({"Rua":self._rua, "Numero": self._numero, "Complemento": self._complemento, "Bairro": self._bairro, "Cidade": self._cidade, "Estado": self._estado, "Pais": self._pais})
        
