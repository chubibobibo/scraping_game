# https://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup

# create a request to the site to be scrape
response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser') # passing the response (which is a text to BS to parse
# print(soup.body) # prints the html body of the first page of the site

# quotes = soup.select('.quote')
# quotes = soup.find(class_='text')
# NOTE: all quotes are in a span with a class of 'text'
quotes = soup.select('.text') # returns a list of all quotes in a list
author = soup.select('.author')
# print(author)

#create a list where we are going to store the quotes.
all_quotes = []

# loop through the list of quotes and use get_text() method to each of the quotes to obtain just the inner text
for each_quote in quotes:
    all_quotes.append({'text': each_quote.get_text(), 'author': each_quote.find_next_sibling().find(class_='author').get_text()})
    print(all_quotes)
    
