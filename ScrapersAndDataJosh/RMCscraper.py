import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

URLS = []

req = requests.get("https://www.ratemycourses.io/purdue")
bigSoup = BeautifulSoup(req.content, 'html5lib')
urlsTable = bigSoup.find('article').find('div').find_next_sibling().find_next_sibling().find('div').find_next_sibling().find_next_sibling().find('div').find_next_sibling().find('div').find_all('a')
for val in urlsTable:
    URLS.append("https://www.ratemycourses.io" + val['href'])

comments = []
difficulty = []
possibleDifficulties = ["Very Hard", "Hard", "Avg. Difficulty", "Easy", "Very Easy"]

for URL in URLS:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())


    commentsTable = soup.find_all('div', class_='MuiTypography-root MuiTypography-subtitle2 MuiTypography-gutterBottom')
    for val in commentsTable:
        if (val.text == "Comments on the course"):
            comments.append(val.find_next().text)


    difficultyTable = soup.find_all('span')
    for val in difficultyTable:
        if (val.text in possibleDifficulties):
            difficulty.append(val.parent.find('span').text)

df = pd.DataFrame(columns = ["features", "difficulty"])
df["features"] = comments
df["difficulty"] = difficulty
if (os.name == 'nt'):
    csv = f'./ScrapersAndDataJosh\\RMCreviews.csv'
else:
    csv = f'./ScrapersAndDataJosh/RMCreviews.csv'
df.to_csv(csv)
    # for comment in comments:
    #     print(comment, difficulty[i])
    #     i += 1
