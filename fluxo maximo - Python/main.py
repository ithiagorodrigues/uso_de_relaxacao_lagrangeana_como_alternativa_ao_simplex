dado = {
    'variavel':{},
    'funcao':{},
    'objetivo':{},
    'restricao':{}
    }

contR = 0
contV = 0
file = open('fluxo maximo\dados.txt','r+')
for linha in file:
    linha = linha.rstrip()
    if 'vq' in linha:        
        contV = int(linha.replace('vq ',''))+1        
    elif 'v' in linha:
        dado['variavel']['v'+str(contV-1)] =linha.replace('v ','')
        contV -= 1
    elif 'f' in linha:
        dado['funcao']['f'] = linha.replace('f ','')
    elif 'o' in linha:
        dado['objetivo']['o'] = linha.replace('o ','')
    elif 'rq' in linha:
        contR = int(linha.replace('rq ',''))+1
    elif 'r' in linha:
        dado['restricao']['r'+str(contR-1)] =linha.replace('r ','')
        contR -= 1

    pass  

file.close()

for dado_k,dado_v in dado.items():
    print(f'{dado_k}')
    for dados_k, dados_v in dado_v.items():
        print(f'\t{dados_k} , {dados_v}')
        pass
    pass