# coding=utf8
import requests

URL = 'https://bjornkjellgren.se/quiz/v2/questions'


def get_url():  # Hämtar alla data från urlen och gör om datan till json
    results = requests.get(URL)
    data = results.json()
    return data


def get_postapi_false(question):  # Skickar tillbaka data till api:et
    requests.post(URL, json={'id': question['id'], 'correct': False})


def get_postapi_true(question):  # Skickar tillbaka data till api:et
    requests.post(URL, json={'id': question['id'], 'correct': True})


