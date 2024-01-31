import requests as reqw
from bs4 import BeautifulSoup as bs
import random
import time

def req_user_token():
    token = input("Paste your auth token:")
    token = token.strip()
    return token

def parse(url: str):
    page = reqw.get(url)
    soup = bs(page)
    poll = soup.find(id='pollQuestionsContainer')
    if poll is not None:
        answer_question(poll, req_user_token())
    
def answer_question(poll, session_token):
    form = poll.findChildren("form", recursive=True)[0]
    answer = random.choice(form.findChildren("a", recursive=True))
    submit_link = 'https://www.openhotseat.org' + answer['href']
    reqw.post(submit_link, cookies={'ASP.NET_SessionId': session_token})

urls = [f'https://www.openhotseat.org/Topic/Poll/6176{id}' for id in range(4, 10)]

while True:
    for url in urls:
        parse(url)
    time.sleep(100)