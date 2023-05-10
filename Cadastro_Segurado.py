class Endereco:
    def __init__(self, rua, numero, complemento, cep, estado, cidade):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.estado = estado
        self.cidade = cidade

class Contato:
    def __init__(self, celular, tel_residencial, tel_comercial, email):
        self.celular = celular
        self.tel_residencial = tel_residencial
        self.tel_comercial = tel_comercial
        self.email = email

class Beneficiario:
    def __init__(self, primeiro_nome, sobrenome, data_nascimento, cpf, rg, tipo, endereco, contato):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.rg = rg
        self.tipo = tipo
        self.endereco = endereco
        self.contato = contato

class Segurado:
    def __init__(self, primeiro_nome, sobrenome, data_nascimento, cpf, rg, endereco, contato):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
        self.beneficiarios = []

    def adicionar_beneficiario(self, beneficiario):
        self.beneficiarios.append(beneficiario)

# Teste
endereco_segurado = Endereco('Rua A', '123', 'Apto 101', '12345-678', 'SP', 'São Paulo')
contato_segurado = Contato('11 99999-9999', '11 2222-2222', '11 3333-3333', 'segurado@exemplo.com')
segurado = Segurado('João', 'Silva', '01/01/2000', '111.111.111-11', '1.234.567', endereco_segurado, contato_segurado)

endereco_beneficiario = Endereco('Rua B', '456', 'Casa 1', '54321-876', 'RJ', 'Rio de Janeiro')
contato_beneficiario = Contato('21 99999-9999', '21 2222-2222', '21 3333-3333', 'beneficiario@exemplo.com')
beneficiario = Beneficiario('Maria', 'Silva', '01/01/2005', '222.222.222-22', '7.654.321', 'PARENTE', endereco_beneficiario, contato_beneficiario)

segurado.adicionar_beneficiario(beneficiario)

print(segurado.primeiro_nome,segurado.sobrenome)
print(segurado.sobrenome)
print(beneficiario.cpf)


