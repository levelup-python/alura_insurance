class Apolice:

    def __init__(self, numero, valor_premio, valor_beneficio, segurado, corretor, inicio_vigencia, fim_vigencia, data_criacao, status, tipo = 'VIDA'):
        self.__numero = numero
        self.__valor_beneficio = valor_beneficio
        self.__valor_premio = valor_premio
        self.__segurado = segurado
        self.__corretor = corretor
        self.__inicio_vigencia = inicio_vigencia
        self.__fim_vigencia = fim_vigencia
        self.__data_criacao = data_criacao
        self.__status = status
        self.__tipo = tipo

    @property
    def valor_premio(self):
        return self.__valor_premio
    
    @property
    def valor_beneficio(self):
        return self.__valor_beneficio
    
