from os import path
from faker import Faker
from random import randint
import requests

COUNT = 500                         # count of data that will be generated
API_URL = "http://127.0.0.1:8080"   # service URL


AVATAR = "blue-simple-avatar.png"
GENDERS = {"M": "male", "F": "female"}
CREATE_URI = "/api/human/"

def genarate_humans(faker):
    humans = []

    for _ in range(COUNT):
        profile = faker.simple_profile()
        name = profile["name"].split()

        human = {
            "avatar": AVATAR,
            "first_name": name[0],
            "second_name": name[1],
            "age": randint(1, 140),
            "gender": GENDERS[profile["sex"]],
        }
        humans.append(human)
    return humans


def post_human(url, data):
    files = {"avatar": (data["avatar"], open(path.join("fake", data["avatar"]), "rb"))}
    response = requests.post(url, data=data, files=files)

    response.raise_for_status()


if __name__ == "__main__":
    faker = Faker()
    humans = genarate_humans(faker)

    for human in humans:
        post_human(API_URL + CREATE_URI, human)
