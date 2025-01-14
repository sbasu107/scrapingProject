import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

website_url = 'https://samplearticlescraping.web.app'
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

requests_response = requests.get(website_url)

#Clean response using BeautifulSoup
soup = BeautifulSoup(requests_response.text, 'html.parser')
article_contents = soup.get_text()

question = "Explain the benefits of tofu that the following article points out."

#Set Gemini model and feed input here
model = genai.GenerativeModel('gemini-1.5-pro')
llm_response = model.generate_content(question + " : " + article_contents, stream=True)

for chunk in llm_response:
    print(chunk.text, end='')

with open("scrapingProj/response.txt", "w") as file:
    file.write(llm_response.text)