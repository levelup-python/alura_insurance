
from ModelosSeguradora.Pessoa import Pessoa
from ModelosSeguradora.Apolice import *
from ModelosSeguradora.Corretor import Corretor
from ModelosSeguradora.Segurado import Segurado

class TestClass:

    def test_quando_nome_Caroline_sobrenome_Lima_deve_retornar_nome_completo_Carolina_Lima(self):
        
        entrada_nome = 'Carolina'
        entrada_sobrenome = 'Lima'
        esperado = 'Carolina Lima'

        Pessoa_teste = Pessoa(entrada_nome, entrada_sobrenome, "01/05/1986", "123.456.789-00", "223334441")
        resultado = Pessoa_teste.nome_completo() 

        assert resultado == esperado 

    def test_quando_segurado_paga_dois_premios_143_e_84_retornar_227(self):

        entrada_premio1= 143
        entrada_premio2= 84
        esperado = 227

        segurado_teste= Segurado("ana","silva","25/08/1986","123.456.789-00","223334441","endereco_completo","contato_completo",["beneficiario1"])

        apolice_teste1 = Apolice(1, entrada_premio1, 150000, segurado_teste, "corretor_teste", '01/05/2023', '31/12/2025','01/12/2021', StatusApolice.ATIVA, TipoApolice.VIDA)
        apolice_teste2 = Apolice(2, entrada_premio2, 25000, segurado_teste, "corretor_teste", '22/06/2023', '31/12/2023', '25/12/2022', StatusApolice.ATIVA, TipoApolice.VIDA)

        segurado_teste.incluir_apolice(apolice_teste1)
        segurado_teste.incluir_apolice(apolice_teste2)

        resultado = segurado_teste.premio_total()

        assert resultado == esperado 

    def test_quando_recebe_beneficio_vida_1500000_carro_25000_casa_600000_viagem_3000_deve_retornar_10163(self):
        entrada_beneficio1 = 1500000
        entrada_beneficio2 = 25000
        entrada_beneficio3 = 600000
        entrada_beneficio4 = 3000
        esperado = 10163

        corretor_teste = Corretor("Joao", "santos", "15414600000000000", "contato_joao")
        apolice_teste1 = Apolice(1, 231, entrada_beneficio1, "segurado_teste", corretor_teste, '01/05/2023', '31/12/2025','01/12/2021', StatusApolice.ATIVA, TipoApolice.VIDA)
        apolice_teste2 = Apolice(2, 140, entrada_beneficio2, "segurado_teste", corretor_teste, '22/06/2023', '31/12/2023', '25/12/2022', StatusApolice.ATIVA, TipoApolice.CARRO)
        apolice_teste3 = Apolice(3, 124, entrada_beneficio3, "segurado_teste", corretor_teste, '22/06/2023', '31/12/2023', '25/12/2022', StatusApolice.ATIVA, TipoApolice.CASA)
        apolice_teste4 = Apolice(4, 20, entrada_beneficio4, "segurado_teste", corretor_teste, '22/06/2023', '31/12/2023', '25/12/2022', StatusApolice.ATIVA, TipoApolice.VIAGEM)

        corretor_teste.incluir_apolice(apolice_teste1)
        corretor_teste.incluir_apolice(apolice_teste2)
        corretor_teste.incluir_apolice(apolice_teste3)
        corretor_teste.incluir_apolice(apolice_teste4)

        resultado = corretor_teste.comissao_total()
        
        assert resultado == esperado 
        



