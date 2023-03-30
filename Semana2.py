class segurado():

    def __init__(self, primeiro_nome, sobrenome, dt_nasc, cpf, rg, endereco, contato, beneficiarios):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__dt_nasc = dt_nasc
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__contato = contato
        self.__beneficiarios = beneficiarios
        self.premio_total = 0

    @property
    def primeiro_nome(self):
        return self.__primeiro.title()

    @property
    def sobrenome(self):
        return self.__sobrenome.title()

    def nome_completo(self):
        print(f"{self.__primeiro_nome.title()} {self.__sobrenome.title()}")

    def cria_apolice(self, numero, valor_premio):
        self.premio_total += valor_premio

    def total_premio(self):
        print(f" O valor total de prêmio é: R$ {self.premio_total}")


class beneficiario():
    def __init__(self, primeiro_nome, sobrenome, dt_nasc, cpf, rg, tipo, endereco, contato ):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__dt_nasc = dt_nasc
        self.__cpf = cpf
        self.__rg = rg
        self.__tipo = tipo
        self.__endereco = endereco
        self.__contato = contato

class apolice():
    def __init__(self, numero, tipo, valor_premio, valor_benef, segurado, corretor, vig, dt_criacao, status):
        self.__numero = numero
        self.__tipo = tipo
        self.__valor_premio = valor_premio
        self.__valor_benef = valor_benef
        self.__segurado = segurado
        self.__corretor = corretor
        self.__vig = vig
        self.__dt_criacao = dt_criacao
        self.__status = status

class corretor():
    def __init__(self, primeiro_nome, sobrenome, num_susep, apolice, contato, comissao_total):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__num_susep = num_susep
        self.__apolice = apolice
        self.__contato = contato
        self.__comissao_total = 0

    def cria_apolice(self, numero, valor_premio):
        self.comissao_total += valor_premio * 0.01

    def total_comissao(self):
        print(f" O valor total de comissao é: R$ {self.comissao_total}")





