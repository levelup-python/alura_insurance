class Apolice:
    def __init__(self, nome, sobrenome, cadastro_susep, celular, telefone_residencial, telefone_comercial, email, apolices):
        self._nome = nome
        self._sobrenome = sobrenome
        self.cadastro_susep = cadastro_susep
        self._celular = celular
        self._telefone_residencial = telefone_residencial
        self._telefone_comercial = telefone_comercial
        self._email = email
        self._apolices = apolices

    def nome_completo(self):
        return ("{} {}".format(self._nome.title(), self._sobrenome.title()))

    def __str__(self):
        return ("Nome: {} - Cadastro SUSEP: {}".format(self.nome_completo(), str(self._cadastro_susep)))


    def incluir_apolice(self, apolice):
        self._apolices.append(apolice.__str__())


    def comissao_total(self):
        soma = 0
        for apolice in self._apolices:
            soma += (apolice.valor_premio*0.01)
        return soma

    @property
    def apolices(self):
        return self._apolices


