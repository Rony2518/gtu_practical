import requests
from bs4 import BeautifulSoup

def fetch(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None
    
url = "http://example.com"
data = fetch(url)
if data is not None:
    print(data)
else:
    print("Failed to get data")

soup = BeautifulSoup(data, 'html.parser')

print(soup.title.string)
