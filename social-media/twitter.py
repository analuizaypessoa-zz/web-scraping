from bs4 import BeautifulSoup
import requests
import pandas as pd


# get account info such as number of followers and stuff
def twitter_profile_info(account):
        url = "https://twitter.com/" + account
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        tag = soup.find("li", {"class": "ProfileNav-item ProfileNav-item--tweets is-active"})
        tweets_number = tag.find("span", {"class": "ProfileNav-value"}).get_text().strip()
        print(tweets_number)

        tag = soup.find("li", {"class": "ProfileNav-item ProfileNav-item--following"})
        following = tag.find("span", {"class": "ProfileNav-value"}).get_text().strip()
        print(following)

        tag = soup.find("li", {"class": "ProfileNav-item ProfileNav-item--followers"})
        followers = tag.find("span", {"class": "ProfileNav-value"}).get_text().strip()
        print(followers)

        tag = soup.find("li", {"class": "ProfileNav-item ProfileNav-item--favorites"})
        likes = tag.find("span", {"class": "ProfileNav-value"}).get_text().strip()
        print(likes)
        
        bio = soup.find("p", {"class": "ProfileHeaderCard-bio u-dir"}).get_text().strip()
        print(bio)

        join_date = soup.find("span", {"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"}).get_text().strip()
        print(join_date)
        
        info = {
                "Number of tweets": tweets_number,
                "Following": following,
                "Followers": followers,
                "Likes": likes,
                "Bio": bio,
                "Join date": join_date
        }

        return info


# get tweets text 
def twitter_profile_tweets(account):
    url = "https://twitter.com/" + account
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    tweets = [tweet.text for tweet in soup.find_all('p',{"class": "TweetTextSize"})]
    users = [user.text for user in soup.find_all('strong', {"class": "fullname"})]
    c = 1
    for i in range(len(tweets)):
        print(c, tweets[i], "\n"
        "by ",  users[i], "\n")
        c+=1




