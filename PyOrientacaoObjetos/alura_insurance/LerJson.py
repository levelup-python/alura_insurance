
import json

# abre um arquivo para leitura e ao final fecha
with open('arquivo.json') as conteudo:
    # lê o arquivo e transforma em dict
    pessoa = json.load(conteudo)

# pegando a propriedade celular do arquivo e imprimindo
print(pessoa['contato']['celular'])
