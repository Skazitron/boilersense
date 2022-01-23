from numpy import array
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

def addCoursesToBInfo():
    with open("./course_binfo.txt", "r") as f:
        with open("./course_binfo_compressed.txt", "w") as f2:
            for line in f:
                strippedLine = line.split(' - ')[0].replace(" ", "")
                if re.search(r"^CS[0-3]\d+", strippedLine) or re.search(r"^EAPS[0-3]\d+", strippedLine):
                    f2.write(strippedLine + '\n')
                    print("Added ", strippedLine)

def soupScrape():
    URL = "https://www.thesaurus.com/browse/easy"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())

    table = soup.find('ul', class_='css-123gjy7 e1ccqdb60').find_all('li')
    for val in table:
        print(val.find('a').text)


def redditScrape():

    courseArr = []
    with open("./course_binfo_compressed.txt") as f:
        courseArr = f.readlines()
        courseArr = [course.rstrip() for course in courseArr]

    start_epoch=int(dt.datetime(2015, 1, 1).timestamp())

    df = pd.DataFrame(columns=['Course number','Text'])
    for course in courseArr:
        for submission in api.search_submissions(
            after=start_epoch,
            subreddit='Purdue',
            q=f'{course[:-2]}|{course}',
            limit=10000
        ):
            print(submission.title)
            if len(re.compile("\\D{2,4}\\d{3,5}").findall(submission.title)) == 1:
                for comment in api.search_comments(
                    subreddit='Purdue',
                    link_id=submission.id,
                    filter=['body'],
                ):
                    if comment.score < 6:
                        continue
                    for synonym in synonyms:
                        index = comment.body.lower().find(synonym)
                        if not (index == -1 or (index != 0 and comment.body[index-1] not in string.whitespace + string.punctuation) or (index + len(synonym) < len(comment.body) and comment.body[index + len(synonym)] not in string.whitespace + string.punctuation)):
                            df = df.append({"Course number": course, "Text": comment.body }, ignore_index=True)
                            print(comment)
                            break
                    time.sleep(0.15)
            time.sleep(1)

    if (os.name == 'nt'):
        csv = f'./ScrapersAndDataJosh\\reddit_comments.csv'
    else:
        csv = f'./ScrapersAndDataJosh/reddit_comments.csv'
    df.to_csv(csv)


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