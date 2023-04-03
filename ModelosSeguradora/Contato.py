class Contato:

    def __init__(self, celular, telefone_residencial, telefone_comercial, email):
        self._celular = celular
        self._telefone_comercial = telefone_comercial
        self._telefone_residencial = telefone_residencial
        self._email = email

    def contato_completo(self):
        return ({"Celular": self._celular, "Telefone_Comercial": self._telefone_comercial, "Telefone_Residencial": self._telefone_residencial, "Email": self._email})