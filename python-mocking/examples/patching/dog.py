import requests as requests


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

    def get_profile(self):
        response = requests.get("http://www.dogbook.com/{}".format(self.name))

        if response.status_code == 200:
            return response.json()

