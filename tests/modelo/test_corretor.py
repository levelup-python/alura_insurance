from unittest.mock import Mock

import src.modelo.corretor as modulo_corretor
from src.conversores import CorretorConversor
from src.modelo.corretor import Corretor


def test_corretor_conversor():
    data = {
        "nome": "Monteiro Lobato",
        "numero_susep": "15414685940386723",
        "cpf": "123.456.789-00",
        "rg": "12.345.678-9",
        "apolices": [],
        "contato": {
            "celular": "(11)99999-9999",
            "telefone_residencial": "(11)2222-2222",
            "telefone_comercial": "(11)3333-3333",
            "email": "corretor@alura.com.br"
        }
    }
    corretor = CorretorConversor(data)()
    assert isinstance(corretor, Corretor)


def test_comissao_total_chama_calculadora_comissao_calcula(monkeypatch):
    mock_calculadora_comissao = Mock()
    monkeypatch.setattr(modulo_corretor, "CalculadoraComissao", mock_calculadora_comissao)
    corretor = Corretor(
        "Monteiro",
        "Lobato",
        "123.456.789-00",
        "12.345.678-9",
        Mock(),
        "15414685940386723",
        [],
    )
    corretor.comissao_total()
    mock_calculadora_comissao.assert_called_once()
