import sqlite3
import random
import requests
from bs4 import BeautifulSoup

banco = sqlite3.connect('Produtos.db')
cursor = banco.cursor()

visitados = []

class scrapper:
    def __init__(self):
        pass
    
    def crawl():
        try:
            rand = random.randint(1000000000, 2400000000)
            url = f'https://produto.mercadolivre.com.br/MLB-{rand}'
            if url in visitados:
                print('Ja foi visitado')
                scrapper.crawl()
            else:
                params = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel)'}
                req = requests.get(url, params=params)
                bs = BeautifulSoup(req.text, 'html.parser')
                produto = bs.find('h1').text
                desc = bs.find('p', {'class': 'ui-pdp-description__content'}).text
                preço = bs.find('span', {'class': 'andes-money-amount__fraction'}).text.replace('.', ',')
                print('Encontrado')
                visitados.append(rand)
                cursor.execute(f"""INSERT INTO produtos VALUES(NULL, '{produto}', '{preço}', '{url}')""")
                banco.commit()
            
        except AttributeError:
            scrapper.crawl()
        
        
        
for x in range(100000):
    scrapper.crawl()       

banco.close()