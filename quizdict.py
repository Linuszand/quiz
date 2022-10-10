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

    answers = question['answers']
    selected_answer = answers[user_input - 1]

    if selected_answer['correct']:
        score = score + 1
        print("")
        print(f"Rätt svar! Du har {score} poäng.\n")
        # print(selected_answer['answer'])
    else:
        for i, answer in enumerate(question['answers']):
            # print(answers[i]['answer'])
            # print(answers[i]['correct'])
            correct_answer = answers[i]['answer']
            if answers[i]['correct']:
                print("")
                print(f"Fel! Rätt svar är: {correct_answer}")
                print(f"Du har {score} poäng.\n")


print(f"Du har sammanlagt fått {score} poäng av {a}")


def main():
    pass


main()
