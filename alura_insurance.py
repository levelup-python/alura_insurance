class Segurado:

    def __init__(self, primeiro_nome, sobrenome, nascimento, cpf, rg,
                 endereco_rua, endereco_numero,endereco_complemento,endereco_cep,
                 endereco_estado, endereco_cidade,
                 contato_celular, contato_telefone, contato_residencial,
                 contato_telefone_comercial,
                 contato_email, beneficiarios,apolices):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__nascimento = nascimento
        self.__rg = rg
        self.__cpf = cpf
        self.__beneficiarios = beneficiarios
        self.__endereco_rua = endereco_rua
        self.__endereco_numero = endereco_numero
        self.__endereco_complemento = endereco_complemento
        self.__endereco_cep = endereco_cep
        self.__endereco_estado = endereco_estado
        self.__endereco_cidade = endereco_cidade
        self.__contato_celular = contato_celular
        self.__contato_telefone = contato_telefone
        self.__contato_residencial = contato_residencial
        self.__contato_telefone_comercial = contato_telefone_comercial
        self.__contato_email = contato_email
        self.__apolices = apolices

class Beneficiario:

    def __init__(self, primeiro_nome, sobrenome, nascimento, cpf, rg,tipo,
                 endereco_rua, endereco_numero, endereco_complemento, endereco_cep,
                 endereco_estado, endereco_cidade,
                 contato_celular, contato_telefone, contato_residencial,
                 contato_telefone_comercial,
                 contato_email
                 ):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__nascimento = nascimento
        self.__rg = rg
        self.__cpf = cpf
        self.__tipo = tipo
        self.__endereco_rua = endereco_rua
        self.__endereco_numero = endereco_numero
        self.__endereco_complemento = endereco_complemento
        self.__endereco_cep = endereco_cep
        self.__endereco_estado = endereco_estado
        self.__endereco_cidade = endereco_cidade
        self.__contato_celular = contato_celular
        self.__contato_telefone = contato_telefone
        self.__contato_residencial = contato_residencial
        self.__contato_telefone_comercial = contato_telefone_comercial
        self.__contato_email = contato_email

class Apolice


