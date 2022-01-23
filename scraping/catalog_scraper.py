import requests
from bs4 import BeautifulSoup
from pprint import pprint
from fake_useragent import UserAgent
import time
import re

rmhtml = re.compile('<.*?>')

# randomizing useragent to prevent getting locked
ua = UserAgent()

headers = {
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}


def fetch_html(url):
    headers["User-Agent"] = ua.random
    url = url.strip()
    cont = requests.get(url, headers=headers)
    return cont.text

def make_soup(html, index):
    soup = BeautifulSoup(html, 'html.parser')
    multisoup = soup.find_all("td", {"class": "ntdefault"})
    title = soup.find("td", {"class": "nttitle", "scope": "colgroup"}).get_text()
    if len(multisoup) > 0:
        tex = (multisoup[0]).get_text()
        if (tex.find("West Lafayette") != -1):
            f = open("clean_html/course" + str(index) + ".txt", "a")
            f.write(title + "\n")
            f.write(tex)


if __name__ == "__main__":
    count = 0
    urlfile = open("urls.txt", "r")
    for line in urlfile:
        html = fetch_html(line)
        make_soup(html, count)
        count += 1
