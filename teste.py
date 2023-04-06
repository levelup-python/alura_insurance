from ModelosSeguradora.Segurado import *
from ModelosSeguradora.Apolice import *
from ModelosSeguradora.Corretor import *
from ModelosSeguradora.Beneficiario import *
from ModelosSeguradora.Endereco import *
from ModelosSeguradora.Contato import *
from ModelosSeguradora.Pessoa import *
import datetime
from ModelosSeguradora.CalculadoraComissao import *

# Faremos uma cliente chamada Ana que tem duas apólices ativas na seguradora com o mesmo corretor, Joao, e cujo beneficario é sua filha Clara.

# Definindo os objetos de cada classe:
## Para a definicao de contato e endereco usaremos as respectivas classes

endereco_ana = Endereco("X", "203", "Y", "Rio de Janeiro", "RJ", "Brasil")
contato_ana = Contato(99998888, 11112222, 33334444, "anasilva@gmail.com")
contato_joao = Contato(77779898, 21212121, 75986352, "joaosantoscorretagem@gmail.com")

# Definindo o beneficiario
beneficiario1 = Beneficiario("Clara","Silva","08/09/2010","000.000.000-60","9191991991",TipoBeneficiario.FILHOS, "endereco", "contato")

## Definindo o segurado
segurado1= Segurado("ana","silva","25/08/1986","123.456.789-00","223334441",endereco_ana.endereco_completo(),contato_ana.contato_completo(),[beneficiario1])

print(len('15414600000000000'))
## Definindo Corretor
corretor1 = Corretor("Joao", "santos", "15414600000000000", contato_joao)

## Definindo as apolices
apolice1 = Apolice(1, 143, 150000, segurado1, corretor1, '01/01/2022', '31/12/2025','01/12/2021', StatusApolice.ATIVA, TipoApolice.VIDA)
apolice2 = Apolice(2, 56, 25000, segurado1, corretor1, '01/01/2023', '31/12/2023', '25/12/2022', StatusApolice.ATIVA, TipoApolice.VIDA)

## Incluindo as apolices no corretor e segurado
corretor1.incluir_apolice(apolice1)
corretor1.incluir_apolice(apolice2)

segurado1.incluir_apolice(apolice1)
segurado1.incluir_apolice(apolice2)


print(segurado1.nome_completo())

"""
print(corretor1.apolices)
print(segurado1.apolices)

print(segurado1)
print(beneficiario1)
print(corretor1)
print(apolice1)
print(apolice2)

calc1 = CalculadoraComissao([apolice1, apolice2])
print(calc1.calcula_comissao())
"""

# Testando as classes criadas:
#print("Valor do beneficio da apólice1 é {} reais".format(apolice1.valor_beneficio))
#print("Valor do prêmio da apólice2 é {} reais".format(apolice2.valor_premio))
#print("Valor do prêmio total que a segurada Ana paga é {} reais".format(segurado1.premio_total()))
#print("Valor do beneficio total que a segurada Ana paga é {} reais".format(segurado1.beneficio_total()))
#print("Valor do total de comissão que o corretor Joao recebe é {} reais".format(corretor1.comissao_total()))
