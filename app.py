#!/usr/bin/python

from lxml import html
import requests
import re
import os
import tweepy

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])

tweepy = tweepy.API(auth)

page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
tree = html.fromstring(page.content)

stories = tree.xpath('//div[@id="mp-otd"]/ul[1]/li')

for story in stories:
    story = re.sub('<[^<]+>|\\n', "", html.tostring(story, encoding="ascii")).replace("&#8211;", "-")
    if len(story) <= 140:
        tweepy.update_status(story)
        break
