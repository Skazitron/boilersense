import requests
from bs4 import BeautifulSoup
from pprint import pprint


with open('entries.html', 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')
newdata = soup.findAll("td", {"class" : "nttitle"})



headers = {
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}



t = requests.get("https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=202310&subj_code_in=WGSS&crse_numb_in=68100", headers=headers)
pprint(t.content)

