from bs4 import BeautifulSoup
import requests
import pandas as pd


def top_movies():
    url = "https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    # get movie title
    titles = [title.text.split('.')[1] for title in soup.find_all('h3', {"class": "lister-item-header"})]
    # get movie year
    years = [year.split('(')[1].split(')')[0].strip() for year in titles]
    titles = [title.split("(")[0].strip() for title in titles]
    # get movie rating
    ratings = [rating.text.strip() for rating in soup.find_all('div', {"class": "ratings-imdb-rating"})]

    df = pd.DataFrame({'movies': titles, 'rating': ratings, 'year': years})
    return df


print(top_movies())