class Corretor:

    def __init__(self, nome, sobrenome, cadastro_susep, apolices, contato):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cadastro_susep = cadastro_susep
        self.__contato = contato
        self.__apolices = apolices
    

    def comissao_total(self):
        soma = 0
        for apolice in self.__apolices:
            soma += (apolice.valor_premio*0.01) 
        return soma