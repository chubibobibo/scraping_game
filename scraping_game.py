# https://quotes.toscrape.com/

# @NOTE: sleep allows us to space out our requests
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

# creating variables for the url's to allow us to modify it dynamically.
base_url = 'https://quotes.toscrape.com'
url = '/page/1/'


# print(soup.body) # prints the html body of the first page of the site

    #create a list where we are going to store the quotes.
all_quotes = []
# loop that will allow us to navigate to different pages.abs
while url:
    print(f'Now scraping {base_url}{url}')
    # create a request to the site to be scrape using the url variables
    response = requests.get(f'{base_url}{url}')
    soup = BeautifulSoup(response.text, 'html.parser') # passing the response (which is a text to BS to parse
    # quotes = soup.select('.quote')
    # quotes = soup.find(class_='text')
    # NOTE: all quotes are in a span with a class of 'text'
    quotes = soup.select('.text') # returns a list of all quotes in a list
    # author = soup.select('.author')
    # print(author)

    # loop through the list of quotes and use get_text() method to each of the quotes to obtain just the inner text
    # we do the same for the author by finding the next sibling and looking for the class author.
    # to  get the href tag, we need to find the element with author class and since the href tag is it's sibling, we are able to access it using find_next_sibling. and using brackets to obtain the href attribute.
    for each_quote in quotes:
        all_quotes.append({
            'text': each_quote.get_text(), 
            'author': each_quote.find_next_sibling().find(class_='author').get_text(),
            'link': each_quote.find_next_sibling().find(class_='author').find_next_sibling()['href']})
    # print(all_quotes)

    next_btn = soup.find(class_ = 'next') # looks for the class of the next button
    if next_btn:
        btn_link = next_btn.find('a')['href'] # accesses the link in the anchor tag in the element with the class 'next
        # print(btn_link)
        url = btn_link if btn_link else None
    else:
        url = None
    # print(btn_link)
    # sleep(2)# argument in seconds
# print(all_quotes)

#=============================== Game Logic=============================
random_quote = choice(all_quotes)
# print(f'This is a random quote: {random_quote['text']}')
print(f'This is the author: {random_quote['author']}')

chances = 3
user_input = ''

while user_input.lower() != random_quote['author'].lower() and chances > 0 :
# while chances > 0 :
    if chances == 3:
        print('Here is a random quote...')
        print(random_quote['text'])
        print(f'Try to guess the author. Guesses remaining {chances} ')
    user_input = input()
    chances -= 1
    if chances == 0 and user_input.lower() != random_quote['author'].lower():
        print(f'You guessed wrong. Chances left {chances}')
        print('Game over')
        break
    elif chances > 1:
        print(f'You guessed wrong. Try Again. Chances left {chances}')
        print('Here is a hint to help you out:')
        print(f'The author of this quote is: {random_quote['author']}')
    elif chances == 1:
            # obtain a new request using the "link" key in our random_quote dictionary to obtain author's birthdate
            response = requests.get(f'{base_url}{random_quote['link']}')
            # print(response.text)
            soup = BeautifulSoup(response.text, 'html.parser')
            author_date = soup.find(class_='author-born-date').get_text()
            author_location = soup.find(class_='author-born-location').get_text()
            print('You guessed wrong, Here is another tip')
            print(f"The author's birthdate is: {author_date} ")
        # print(author_date)
    # else:
    #     print(f"The first letter of the author's surname is: {random_quote['author'][0] }")
print('You got it')
        


        

