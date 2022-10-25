from urllib.parse import urlparse
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

f = open('parsed_html.txt', 'w')

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "https://edu.isuct.ru/login/index.php"
response = request(target_url)
#f.write(str(response.content))

parsed_html = BeautifulSoup(response.content, features="html.parser")

forms_list = parsed_html.findAll("form")#finding form tegs

for form in forms_list:
    action = form.get("action")#getting action
    post_url = urljoin(target_url, action)#link aggregation
    method = form.get("method")#getting method

    inputs_list = form.findAll("input")#getting input
    post_data = {}
    for input in inputs_list:
        input_name = input.get("name")#getting name
        input_type = input.get("type")#getting type
        input_Value = input.get("value")#getting value
        if input_type == "text":
            input_Value = "test"

        post_data[input_name] = input_Value
        result = requests.post(post_url, data=post_data)
        print(result.content)
        