import requests
import re
import urlparse
from BeautifulSoup import BeautifulSoup

class Scanner:
    def __init__(self, url, ignore_links):
        pass

    def extract_links_form(self, url):
        pass

    def crawl(self, url = None):
        pass

    def extract_forms(self, url):
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

           post_data