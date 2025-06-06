import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()