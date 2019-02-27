from bs4 import BeautifulSoup
import requests
import pandas as pd


def coinmarketcap_mainpage():
    url = "https://coinmarketcap.com/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    
    # get currency name
    names = [name.text.strip() for name in soup.find_all("a", {"class": "currency-name-container"})] 
    
    # get currency price
    prices = [price.text.strip()  for price in soup.find_all("a", {"class": "price"})]
    
    # get currency marketcap
    markets = [market.text.strip()  for market in soup.find_all("td", {"class": "market-cap"})]
    
    # get currency daily volume 
    volume = [x.get_text().strip() for x in soup.find_all('a', {"class":"volume"})]
    
    # get currency daily price change
    change = [x.get_text().strip() for x in soup.find_all('td', {"class": "percent-change"})]

    df = pd.DataFrame({'name': names, 'price': prices, 'marketcap': markets, "volume": volume, "change": change})
    
    return df

def coinmarketcap_mainpage_single_currency(name):
    url = "https://coinmarketcap.com/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    currency_id = "id-" + name

    currency = soup.find("tr", {"id": currency_id})

    # get currency name
    name = currency.find("a", {"class": "currency-name-container"}).text.strip() 
    
    # get currency price
    price = currency.find("a", {"class": "price"}).text.strip() 
    
    # get currency marketcap
    market = currency.find("td", {"class": "market-cap"}).text.strip() 
    
    # get currency daily volume 
    volume = currency.find('a', {"class":"volume"}).text.strip() 
    
    # get currency daily price change
    change =  currency.find('td', {"class": "percent-change"}).text.strip() 

    response = {'name': name, 'price': price, 'marketcap': market, "volume": volume, "change": change}
    
    return response



df = coinmarketcap_mainpage()
print(df)