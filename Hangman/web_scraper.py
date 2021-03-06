"""Web Scraper."""
import requests
from bs4 import BeautifulSoup

# Scrape makeschool's website for words - Beautiful soup

# specify the url
quote_page = "https://www.makeschool.com"

# query the website and return the html to the variable ‘page’
page = requests.get(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page.content, "html.parser")


def all_pages(soup):
    """Return a list of all the links found on the page."""
    links = []
    for link in soup.findAll('a'):
        if link.get('href'):
            if link.get('href')[0] == "/":
                ms_link = "https://makeschool.com" + str(link.get('href'))
                if ms_link not in links:
                    links.append(ms_link)
                    # Uncomment to see all links: print(ms_link)
    return links


def words(soup):
    """Return list of words pulled from soup text.

    Filter out non-words and words under 4 characters
    """
    # Pull text from web pages
    word_text = soup.get_text()
    words = word_text.split(" ")

    # Filter out short words and non-words
    words = list(filter(lambda x: len(x) > 4, words))
    words = list(filter(lambda x: x.isalpha(), words))

    # Convert words to lower case
    words = list(filter(lambda x: x.lower(), words))
    return words


def word_list(soup):
    """Return the word list."""
    word_list = []
    links = all_pages(soup)
    for link in links:
        quote_page = str(link)
        page = requests.get(quote_page)
        soup = BeautifulSoup(page.content, "html.parser")
        word_list.extend(words(soup))
    return word_list


word_list(soup)
