import requests
from chave_api import chave


while True:
    print('''   
        ========================================A L G U M A S   A Ç Ô E S   S U G E R I D A S========================================
        
        'GOLL3','BBDC3','BBAS3','CPLE6','CVCB3','GGBR4','ITSA4', 'ITUB3', 'JBSS3', 'SANB11', 'TAEE11', 'SUZB3', 'MRVE3', 'JBSS3'
         
        =============================================================================================================================
        ''')
    acao = str(input('QUAL AÇÃO DESEJA VER: ')).upper()

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SAO&apikey={chave}'
    r = requests.get(url)
    try:
        data = r.json()['Global Quote']
        preco = data['05. price']
        print(f'A ação escolhida foi: {acao} e a cotação atual é: {preco}')
        break
    except:
        print('=-=-=-=-=Ação inválida. Veifique o nome digitado=-=-=-=-=')
        print('')
        print('')



