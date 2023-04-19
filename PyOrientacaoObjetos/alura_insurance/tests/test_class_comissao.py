from Apolice import Apolice
from Corretor import Corretor


class Teste:

    def test_comissao_total_retorna_soma_das_comissoes_da_apolice1_com_apolice2(self):
        # Given contexto
        premio1 = 5000
        premio2 = 5000
        esperado = 550

        apolice1 = Apolice('238575', premio1, 'segurado1', '1980-02-01',
                           '22/04/1999', 'VIDA', 'ativo')
        apolice2 = Apolice('000000', premio2, 'segurado1', '1980-02-01',
                           '22/04/1999', 'VIAGEM', 'ativo')

        corretor1 = Corretor('Antonio', 'goncalves', '234567', [
            apolice1, apolice2], 'contato_corretor')

        resultado = corretor1.comissao_total  # When - Ação

        assert resultado == esperado  # Then - Desfecho
