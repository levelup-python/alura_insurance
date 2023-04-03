from Contato import Contato
from Endereco import Endereco
from Cliente import Cliente
from Beneficiario import Beneficiario
from Apolice import Apolice
from Corretor import Corretor


class Segurado():

    def __init__(self, cliente=Cliente, endereco=Endereco, contato=Contato,
                 beneficiario=Beneficiario, apolice=Apolice,
                 corretor=Corretor):
        self._cliente = cliente
        self._beneficiario = beneficiario
        self._apolice = apolice
        self._corretor = corretor
        self._endereco = endereco
        self._contato = contato

    @ property
    def contato(self):
        return self._contato

    @ property
    def beneficiario(self):
        return self._beneficiario

    @ property
    def apolice(self):
        return self._apolice

    @ property
    def cliente(self):
        return self._cliente

    @ property
    def corretor(self):
        return self._corretor


segurado1 = Cliente('João', 'Silva', '111.111.111-11', '2222222', '01/01/1980')
segurado1.nome_completo()

endereco1 = endereco_benef1 = Endereco(
    'av brandao', '50', 'ap 2', '2024055', 'RJ', 'rio de janeiro')
contato1 = Contato('21 9 8756 4323', '21 2345 6789',
                   '21 4532 3456', 'joao@hotmail.com')
contato_benef1 = Contato('21 9876 4355', '00 0000 0000',
                         '00 0000 0000', "ana@hotmail.com")
benef1 = Cliente('Ana', 'Andrade', '123-123-343-45', '763458', '12/34/56')
beneficiario1 = Beneficiario(benef1, endereco_benef1, contato_benef1, 1)

apolice1 = Apolice('238575', 5000, 'segurado1', '23/04/2020',
                   '22/04/1999', 'VIDA', 'ativo')
apolice2 = Apolice('000000', 5000, 'segurado1', '00/00/2020',
                   '22/04/1999', 'VIAGEM', 'ativo')

contato_corretor = Contato(
    '21 9875 9845', '21 2345 6778', '21 4567 2324', 'antonio@gmail.com')
Corretor1 = Corretor('Antonio', 'goncalves', '234567', [
                     apolice1, apolice2], contato_corretor)

len(Corretor1.comissao_total)

Corretor1._apolices[0].comissao

Corretor1.comissao_total
