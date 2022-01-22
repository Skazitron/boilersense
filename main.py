import spacy
from rake_nltk import Rake
rake = Rake()
from spacytextblob.spacytextblob import SpacyTextBlob
import re
import pandas as pd
df = pd.DataFrame(columns = ["features", "difficulty"])
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
from bs4 import BeautifulSoup as bs
import requests

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getFeatures(sentence):
    # kw = rake.extract_keywords_from_text(sentence)
    # ranked_phrases = rake.get_ranked_phrases()
    # features = ""
    # for word in ranked_phrases:
    #
    #     if(len(word)>=5):
    #         res = re.sub(r'[^\w\s]', '', word)
    #         features+=res + " "
    # print(features)
    return ' '.join(dict.fromkeys(sentence.split()))
#'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=187591'
def get_web_data(url):
    r = requests.get(url)
    soup = bs(r.content, "html.parser")
    #-dzzyvm-0 gRjWel
    arr_text = soup.find_all("div", class_="Comments__StyledComments-dzzyvm-0 gRjWel")
    arr_rating = soup.find_all("div", class_="CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cDKJcc")
    arr_quality = soup.find_all("div", class_="CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cDKJcc")
    label = []
    text = []
    qual = []
    for i in range(len(arr_text)):
        text.append(arr_text[i].text)
        label.append(arr_rating[i].text)
        qual.append(arr_quality[i].text)
    return label, text, qual
easyLinks = [
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=28473',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132707',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=833507',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1128147',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=232063',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=131995',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=94745',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=965479',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1833876',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2447383',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132088',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=308662',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=435420',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2218951',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1755190',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=133455',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=99252',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=70480',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=134509',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=195834',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=531902',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=682041',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=497809',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=5976',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1123718',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=135247',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=103842',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=129099',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=339885',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=176357',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=466454',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=195832',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1249958',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=147224',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=460753',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=814256',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1128147',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=120370',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2193908',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=168181',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2544740',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=172866',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=192750',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=232063',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=11656',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132517',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=534256',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=521826',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=14775',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=99501',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=48793',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=360583',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=165495',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=775938',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=264516',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=383410',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=451803',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=349375',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=569250',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=541466',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=355069',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=349916',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1042683',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=218975',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2223232',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=382567',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=202976',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=350445',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2097557',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=421689',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=421705',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1328345',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2127942',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=472592',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=165780',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=895385',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=880661',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=573806',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=81530',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=342981',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=389442',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1368844',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=378337',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=81676',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=94747',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1393617',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=7589',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=113360',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=163354',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=154677',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=386757',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=196360',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=462933',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2222745',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1395999',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=196341',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1837362',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=196446',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=612157',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=893536',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=196505',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=257412',
]

mediumLinks = [
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132346',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=161868',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1302653',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1179367',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=338509',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=190864',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=6036',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1217029',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=191323',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=256683',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=147201',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1971770',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=885702',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=335128',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1428347',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=612322',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=131778',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=554801',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1104121',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=345658',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1719020',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1075885',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=363258',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=600146',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=347372',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1216148',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=347372',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=864995',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=788144',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1515305',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=736051',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1104517',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1179367',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=165460',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=170605',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=393225',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=196444'
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132120',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=151966',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=313571',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=574202',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=323778',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=333470',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=441295',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=537630',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=826849',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=153782',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=191323',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=349981',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=256683',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=256109',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=510770',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=545248',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=608862',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=788164',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=28468',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=64565',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=976267',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132579',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=136336',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=157971',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=318510',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=160006',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=165527',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=339272',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=165788',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=343279',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=553522',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=353912',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=441295',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=456504',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=11654',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=356986',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=471885',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=316238',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=472584',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=472587',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=534247',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=537630',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=363258',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=457757',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=343687',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=569904',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=694690',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=831064',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1715721',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=374605',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=788164',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=86665',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=826849',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=988472',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=895908',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=147201',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=373568',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1126317',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=611818',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=612154',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=976267',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1190369',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2253163',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2408256',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1861095',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=196523',
]

hardLinks = [
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=47353',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=783139',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=63745',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=575677',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1232956',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=355059',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=426798',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=147206',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1960869',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=535265',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2075255',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=224125',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=389874',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=892096',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1774714',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=382188',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=135266',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=533507',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=803985',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=566912',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=303831',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=131325',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2105752',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=535349',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1197692',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=821806',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1048973',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=286008',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1431146',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=504294',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=363749',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=94485',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1771533',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=489410',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=344398',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=405601',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=320049',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1939289',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=251311',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=474547',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=760519',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=139301',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132476',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=895132',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=131258',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=630122',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2075130',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=251147',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=356179',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=803985',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=147364',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2215255',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1063606',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=177434',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=381607',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=208568',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=278350',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=340755',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=387214',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1630983',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=815895',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=363749',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1119431',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2030166',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=354097',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=271662',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=99126',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=6152',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=132608',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=151046',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=474547',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=608147',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=133160',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1965599',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=136643',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=348276',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1865887',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1472098',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=119114',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=136643',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=137018',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=164440',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=137065',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=165516',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=323037',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=333810',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=390997',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1807410',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=426170',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=447359',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1690422',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=164804',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1292631',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=576190',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=1189231',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=472594',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=99129',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=534023',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=195819',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=153186',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=481944',
    'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=494726',
]
links = easyLinks + mediumLinks + hardLinks

for link in links:

    labels, text, qual = get_web_data(link)

    for i in range(len(labels)):
        label_val = 0
        qual_label = 0
        if(float(labels[i])<=3):
            label_val = 1
        else:
            label_val = 2
        if(float(qual[i])<=2):
            qual_label = 2
        else:
            qual_label = 3
        # elif(float(labels[i])>3 and float(labels[i])<=4):
        #     label_val = 2
        # elif(float(labels[i])>=4):
            #label_val = 3
        # if(float(labels[i])<=3.6):
        #     label_val = 1
        # else:
        #     label_val = 2
        df = df.append({"features": getFeatures(text[i]), "difficulty": label_val, "quality":qual_label}, ignore_index=True)

df.to_csv("/Users/shellyschwartz/Downloads/boilermakeData2.csv")