from bs4 import BeautifulSoup
import requests
import pandas as pd


def rotten_mainpage():
    url = "https://www.rottentomatoes.com/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    table_top_box = soup.find('table', {"id": "Top-Box-Office"})
    titles_top_box = [title.text.strip() for title in table_top_box.find_all("td", {"class": "middle_col"})]
    ratings_top_box = [rating.text.strip() for rating in table_top_box.find_all("span", {"class": "tMeterScore"})]
    #print(ratings)

    table_opening = soup.find('table', {"id": "Opening"})
    titles_opening = [title.text.strip() for title in table_opening.find_all("td", {"class": "middle_col"})]
    ratings_opening = [rating.text.strip() for rating in table_opening.find_all("span", {"class": "tMeterScore"})]
    #print(ratings)

    table_tv = soup.find('div', {"id": "homepage-tv-bottom"})
    titles_tv = [title.get_text().strip() for title in table_tv.find_all("td", {"class": "middle_col"})]
    ratings_tv = [rating.text.strip() for rating in table_tv.find_all("span", {"class": "tMeterScore"})]
    #print(titles_tv)
    
    
    # df1 = pd.DataFrame({'TOP BOX OFFICE': titles_top_box, "RATING": ratings_top_box})
    # df2 = pd.DataFrame({'OPENING THIS WEEK': titles_opening, "RATING": ratings_opening})
    # df3 = pd.DataFrame({'TV SHOWS': titles_tv, "RATING": ratings_tv})
    
    response = [
        {'TOP BOX OFFICE': titles_top_box, "RATING": ratings_top_box},
        {'OPENING THIS WEEK': titles_opening, "RATING": ratings_opening},
        {'TV SHOWS': titles_tv, "RATING": ratings_tv}
    ]
    print(response)

rotten_mainpage()
