class Beneficiario:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, tipo, endereco, contato):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__tipo = tipo
        self.__endereco = endereco
        self.__contato = contato
    
    
    def nome_completo(self): 
       return ("{} {}".format(self.__nome.title(), self.__sobrenome.title()))
    
