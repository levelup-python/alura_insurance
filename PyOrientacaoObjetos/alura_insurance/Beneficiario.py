import alura_insurance.Contato as Contato
import alura_insurance.Endereco as Endereco


class Beneficiario:

    def __init__(self, nome, sobrenome, data_nascimento, cpf, rg, tipo, endereco, contato):
        self.nome = nome
        self.ano = sobrenome
        self.duracao = data_nascimento
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
        self.tipo = tipo


dados = Beneficiario('Ana', '90', '00', 'Ana', '90', '00', 'Ana', '90')
print(dados)
print(f'nome: {dados.nome} - ano: {dados.ano}'
      f' - duracao: {dados.duracao}')
