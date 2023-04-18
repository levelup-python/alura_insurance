import re


class Contato:
    def __init__(self, celular, telefone_residencial, telefone_comercial, email):
        self.__celular = celular
        self._telefone_residencial = telefone_residencial
        self._telefone_comercial = telefone_comercial
        self.__email = email
        self.__set_celular(celular)
        self.__set_email(email)

    @property
    def celular(self):
        return self.__celular

    def __set_celular(self, value):
        if value is None:
            raise ValueError("O celular não pode ser nulo", value)

        self.__celular = value

    @property
    def email(self):
        return self.__email

    def __set_email(self, value):
        padrao_email = re.compile(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not padrao_email.match(value):
            raise ValueError("O email precisa ter um formato valido", value)

        self.__email = value


a = Contato('2184735368', '3426374532', '65457786', 'adad@gmail.com')
