class Corretor:
    def __init__(self, primeiro_nome, sobrenome, numero_susep, contato):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__numero_susep = numero_susep
        self.__apolices = []
        self.__contato = contato

    def adicionar_apolice(self, apolice):
        self.__apolices.append(apolice)

    def get_nome_completo(self):
        return f"{self.__primeiro_nome} {self.__sobrenome}"

    def __str__(self):
        return f"Corretor: {self.get_nome_completo()}\n" \
               f"Número SUSEP: {self.__numero_susep}\n" \
               f"Contato: {self.__contato}"


class Segurado:
    def __init__(self, nome, cpf, contato):
        self.__nome = nome
        self.__cpf = cpf
        self.__apolices = []
        self.__contato = contato

    def adicionar_apolice(self, apolice):
        self.__apolices.append(apolice)

    def __str__(self):
        return f"Segurado: {self.__nome}\n" \
               f"CPF: {self.__cpf}\n" \
               f"Contato: {self.__contato}"


class Apolice:
    def __init__(self, numero, tipo, valor_premio, segurado, corretor, vigencia, data_criacao, status):
        self.__numero = numero
        self.__tipo = tipo
        self.__valor_premio = valor_premio
        self.__segurado = segurado
        self.__corretor = corretor
        self.__vigencia = vigencia
        self.__data_criacao = data_criacao
        self.__status = status
        segurado.adicionar_apolice(self)
        corretor.adicionar_apolice(self)

    def __str__(self):
        return f"Apolice:\n" \
               f"Número: {self.__numero}\n" \
               f"Tipo: {self.__tipo}\n" \
               f"Valor do Prêmio: {self.__valor_premio}\n" \
               f"{self.__segurado}\n" \
               f"{self.__corretor}\n" \
               f"Vigência: {self.__vigencia}\n" \
               f"Data de Criação: {self.__data_criacao}\n" \
               f"Status: {self.__status}"


def relatorio_geral(apolices):
    total_premios = 0
    total_apolices = len(apolices)
    for apolice in apolices:
        total_premios += apolice._Apolice__valor_premio
    print(f"Total de apólices: {total_apolices}")
    print(f"Total de prêmios: {total_premios}")



class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade