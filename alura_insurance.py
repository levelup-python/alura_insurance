class Segurado:

    def __init__(self, primeiro_nome, sobrenome, nascimento, cpf, rg,
                 endereco_rua, endereco_numero, endereco_complemento, endereco_cep,
                 endereco_estado, endereco_cidade,
                 contato_celular, contato_telefone, contato_residencial,
                 contato_telefone_comercial,
                 contato_email, beneficiarios, apolices):
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

        def nome_completo(self):
            print("O nome completo do segurado é: ".format(self.__primeiro_nome, self.__sobrenome))

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

class Apolice:
    def __init__(self, numero, valor_premio, valor_beneficio, segurado,
                 corretor, vigencia, data_criacao, status, tipo='VIDA'):
        self.__numero = numero
        self.__tipo = tipo
        self.__valor_premio = valor_premio
        self.__valor_beneficio = valor_beneficio
        self.__segurado = segurado
        self.__corretor = corretor
        self.__vigencia = vigencia
        self.__data_criacao = data_criacao
        self.__status = status

class Corretor:
    def __init__(self, primeiro_nome, sobrenome, numero_susep, apolices, contato_celular, contato_telefone,
                 contato_residencial, contato_telefone_comercial, contato_email):
        self.__primeiro_nome = primeiro_nome
        self.__sobrenome = sobrenome
        self.__numero_susep = numero_susep
        self.__apolices = apolices
        self.__contato_celular = contato_celular
        self.__contato_telefone = contato_telefone
        self.__contato_residencial = contato_residencial
        self.__contato_telefone_comercial = contato_telefone_comercial
        self.__contato_email = contato_email



