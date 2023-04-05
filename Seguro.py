from datetime import date
from Beneficiario import Beneficiario
from Corretor import Corretor
from Apolice import Apolice
from Endereco import Endereco
from Apolice import TipoApolice
from Segurado import Segurado
from Calculadora import Calculadora


endereco1 = Endereco("Merces", 43, "casa", "123", "Rio de Janeiro", "RJ")
endereco2 = Endereco("Tres Rios", 172, "casa", "22745160", "Rio de janeiro", "RJ")
benef1 = Beneficiario("Erika", "Gascao", date(1992, 7, 1), "123456", "798", endereco1, "abc", "filha")
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 1), "45679", "9878", endereco2, "hdkhbd", "esposa")
corret1 = Corretor("Paloma", "Ferraz", "002", "999", "774")
apol1= Apolice("123", TipoApolice.Vida, 100.00, 100000.00, "Diego", "Paloma", "15anos", "30/03/2023", "ATIVA")
apol2= Apolice("456", TipoApolice.Vida, 100.00, 100000.00, "Diego", "Paloma", "15anos", "30/03/2023", "ATIVA")
seg1 = Segurado("Diego", "Guerrieri", "30/11/1987", "05878456", "21245", endereco2, "1254877", [benef1, benef2], corret1, [apol1, apol2])

calc1 = Calculadora([apol1, apol2])
x= calc1.calcula()

print(benef1)
seg1._beneficiarios[0]._primeiro_nome
print(seg1)