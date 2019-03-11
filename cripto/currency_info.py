from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_currency_info(name):
    url = "https://coinmarketcap.com/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    currency_id = "id-" + name.lower()

    currency = soup.find("tr", {"id": currency_id})
    
    price = currency.find("a", {"class": "price"}).text.strip() 
    
    market = currency.find("td", {"class": "market-cap"}).text.strip() 
    
    volume = currency.find('a', {"class":"volume"}).text.strip() 
    
    change =  currency.find('td', {"class": "percent-change"}).text.strip() 

    
    df = pd.DataFrame({'price': [price], 'marketcap': [market], "volume": [volume], "change": [change]}, index=[name])
    
    return df
    



print("What currency do you wanna take a look? \n")
currency = input()
df = get_currency_info(currency)
print("\n\n",df)