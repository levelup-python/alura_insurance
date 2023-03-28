from Segurado import *
from Apolice import *
from Corretor import *
from Beneficiario import *

#print(segurado1.nome_completo())

apolice1 = Apolice(1, 100, 10000, "REBECA", "A", '01/01/2023', '01/01/2023','01/01/2023', StatusApolice.ATIVA, TipoApolice.VIDA)

apolice2 = Apolice(2, 200, 20000, "REBECA", "B", '01/01/2023', '01/01/2023', '01/01/2023', StatusApolice.ATIVA, TipoApolice.VIDA)

segurado1= Segurado("Rebeca","barros","14/04/1999","1234","098","rua x","rebeca@gmail.com","l",[apolice1,apolice2])
ben = Beneficiario("Rebeca","barros","14/04/1999","1234","098",TipoBeneficiario.FILHOS, "endereco", "contato")
print(ben.tipo)
#print(apolice2.valor_premio)

#x = [apolice1,apolice2]
#print(x[0].valor_premio)
print(segurado1.premio_total())
#print(segurado1.beneficio_total())
#corretor1 = Corretor("Ana", "Silva", "AB123", [apolice1], "9999-9999","rebeca@gmail.com")
#print(corretor1.comissao_total())
