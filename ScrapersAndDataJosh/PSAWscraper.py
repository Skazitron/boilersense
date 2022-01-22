import praw
import pandas as pd
import datetime as dt
import os
from psaw import PushshiftAPI
import re

if __name__ == '__main__':
    # Get credentials from DEFAULT instance in praw.ini
    with open("./ScrapersAndDataJosh\\PRAW\\secrets.txt","r") as f:
        client_id, client_secret, user_agent, username, password = f.readlines()    #client_id, client_secret, user_agent, username, password
        
    reddit = praw.Reddit(
        client_id=client_id[:-1],
        client_secret=client_secret[:-1],
        user_agent=user_agent[:-1],
        username=username[:-1],
        password=password,
    )

    api = PushshiftAPI(reddit)

    start_epoch=int(dt.datetime(2021, 11, 30).timestamp())

    i = 0
    for submission in api.search_submissions(
        after=start_epoch,
        subreddit='Purdue',
        q='MA261 and FYE',
        limit=1
    ):
        if len(re.compile("\\D{2,4}\\d{0,5}").findall(submission.title)) == 1:
            for comment in api.search_comments(
                subreddit='Purdue',
                link_id=submission.id,
                filter=['body']
            ):
                print(comment.body)
                i += 1
    print(i)