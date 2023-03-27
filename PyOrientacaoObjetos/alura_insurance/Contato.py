class Contato:
    def __init__(self, celular, telefone_residencial, telefone_comercial, email):
        self.celular = celular
        self.telefone_residencial = telefone_residencial
        self.telefone_comercial = telefone_comercial
        self.email = email


dados = Contato('21 99985 3145', '21 3222 6666',
                '21 0000 9999', 'ana@hotmail.com')
