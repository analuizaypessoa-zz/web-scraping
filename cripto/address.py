from bs4 import BeautifulSoup
import requests
import pandas as pd

tx = "c6f2a07b8d2101bc4303ffb31a72ec20e7eadcdddf6b81f9980e5a5845955634"
addr = "1Hz96kJKF2HLPGY15JWLB5m9qGNxvt8tHJ"

def get_address(address):
    url = "https://blockstream.info/address/" + address
    print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    print(soup)

    data = soup.find("div", {"class": "stats-table"})
    #names = [name.text.strip() for name in soup.find_all("a", {"class": "currency-name-container"})] 
    print(data)


get_address(addr)