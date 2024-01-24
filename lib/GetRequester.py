import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response= requests.get(URL)
        return response.content

    def load_json(self):
        python_list=[]
        requests=json.loads(self.get_response_body())
        for request in requests:
            python_list.append(request["agency"])

get_requester=GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()


