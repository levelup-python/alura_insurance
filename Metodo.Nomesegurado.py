class Segurado:
    def __init__(self, nome, cpf, contato):
        self.__nome = nome
        self.idade = None
        self.__apolices = []
        self.contato = contato
        self.cpf = cpf

    def adicionar_apolice(self, apolice):
        self.__apolices.append(apolice)

    def pegar_nome_completo(self):
        return self.__nome

    def __str__(self):
        return f"Segurado: {self.__nome}\n" \
               f"CPF: {self.cpf}\n" \
               f"Idade: {self.idade}\n" \
               f"Contato: {self.contato}\n" \
               f"Apolices: {[apolice.numero for apolice in self.__apolices]}"


segurado = Segurado("João da Silva", "123.456.789-10", "joao@gmail.com")
print(segurado.pegar_nome_completo())  # Deve imprimir "João da Silva"
