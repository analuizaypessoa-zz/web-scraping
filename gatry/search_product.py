from bs4 import BeautifulSoup
import requests
import pandas as pd

def search_product(product):
    url = "https://gatry.com/promocoes?q=" + product
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')


    products  = soup.find_all('div', {"class": "informacoes"})

    titles = [item.find('h3').text for item in products]
    links = [item.find('a').get('href') for item in products]
    prices = [item.find('p', {"class":'preco margin-comentario'}).text for item in products]
   
    
    print(titles)
    print(links)
    print(prices)


search_product("headphone")