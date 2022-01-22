import requests
from bs4 import BeautifulSoup
from pprint import pprint
with open('entries.html', 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')
newdata = soup.findAll("td", {"class" : "nttitle"})



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}
t = requests.get("https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=202310&subj_code_in=WGSS&crse_numb_in=68100", headers=headers)
pprint(t.content)

