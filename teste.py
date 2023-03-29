from ModelosSeguradora.Segurado import *
from ModelosSeguradora.Apolice import *
from ModelosSeguradora.Corretor import *
from ModelosSeguradora.Beneficiario import *
from ModelosSeguradora.Endereco import *
from ModelosSeguradora.Contato import *
from ModelosSeguradora.Pessoa import *

# Faremos uma cliente chamada Ana que tem duas apólices ativas na seguradora com o mesmo corretor, Joao, e cujo beneficario é sua filha Clara.

# Definindo os objetos de cada classe:
## Para a definicao de contato e endereco usaremos as respectivas classes

#ana = Pessoa
endereco_ana = Endereco("X", "203", "Y", "Rio de Janeiro", "RJ", "Brasil")
contato_ana = Contato(99998888, 11112222, 33334444, "anasilva@gmail.com")
contato_joao = Contato(77779898, 21212121, 75986352, "joaosantoscorretagem@gmail.com")

## Definindo as apolices
apolice1 = Apolice(1, 143, 150000, "Ana", "Joao", '01/01/2022', '31/12/2025','01/12/2021', StatusApolice.ATIVA, TipoApolice.VIDA)

apolice2 = Apolice(2, 56, 25000, "Ana", "Joao", '01/01/2023', '31/12/2023', '25/12/2022', StatusApolice.ATIVA, TipoApolice.VIDA)

# Definindo o beneficiario
beneficiario1 = Beneficiario("Clara","Silva","08/09/2010","00000000060","9191991991",TipoBeneficiario.FILHOS, "endereco", "contato")

## Definindo o segurado
segurado1= Segurado("ana","silva","25/08/1986","12345678900","223334441",endereco_ana.endereco_completo(),contato_ana.contato_completo(),beneficiario1,[apolice1,apolice2])

## Definindo Corretor
corretor1 = Corretor("Joao", "santos", "AB123", [apolice1, apolice2], contato_joao)

# Testando as classes criadas:
print("Valor do beneficio da apólice1 é {} reais".format(apolice1.valor_beneficio))
print("Valor do prêmio da apólice2 é {} reais".format(apolice2.valor_premio))
print("Valor do prêmio total que a segurada Ana paga é {} reais".format(segurado1.premio_total()))
print("Valor do beneficio total que a segurada Ana paga é {} reais".format(segurado1.beneficio_total()))
print("Valor do total de comissão que o corretor Joao recebe é {} reais".format(corretor1.comissao_total()))

print(segurado1.nome_completo())
print(beneficiario1.nome_completo())