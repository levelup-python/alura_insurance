class ContaSegurado:
    def __init__(self,Nome,Sobrenome,nascimento,cpf,rg,endereco,contato,beneficiarios):
        print("Cadastrando cliente...{}".format(self))
        self.__Nome=Nome
        self.__Sobrenome=Sobrenome
        self.__nascimento=nascimento
        self.__cpf=cpf
        self.__rg=rg
        self.__endereco=endereco
        self.__contato=contato
        self.__beneficiarios=beneficiarios
        def NomeCompleto(self):
            print("{} {}".format(self.__Nome,self.__Sobrenome))
        
class ContaBeneficiario:
    def __init__(self,NomeSobrenome,nascimento,cpf,rg,tipo,endereco,contato):
        print("Cadastrando cliente...{}".format(self))
        self.__NomeSobrenome=NomeSobrenome
        self.__nascimento=nascimento
        self.__cpf=cpf
        self.__rg=rg
        self.__endereco=endereco
        self.__contato=contato
        self.__tipo=tipo
        
class Apolice:
    def __init__(self,numero,tipo,valordopremio,segurado,corretor,vigencia,datadecriacao,status):
        print("Cadastrando cliente...{}".format(self))
        self.__numero=numero
        self.__tipo=tipo
        self.__valordopremio=valordopremio
        self.__segurado=segurado
        self.__corretor=corretor
        self.__vigencia=vigencia
        self.__datadecriacao=datadecriacao
        self.__status=status
                
class Corretor:
    def __init__(self,NomeSobrenome,NumeroSusep,apolices,contato):
        self.NomeSobrenome=NomeSobrenome
        self.NumeroSusep=NumeroSusep
        self.apolices=apolices
        self.contato=contato

        
        
        
        
        