# coding=utf8
import json
import requests
import pprint


# Ta ut information från url
# lägga varje fråga och frågans alla svarsalternativ i en egen variabel
# Göra så att variabeln har ett korrekt svar.


url = 'https://bjornkjellgren.se/quiz/v1/questions'
results = requests.get(url)
data = results.json()
# pprint.pprint(data)

a = 0
score = 0
for question in data['questions']:
    a = a + 1
    print(f"Fråga {a}.")
    print(question['prompt'])

    for i, answer in enumerate(question['answers'], start=1):
        print(f"{i}. {answer['answer']}")
        # i = i + 1
    user_input = int(input(">>>"))
    # print(user_input)
    # print(type(user_input))
    # # pprint.pprint(question['answers'])

    answers = question['answers']

    selected_answer = answers[user_input - 1]

    if selected_answer['correct']:
        score = score + 1
        print(f"Rätt svar! Du har {score} poäng.\n")
    else:
        print(f"Ditt svar: {user_input}\n")
        # print(f"Fel! Rätt svar: {correct_answer}")
print(f"Du har sammanlagt fått {score} poäng av {a}")




def main():
    pass







main()






































