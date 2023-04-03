from ModelosSeguradora.Segurado import *
from ModelosSeguradora.Apolice import *
from ModelosSeguradora.Corretor import *
from ModelosSeguradora.Beneficiario import *
from ModelosSeguradora.Endereco import *
from ModelosSeguradora.Contato import *
from ModelosSeguradora.Pessoa import *
from ModelosSeguradora.CalculadoraComissao import *
import json

# abre um arquivo para leitura e ao final fecha
with open('inputs/Exemplo_Corretor.json') as conteudo:
    # lê o arquivo e transforma em dict
    pessoa = json.load(conteudo)

# pegando a propriedade celular do arquivo e imprimindo
print(pessoa['contato']['celular'])
print(pessoa)

contato_ex = Contato(pessoa['contato']['celular'], 
                     pessoa['contato']['tel_residencial'], 
                     pessoa['contato']['tel_comercial'],
                     pessoa['contato']['email'])

corretor_ex = Corretor(pessoa['nome'], pessoa['sobrenome'], pessoa['susep'], contato_ex)

print(corretor_ex)