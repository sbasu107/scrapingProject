import requests
from bs4 import BeautifulSoup

website_url = 'https://samplearticlescraping.web.app'
response = requests.get(website_url)

soup = BeautifulSoup(response.text, 'html.parser')
article_contents = soup.get_text()

print(article_contents)

