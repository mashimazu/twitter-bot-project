import tweepy
import time
from random import randrange
import os
from os import environ

CONSUMER_KEY=environ['CONSUMER_KEY']
CONSUMER_SECRET=environ['CONSUMER_SECRET']
ACCESS_KEY=environ['ACCESS_KEY']
ACCESS_SECRET=environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#ola mundo
print("iniciou a nova versao")

def Rodar():
    pesquisa = "\"minha opiniao\"" + " -filter:retweets"
    results = api.search(q=pesquisa,count=1)
    for i in results:
        api.retweet(i.id)
    
def Ciclo():
    while True:
        x = randrange(21600)
        time.sleep(x)
        Rodar()
        time.sleep(21600-x)
        
Ciclo()
