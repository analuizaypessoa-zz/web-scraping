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

def imdb_top_movie_details():
    url = "https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    # get movie page url 
    tags = soup.find_all('h3',{"class": "lister-item-header"})
    movies_url = ["https://www.imdb.com" + item.find('a').get('href') for item in tags]

    movies = []
    for link in movies_url:
        # go to the movie page and get detailed info
        movie = movie_details(link)
        print(movie)
        movies.append(movie)


print(top_movies())