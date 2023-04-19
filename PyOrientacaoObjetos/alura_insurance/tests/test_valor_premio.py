from Apolice import Apolice
from Segurado import Segurado


class Teste:

    def test_valor_premio_retorna_valor_maior_que_0(self):
        # Given contexto
        premio1 = 5000
        premio2 = 5000
        esperado = 10000

        apolice1 = Apolice('238575', premio1, 'segurado1', '1980-02-01',
                           '22/04/1999', 'VIDA', 'ativo')
        apolice2 = Apolice('000000', premio2, 'segurado1', '1980-02-01',
                           '22/04/1999', 'VIAGEM', 'ativo')

        cliente1 = Segurado('Ana', 'endereco', 'contato',
                            'benef', [apolice1, apolice2], 'Corretor')

        resultado = cliente1.premio_total  # When - Ação

        assert resultado == esperado  # Then - Desfecho
