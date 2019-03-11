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


df = coinmarketcap_mainpage()
print(df)
print("< CoinMarketCap currencies info >")