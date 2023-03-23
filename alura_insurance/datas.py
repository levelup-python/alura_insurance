class Data:
    def __init__(self,dia,mes,ano):
        print("Cadastrado.")
        self.dia=dia
        self.mes=mes
        self.ano=ano
        self.formatada="{}/{}/{}".format(self.dia,self.mes,self.ano)


d=Data("23","08","2002")

d.dia
d.mes
d.ano
d.formatada