class Corretor:
    def __init__(self, primeiro_nome, sobrenome, numero_susep, contato):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.numero_susep = numero_susep
        self.apolices = []
        self.contato = contato

    def adicionar_apolice(self, apolice):
        self.apolices.append(apolice)

    def __str__(self):
        return f"Corretor: {self.primeiro_nome} {self.sobrenome}\n" \
               f"Número SUSEP: {self.numero_susep}\n" \
               f"Contato: {self.contato}"


class Segurado:
    def __init__(self, nome, cpf, contato):
        self.nome = nome
        self.cpf = cpf
        self.apolices = []
        self.contato = contato

    def adicionar_apolice(self, apolice):
        self.apolices.append(apolice)

    def __str__(self):
        return f"Segurado: {self.nome}\n" \
               f"CPF: {self.cpf}\n" \
               f"Contato: {self.contato}"


class Apolice:
    def __init__(self, numero, tipo, valor_premio, segurado, corretor, vigencia, data_criacao, status):
        self.numero = numero
        self.tipo = tipo
        self.valor_premio = valor_premio
        self.segurado = segurado
        self.corretor = corretor
        self.vigencia = vigencia
        self.data_criacao = data_criacao
        self.status = status
        segurado.adicionar_apolice(self)
        corretor.adicionar_apolice(self)

    def __str__(self):
        return f"Apolice:\n" \
               f"Número: {self.numero}\n" \
               f"Tipo: {self.tipo}\n" \
               f"Valor do Prêmio: {self.valor_premio}\n" \
               f"{self.segurado}\n" \
               f"{self.corretor}\n" \
               f"Vigência: {self.vigencia}\n" \
               f"Data de Criação: {self.data_criacao}\n" \
               f"Status: {self.status}"


corretor = Corretor("João", "Silva", "123456", "joao.silva@exemplo.com")
segurado = Segurado("Maria", "12345678910", "maria@exemplo.com")
apolice = Apolice(1, "VIDA", 1000.00, segurado, corretor, "01/01/2023", "01/01/2022", "ATIVA")
print(apolice.__str__())
