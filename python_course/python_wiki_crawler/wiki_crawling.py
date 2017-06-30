import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Science"
article_chain = [start_url]


def continue_crawl(search_history, target_url):
    """
    Function to check current url to decide if the crawling while loop should continue.
    :param search_history: an array holding all urls that have been clicked, including current page
    :param target_url: the url of the science article, our stopping point
    :return:    if the current url matches target - false, stop loop
                if the loop has run more than 25 times - false, stop loop
                if the current url has already been visited - false, stop loop
                else - true,continue loop
    """
    if search_history[-1] == target_url:
        print("You made it to the science article! That's the end!")
        return False
    elif len(search_history) > 25:
        print("We've been at this for 26 clicks. I think we'll stop here.")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("Wait! Come back! Bender's stuck in a loop!")
        return False
    else:
        print("Onwards! To the science article!")
        return True


def find_first_link(article_url):
    """
    Function to crawl the article_url, parse it with beautifulsoup, and return the first <a> tag from the body
    :param article_url: the starting article url, where the crawl will happen
    :return: the string url of the first <a> tag located in the article body, or None if no <a>
    """
    req = requests.get(article_url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    first_article_link = None
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_article_link = element.find("a", recursive=False).get('href')
            break

    if not first_article_link:
        return

    full_first_link = urljoin('https://en.wikipedia.org/', first_article_link)
    return full_first_link


while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])

    if not first_link:
        print("Oh no! A page with no links. End of the road buddy!")
        break

    # add the first link to the article_chain
    article_chain.append(first_link)
    # delay ~ 2 seconds
    time.sleep(2)
    print(article_chain)
    print(len(article_chain))
