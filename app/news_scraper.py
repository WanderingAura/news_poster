import requests
from bs4 import BeautifulSoup as bs

class NewsScraper:
    def __init__(self, url: str, headline_tag: str, a_class: str, p_class: str) -> None:
        self.h_tag = headline_tag
        self.a_class = a_class
        self.p_class = p_class

        response = requests.get(url)
        self.page = bs(response.content, "html.parser")
    
    def get_headlines(self):
        headlines2url = {}
        for tag in self.page.find_all("a", class_ = self.a_class):
            print(tag)
            headline = tag.find_next("h2")
            if headline in headlines2url:
                continue
            link = tag["href"]
            if link[0] == "/":
                link = "https://www.bbc.com" + link
            headlines2url[headline.text] = link
            return headlines2url
        
    def get_articles(self):
        headlines2url = self.get_headlines()
        articles = {}
        for h, url in headlines2url:
            response = requests.get(url)
            page = bs(response.content, "html.parser")
            paragraphs = page.find_all("p", class_=self.p_class)
            article_text = []
            for p in paragraphs:
                article_text.append(p.text)
            articles[h] = "\n".join(article_text)
        return articles

