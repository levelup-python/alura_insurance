import datetime

class Corretor:

    def __init__(self, nome, sobrenome, cadastro_susep, contato):
        self.__set_nome(nome)
        self.__set_sobrenome(sobrenome)
        self.__set_cadastro_susep(cadastro_susep)
        self._contato = contato
        self._apolices = []

    @property
    def nome(self):
        return self.__nome

    def __set_nome(self, value):
        if not isinstance(value, str):
            raise ValueError("O atributo nome deve ser uma string")
        if len(value) < 2:
            raise ValueError("O atributo nome deve conter no mínimo 2 caracteres")
                    
        self.__nome = value

    @property
    def sobrenome(self):
        return self.__sobrenome

    def __set_sobrenome(self, value):
        if not isinstance(value, str):
            raise ValueError("O atributo nome deve ser uma string")
        if len(value) < 2:
            raise ValueError("O atributo nome deve conter no mínimo 2 caracteres")
                    
        self.__sobrenome = value

    @property
    def cadastro_susep(self):
        return self.__cadastro_susep

    def __set_cadastro_susep(self, value):
        inicio_num_susep = '154146'
        if len(value) != 17:
            raise ValueError("O número do cadastro SUSEP deve ter 17 caracteres")
        if value[0:6] != inicio_num_susep:
            raise ValueError("O número do cadastro SUSEP deve iniciar com: ", inicio_num_susep)
                    
        self.__cadastro_susep = value


    def nome_completo(self): 
       return ("{} {}".format(self.nome.title(), self.sobrenome.title()))
    
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
    