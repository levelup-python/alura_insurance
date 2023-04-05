from typing import Optional

from validadores import valida_arg_nao_nulo
from validadores import valida_email


class Contato:
    def __init__(
        self, celular: str, telefone_residencial: Optional[str], telefone_comercial: Optional[str], email: str
    ):
        self._celular = valida_arg_nao_nulo(celular, "celular")
        self._telefone_residencial = telefone_residencial
        self._telefone_comercial = telefone_comercial
        self._email = valida_email(email)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("celular"),
            data.get("telefone_residencial"),
            data.get("telefone_comercial"),
            data.get("email"),
        )

    def __str__(self):
        return (
            f"celular: {self._celular}, telefone_residencial: {self._telefone_residencial}, telefone_comercial: "
            f"{self._telefone_comercial}, email: {self._email}"
        )
