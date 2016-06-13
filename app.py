#!/usr/bin/python

from lxml import html
import requests
import re

page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
tree = html.fromstring(page.content)

#This will create a list of stories:
stories = tree.xpath('//div[@id="mp-otd"]/ul[1]/li')

tweets = []
for story in stories:
    tweets.append(re.sub('<[^<]+>|\\n', "", html.tostring(story, encoding="ascii")).replace("&#8211;", "-"))

print 'Tweets: ', tweets
