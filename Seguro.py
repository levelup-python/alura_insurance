from Apolice import Apolice, TipoApolice
from Beneficiario import Beneficiario
from Calculadora import Calculadora
from Corretor import Corretor   
from Endereco import Endereco
from Segurado import Segurado
from datetime import date


endereco1 = Endereco("Merces", 43, "casa", "123", "Rio de Janeiro", "RJ")
endereco2 = Endereco("Tres Rios", 172, "casa", "22745160", "Rio de janeiro", "RJ")
benef1 = Beneficiario("Erika", "Gascao", date(2000, 1, 1), "123456", "798", endereco1, "abc", "filha")
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "45679", "9878",endereco2, "hdkhbd", "esposa")
corret1 = Corretor("Paloma", "Ferraz", "002", "999", "774")            
seg1 = Segurado("Diego", "Guerrieri", "30/11/1987", "05878456", "21245", endereco2, "1254877", [benef1, benef2], corret1, "apol1")
apol1 = Apolice(1, TipoApolice.Vida, 100, 1000000, seg1,corret1, date(2024, 1, 1), date(2023, 3, 30),"Ativa")
apol2 = Apolice(2, TipoApolice.Casa, 500, 5000000, seg1,corret1, date(2023, 2, 2), date(2023, 3, 30),"Ativa")
calc1 = Calculadora([apol1, apol2])
apol1._tipo.value
calc1.calcula()
print(benef1)
seg1._beneficiarios[0]._primeiro_nome
seg1._beneficiarios[0]
print(seg1)

