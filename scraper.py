import requests
from bs4 import BeautifulSoup


response = requests.get('https://samplearticlescraping.web.app')

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.get_text())