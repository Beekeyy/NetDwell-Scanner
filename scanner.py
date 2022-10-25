from urllib import response
import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []

    def extract_links_form(self, url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', str(response.content))

    def crawl(self, url):
        href_links = self.extract_links_form(url)
        for link in href_links:
            link = urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)


"""     def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content)
        return parsed_html.findAll("form")

    def submit_for(self, form, value, url):
        action = form.get("action")
        post_url = urlparse.urljoin(url, action)
        method = form.get("method")

        inputs_list = form.findAll("input")
        post_data = {}
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = "test"

           post_data """