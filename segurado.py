from datetime import date
from typing import List

from apolice import Apolice
from beneficiario import Beneficiario
from contato import Contato
from endereco import Endereco
from pessoa import Pessoa
from validadores import valida_arg_nao_nulo
from validadores import valida_beneficiarios
from validadores import valida_maioridade


class Segurado(Pessoa):
    def __init__(
        self,
        primeiro_nome: str,
        sobrenome: str,
        data_nascimento: date,
        cpf: str,
        rg: str,
        endereco: Endereco,
        contato: Contato,
        beneficiarios: List[Beneficiario],
        apolices: List[Apolice],
    ) -> None:
        super().__init__(
            primeiro_nome, sobrenome, data_nascimento, cpf, rg, endereco, contato
        )
        self._beneficiarios = valida_beneficiarios(beneficiarios)
        self._apolices = valida_arg_nao_nulo(apolices, "apolices")
        self._data_ingresso = min([apolice.data_inicio_vigencia for apolice in apolices])
        valida_maioridade(self._data_nascimento, self._data_ingresso)

    def __str__(self):
        return super().__str__() + f", beneficio_total: {self.beneficio_total():,.2f}"

    def beneficio_total(self):
        return sum([apolice.valor_beneficio for apolice in self._apolices])
