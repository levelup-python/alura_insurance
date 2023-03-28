class Segurado:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios, apolices):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__contato = contato
        self.__beneficiarios = beneficiarios
        self.__apolices = apolices

    def nome_completo(self): 
       return ("{} {}".format(self.__nome.title(), self.__sobrenome.title()))
    
    def premio_total(self):
        soma = 0
        for apolice in self.__apolices:
            soma += apolice.valor_premio 

        return soma
    
    def beneficio_total(self):
        soma = 0
        for apolice in self.__apolices:
            soma += apolice.valor_beneficio 
            
        return soma