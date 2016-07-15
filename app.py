#!/usr/bin/python

from lxml import html
import requests
import re
import os
import tweepy
import time
import random

class DailyWikiBot:
    def __init__(self):
        auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
        auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
        self.tweepy = tweepy.API(auth)

    def parse(self, facts):
        parsedFacts = []
        for fact in facts:
            fact = re.sub('<[^<]+>|\\n', '', html.tostring(fact, encoding='UTF-8'))
            if len(fact) <= 140: parsedFacts.append(fact)
        return parsedFacts

    def run(self):
        page = requests.get('https://en.wikipedia.org/wiki/{0}_{1}'.format(time.strftime('%B'), time.strftime('%d')))
        facts = self.parse(html.fromstring(page.content).xpath('//div[@id="mw-content-text"]/ul[1]/li'))

        self.tweepy.update_status(random.choice(facts))


bot = DailyWikiBot()
bot.run()
