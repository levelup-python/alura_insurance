import ModelosSeguradora.Valida

class Corretor:

    def __init__(self, nome, sobrenome, cadastro_susep, contato):
        self._nome = ModelosSeguradora.Valida.valida_nome(nome)
        self._sobrenome = ModelosSeguradora.Valida.valida_sobrenome(sobrenome)
        self._cadastro_susep = ModelosSeguradora.Valida.valida_cadastro_susep(cadastro_susep)
        self._contato = contato
        self._apolices = []



    def nome_completo(self): 
       return ("{} {}".format(self._nome.title(), self._sobrenome.title()))
    
    def __str__(self):
        return ("Nome: {} - Cadastro SUSEP: {}".format(self.nome_completo(), str(self._cadastro_susep)) )
    
    def comissao_total(self):
        soma = 0
        for apolice in self._apolices:
            soma += (apolice.valor_premio*0.01) 
        return soma
    
    def incluir_apolice(self, apolice):
        self._apolices.append(apolice.__str__()) 
    
    @property
    def apolices(self):
        return self._apolices
    