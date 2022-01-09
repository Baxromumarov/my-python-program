from newspaper import Article, article
from newspaper import Article
from newspaper import fulltext
import requests
from requests.api import request


url = 'https://edition.cnn.com/interactive/2021/health/global-covid-vaccinations/'
article = Article(url, language = 'en')

print(article.text)