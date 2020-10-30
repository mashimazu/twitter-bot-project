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


def Rodar():
    pesquisa = "\"bom dia\"" + " -filter:retweets"
    results = api.search(q=pesquisa,count=1)
    for i in results:
        api.retweet(i.id)
    
def Ciclo():
    while True:
        h=time.localtime().tm_hour
        m=time.localtime().tm_min
        s=time.localtime().tm_sec
        s=s+(m*60)+(h*3600)
        esperar=(randrange(21600)+(86400 - s)+21600)
        time.sleep(esperar)
        Rodar()
        
        
Ciclo()
