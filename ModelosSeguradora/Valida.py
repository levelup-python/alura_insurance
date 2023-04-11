import re
import datetime
from dateutil.relativedelta import relativedelta

def valida_nome(value):
     
     if not isinstance(value, str):
            raise ValueError("O atributo nome deve ser uma string")
     
     if len(value) < 2:
            raise ValueError("O atributo nome deve conter no mínimo 2 caracteres")
     
     return value


def valida_sobrenome(value):
     
     if not isinstance(value, str):
            raise ValueError("O atributo sobrenome deve ser uma string")
     
     if len(value) < 2:
            raise ValueError("O atributo sobrenome deve conter no mínimo 2 caracteres")
     
     return value


def valida_cpf(value):
    
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    valida = re.match(padrao, value)

    if valida == None:
        raise ValueError("Formato inválido de CPF")
    return value

def valida_data_nascimento(value):

    data_atual = datetime.date.today()    
    
    if value == None or len(value) == 0:
        raise ValueError("O atributo data_nascimento não pode ser nulo")
    
    value = datetime.date(int(value[6:11]), int(value[3:5]),int(value[0:2]))
    if value > data_atual:
        raise ValueError("Data de nascimento não pode ser uma data futura")
        
    return value


def valida_maioridade(value):

    value = datetime.date(int(value[6:11]), int(value[3:5]),int(value[0:2]))
    data_atual = datetime.date.today()
    idade = relativedelta(data_atual, value).years
        
    if idade < 18:
        raise ValueError("Segurado precisa ter pelo menos 18 anos")
    
    return value


def valida_vazio_ou_nulo(value, nome_atributo):
     
    if value == None or len(value) == 0:
        raise ValueError(f"O atributo {nome_atributo} não pode ser nulo")
    
    return value

def valida_qtd_beneficiarios(value):

    if len(value) > 10:
        raise ValueError("Não pode ter mais que 10 beneficiários")
        
    return value

def valida_email(value):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(regex, value):
        raise ValueError("O email informado está em um formato inválido.")
    
    return value
    
def valida_estado(value):
     
    lista_siglas_estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    if value not in lista_siglas_estados:
     raise ValueError("Sigla do estado inválida.")
    
    return value


def valida_cadastro_susep(value):
    inicio_num_susep = '154146'
    if len(value) != 17:
        raise ValueError("O número do cadastro SUSEP deve ter 17 caracteres")
    if value[0:6] != inicio_num_susep:
        raise ValueError("O número do cadastro SUSEP deve iniciar com: ", inicio_num_susep)
                    
    return value


