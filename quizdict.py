# coding=utf8
# from getmethods import get_questions_data, print_answers_loop, get_answers_data, get_selected_answer, \
#     score_plus_and_print_correct_answer, get_correct_answer, score_plus_and_print_wrong_answer
import json
import requests
import pprint
import random


def get_percent(a, b): # Gör om a delat på b till procent-form
    return 100 * a / b


def get_percent_variable(question):
    hela = int(question['times_asked'])  # Tar nyckeln 'times_asked' som har ett nummer i sig och konverterar det till int
    delen = int(question['times_correct'])  # Tar nyckeln 'times_correct' som har ett nummer i sig och konverterar det till int
    percent = int(get_percent(delen, hela))  # Kallar på get_percent funktionen som har som uppgift att dividera delen i det hela och lägger resultat i en variabel som heter percent samt gör om det till int
    return percent


def get_url():  # Hämtar alla data från urlen och gör om datan till json
    url = 'https://bjornkjellgren.se/quiz/v2/questions'
    results = requests.get(url)
    data = results.json()
    pprint.pprint(data)
    return data


def main():
    data = get_url()

    wrong_questions_list = []

    url = 'https://bjornkjellgren.se/quiz/v2/questions'
    params = {
        'id': 11, 'correct': True
    }

    res = requests.post(url, json=params)

    print(res.text)

    score = 0
    for a, question in enumerate(random.sample(data['questions'], 10)):  # En loop med ett index(a) som startar på 1, och som tar ut all data från nyckeln 'questions'

        percent = get_percent_variable(question)
        quest = (question['prompt']) # Tar nyckeln 'prompt' och lägger det i variabeln quest

        print(f'Fråga. {a+1} [{percent}% har svarat rätt] {quest} ') # printar ut alla
        answers = question['answers']
        for i, answer in enumerate(answers):  # En loop med ett index(i) som startar på 1, och som tar ut element från nyckeln 'answers'
            print(f"{i + 1}. {answer['answer']}")

        while True:
            user_input = (input(">>"))
            try:
                user_input = int(user_input)

            except ValueError:
                pass
            if user_input in range(1, len(question['answers']) + 1):
                break
            print(f"Skriv ett nummer mellan 1 - {len(question['answers'])}")

        answers = question['answers']

        selected_answer = answers[user_input - 1]

        if selected_answer['correct']:

            score = score + 1
            print("")
            print(f"Rätt svar! Du har {score} poäng.\n")
        else:
            for i, answer in enumerate(question['answers']):

                if answers[i]['correct']:
                    your_answer = selected_answer['answer']
                    correct_answer = answers[i]['answer']

                    print("")
                    print(f"Fel! Rätt svar är: . {correct_answer}")
                    print(f"Du har {score} poäng.")
                    wrong_questions_list.append((question['prompt'], your_answer, correct_answer)) # tar ut alla frågor, alla rätta svar och varje svar användaren gav på varje fråga och lägger sedan in dem i listan
            print(f"Ditt svar: {your_answer}\n")

    print(f"Du har sammanlagt fått {score} poäng av {a + 1}\n")
    print(f"Du svarade fel på dessa frågor: ")
    for item in wrong_questions_list:
        print(item[0])  # itererar igenom listan(wrong_questions_list) element 0 som är [q['prompt']
        print(f"Ditt svar: {item[1]}")
        print(f"Rätt svar: {item[2]}\n")


main()
