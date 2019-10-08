from datetime import datetime
import requests as requests


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


def greet_if_weekday():
    response = requests.get("http://www.awesome-greetings.com")

    if is_weekday() and response.status_code == 200:
        return response.json()["greeting"]
