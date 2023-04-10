import re
import datetime
from dateutil.relativedelta import relativedelta



def ValidaNome(value):
     
     if not isinstance(value, str):
            raise ValueError("O atributo nome deve ser uma string")
     
     if len(value) < 2:
            raise ValueError("O atributo nome deve conter no mínimo 2 caracteres")
     
     return value


def ValidaSobrenome(value):
     
     if not isinstance(value, str):
            raise ValueError("O atributo sobrenome deve ser uma string")
     
     if len(value) < 2:
            raise ValueError("O atributo sobrenome deve conter no mínimo 2 caracteres")
     
     return value


def ValidaCPF(value):
    
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    valida = re.match(padrao, value)

    if valida == None:
        raise ValueError("CPF não está na formatação correta")
    return value

def ValidaDataNascimento(value):

    data_atual = datetime.date.today()    
    
    if value == None or len(value) == 0:
        raise ValueError("O atributo data_nascimento não pode ser nulo")
    
    value = datetime.date(int(value[6:11]), int(value[3:5]),int(value[0:2]))
    if value > data_atual:
        raise ValueError("Data de nascimento não pode ser uma data futura")
        
    return value

def ValidaVazioNulo(value, nome_atributo):
     
    if value == None or len(value) == 0:
        raise ValueError(f"O atributo {nome_atributo} não pode ser nulo")
    
    return value

def ValidaQtdBeneficiarios(value):

    if len(value) > 10:
        raise ValueError("Não pode ter mais que 10 beneficiários")
        
    return value