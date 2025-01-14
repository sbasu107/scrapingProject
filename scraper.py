import requests
from bs4 import BeautifulSoup


response = requests.get('https://samplearticlescraping.web.app')

soup = BeautifulSoup(response.text, 'html.parser')
article_contents = soup.get_text()

print(article_contents)

