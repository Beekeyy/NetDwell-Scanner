import requests
from bs4 import BeautifulSoup

f = open('parsed_html.txt', 'w')

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "https://python-scripts.com/upgrade-pip-windows"
response = request(target_url)
print(response.content )
f.write(str(response.content))