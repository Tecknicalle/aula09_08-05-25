# CADASTRA 
def cadastra_pessoa(num):
    for i in range(num):
        nome = input('informe o nome do vendedor, por favor!: ')
        valor = input('informe o valor da venda!:   ')

        pessoa = {
            'Nome': nome, 
            'valor': valor 
        }

        lst_cadastro.append(pessoa)


def calcula_total_media(): 
    tot = 0
    for pessoa in lst_cadastro:
     tot += pessoa['valor']

    med = tot / len(lst_cadastro)
    return tot, med

def busca_maior()
    maior = 0
    vendedor = ''

    for v in lst_cadastro:
        if v ['valor'] > maior:
            maior = v['valor']
            vendedor = v['Nome']

    return maior, vendedor 

def busca_vendedor(nome):
    resposta = ''
    vl = 0

    for cadastro in lst_cadastro:
        if cadastro('nome') == nome:
            resposta = cadastro('nome')
            vl = cadastro['valor']

            return resposta, vl
    return resposta, vl   # Se entrar no if, executa as in
return resposta, vl # Só executa, se não entrar no if     


            



    


# EXEMPLO 1 - CADASTRA FUNCIONÁRIO  

lst_cadastro = []

qtd = int(input('Quantas pessoas?'))
cadastra_pessoa(qtd)
print(lst_cadastro)

# ----------------------------------------------------------------------------

# EXEMPLO 2 - TOTAL E MÉDIA 

total, media = calcula_total_media()
print(30'=')
print(f'total': {total})
print(f'média: {media}')

# EXEMPLO 3 - MAIOR VALOR E VENDEDOR 
maior_venda, maior_vendedor = busca_maior()
print(30'=')
print(f'Maior venda: {maior_venda})
print(f'Nome do vendedor: {maior_vendedor}')

# EXEMPLO 04 - BUSCAR VENDEDOR 
vendedor = input('Informe o nome do vendedor: ')
nome_vendedor = busca_vendedor(vendedor)

if nome_vendedor:
    print(f'O vendedor {nome_vendedor} está presente')
    print(f'O valor da venda é {Valor}')
else:
 print('f{nome_vendedor} não encontrado')          




