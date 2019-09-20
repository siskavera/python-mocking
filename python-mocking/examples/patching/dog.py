import requests as requests


class Dog:
    def __init__(self, name, sleeping_hour=23, waking_hour=7):
        self.name = name
        self.sleeping_hour = sleeping_hour
        self.waking_hour = waking_hour

    def bark(self):
        return "Woof!"

    def get_pedigree(self):
        response = requests.get("http://www.dog-pedigree.com/{}".format(self.name))

        if response.status_code == 200:
            return response.json()

