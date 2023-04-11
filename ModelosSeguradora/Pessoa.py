import ModelosSeguradora.Valida

class Pessoa:
    
    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg):
        self._nome = ModelosSeguradora.Valida.valida_nome(nome)
        self._sobrenome = ModelosSeguradora.Valida.valida_sobrenome(sobrenome)
        self._data_nascimento = ModelosSeguradora.Valida.valida_data_nascimento(data_nascimento)
        self._cpf = ModelosSeguradora.Valida.valida_cpf(cpf)
        self._rg = ModelosSeguradora.Valida.valida_vazio_ou_nulo(rg, "rg")

    def nome_completo(self):
        return ("{} {}".format(self._nome.title(), self._sobrenome.title()))
    
    def __str__(self):
        return ("Nome: {} - Data de Nascimento: {} - CPF: {} - RG: {}".format(self.nome_completo(), self._data_nascimento, self._cpf, self._rg))