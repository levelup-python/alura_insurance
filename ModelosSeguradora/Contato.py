class Contato:

    def __init__(self, celular, telefone_residencial, telefone_comercial, email):
        self.__celular = celular
        self.__telefone_comercial = telefone_comercial
        self.__telefone_residencial = telefone_residencial
        self.__email = email

    def contato_completo(self):
        return ({"Celular": self.__celular, "Telefone_Comercial": self.__telefone_comercial, "Telefone_Residencial": self.__telefone_residencial, "Email": self.__email})