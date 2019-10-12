import requests as requests


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

    def get_pedigree(self): # TODO Rename
        response = requests.get("http://www.dog-pedigree.com/{}".format(self.name))

        if response.status_code == 200:
            return response.json()

