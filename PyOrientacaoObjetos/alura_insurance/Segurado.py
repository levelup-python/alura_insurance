from alura_insurance.Contato import Contato
from alura_insurance.Endereco import Endereco


class Segurado:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, endereco, contato, beneficiarios):
        self.nome = nome
        self.ano = sobrenome
        self.duracao = data_nascimento
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
        self.beneficiarios = beneficiarios


dados = Segurado('Ana', '90', '00', 'Ana', '90', '00', 'Ana', '90')
print(dados)
print(f'nome: {dados.nome} - ano: {dados.ano}'
      f' - duracao: {dados.duracao}')
