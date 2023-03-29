class Endereco:

    def __init__(self, rua, numero, bairro, cidade, estado, pais):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__pais = pais

    def endereco_completo(self):
        return ({"Rua":self.__rua, "Numero": self.__numero, "Bairro": self.__bairro, "Cidade": self.__cidade, "Estado": self.__estado, "Pais": self.__pais})
        
