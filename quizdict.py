# coding=utf8
# from getmethods import get_questions_data, print_answers_loop, get_answers_data, get_selected_answer, \
#     score_plus_and_print_correct_answer, get_correct_answer, score_plus_and_print_wrong_answer
import json
import requests
import pprint
import random


# 1. Programmet kraschar ibland om jag råkar trycka på retur utan att ha skrivit in något eller om jag skriver något annat än siffror. Om frågan har 4 svar skall bara siffrorna 1-4 accepteras som input.
# 2. Välj ut 10 slumpmässiga frågor av dem ni får från APIet.
# 3. När jag besvarat alla frågor vill jag att programmet skriver ut de frågor jag svarade fel på tillsammans med det rätta svaret.


def get_percent(a, b): # Gör om a delat på b till procent-form
    return 100 * a / b

def get_url(): # Hämtar alla data från urlen och gör om datan till json
    url = 'https://bjornkjellgren.se/quiz/v2/questions'
    results = requests.get(url)
    data = results.json()
    return data
def main():
    data = get_url()


    wrong_questions_list = []

    score = 0
    for a, question in enumerate(random.sample(data['questions'], 10)):  # En loop med ett index(a) som startar på 1, och som tar ut all data från nyckeln 'questions'

        # q = data['questions'][a] # q tar ut varje element från nyckeln 'answers' först data['questions'][0], sen data['questions'][1] osv...
        # q gjorde så att ett fel uppstod, men jag vet inte exakt varför. När jag tog bort q fixade allt sig i alla fall!

        hela = int(question['times_asked']) # Tar nyckeln 'times_asked' som har ett nummer i sig och konverterar det till int
        delen = int(question['times_correct']) # Tar nyckeln 'times_correct' som har ett nummer i sig och konverterar det till int

        percent = int(get_percent(delen, hela))  #  Kallar på get_percent funktionen som har som uppgift att dividera delen i det hela och lägger resultat i en variabel som heter percent samt gör om det till int

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
                    print(f"Fel! Rätt svar är: {correct_answer}")
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
