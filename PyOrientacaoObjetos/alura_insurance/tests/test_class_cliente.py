from Cliente import Cliente


class Teste:

    def test_quando_chama_nomecompleto_retornar_nome_sobrenome(self):
        # Given contexto
        nome = 'Ana'
        sobrenome = 'Gonçalves'
        esperado = 'Ana Gonçalves'

        cliente1 = Cliente(nome, sobrenome, '123.123.123-12',
                           '242424', '2000-10-13')

        resultado = cliente1.calcular_nome_completo()  # When - Ação

        assert resultado == esperado  # Then - Desfecho
