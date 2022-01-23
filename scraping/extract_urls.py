from bs4 import BeautifulSoup
import os

out = open("urls.txt", "w")

def addUrls(filename):
    f = (open(filename, "r")).read()
    soup = BeautifulSoup(f, 'html.parser')
    new_soup = (soup.find_all("td", {"class": "nttitle"}))
    for elem in new_soup:
        d = elem.find("a", recursive=False)["href"]
        d = d + "\n"
        out.write(d)

dirname = "entries_files"
for filename in os.listdir(dirname):
    f = os.path.join(dirname, filename)
    if os.path.isfile(f):
        addUrls(f)
