import praw
import pandas as pd
import datetime as dt
import os
from psaw import PushshiftAPI
import re
import time
import requests
from bs4 import BeautifulSoup
import string

def soupScrape():
    URL = "https://www.thesaurus.com/browse/easy"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())

    table = soup.find('ul', class_='css-123gjy7 e1ccqdb60').find_all('li')
    for val in table:
        print(val.find('a').text)


def redditScrape():

    def findSynonyms():
        for synonym in synonyms:
            index = comment.body.lower().find(synonym)
            if index == -1 or (index != 0 and comment.body[index-1] not in string.whitespace + string.punctuation) or (index + len(synonym) < len(comment.body) and comment.body[index + len(synonym)] not in string.whitespace + string.punctuation):
                continue
            else:
                comments.append(comment.body)
                print(synonym, comment.body, comment.body.lower().find(synonym))
                return 1
        return 0

    start_epoch=int(dt.datetime(2021, 11, 1).timestamp())

    comments = []

    print("Starting reddit crawl...")

    course = '\"ma261 curve\"'

    for submission in api.search_submissions(
        after=start_epoch,
        subreddit='Purdue',
        q=course,
        limit=10000
    ):
        print(submission.title)
        if len(re.compile("\\D{2,4}\\d{3,5}").findall(submission.title)) == 1:
            for comment in api.search_comments(
                subreddit='Purdue',
                link_id=submission.id,
                filter=['body']
            ):
                findSynonyms()
                time.sleep(0.1)
        time.sleep(1)

    # df = pd.DataFrame(columns=['comments'])
    # df['comments'] = comments
    # strippedCourse = re.sub(r'\W+', '', course)
    # if (os.name == 'nt'):
    #     csv = f'./ScrapersAndDataJosh\\{strippedCourse}_comments.csv'
    # else:
    #     csv = f'./ScrapersAndDataJosh/{strippedCourse}_comments.csv'
    # df.to_csv(csv)


if __name__ == '__main__':
    # Get credentials from DEFAULT instance in praw.ini
    with open("./ScrapersAndDataJosh\\PRAW\\secrets.txt","r") as f:
        client_id, client_secret, user_agent, username, password = f.readlines()    #client_id, client_secret, user_agent, username, password

    with open("./ScrapersAndDataJosh\\synonyms.txt") as f:
        synonyms = f.readlines()
        synonyms = [synonym.rstrip() for synonym in synonyms]
        
    reddit = praw.Reddit(
        client_id=client_id[:-1],
        client_secret=client_secret[:-1],
        user_agent=user_agent[:-1],
        username=username[:-1],
        password=password,
    )

    api = PushshiftAPI(reddit)

    redditScrape()