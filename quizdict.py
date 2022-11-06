# coding=utf8
from geturl import get_url, get_postapi_false, get_postapi_true
import json
import requests
import pprint
import random



#  Ger tillbaks en siffra mellan 0-100
def get_percent(a, b):
    return 100 * (a / b)


#  Ger tillbaks en variabel som heter percent
def get_percent_var(question):
    hela = int(question['times_asked'])  # Tar nyckeln 'times_asked' som har ett nummer i sig och konverterar det till int
    delen = int(question['times_correct'])  # Tar nyckeln 'times_correct' som har ett nummer i sig och konverterar det till int
    percent = int(get_percent(delen, hela))  # Kallar på get_percent funktionen som har som uppgift att dividera delen i det hela och lägger resultat i en variabel som heter percent samt gör om det till int
    return percent


#  Hämtar all data från API:et



# Skriver ut "Fel! Rätt svar är: rätta svaret"
def print_correct_answers(question):
    for answer in question['answers']:
        if answer['correct']:
            print(f"Fel! Rätt svar är: {answer['answer']}")


# Gör så att man kan skriva ett ogiltigt svar i en While loop(En bokstav eller för hög/låg siffra)
def get_user_answer(max_num: int, prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
        except ValueError:
            pass
        if user_input in range(1, max_num + 1):
            break
        print(f"Skriv ett nummer mellan 1 - {max_num}")
    return user_input


#  ger tillbaks rätt svar och ditt svar
def get_your_and_correct_answer(answers, i, selected_answer):  # Hämtar rätt svar och det man svarade
    your_answer = selected_answer['answer']
    correct_answer = answers[i]['answer']
    return correct_answer, your_answer


def main():

    data = get_url()

    wrong_questions_list = []

    score = 0

    for a, question in enumerate(random.sample(data['questions'], 10)):  # En loop med ett index(a) som startar på 0, och som tar ut all data från nyckeln 'questions'

        percent = get_percent_var(question)

        print(f"Fråga. {a+1} [{percent}% har svarat rätt] {question['prompt']}") # printar ut alla
        answers = question['answers']
        for i, answer in enumerate(answers):  # En loop med ett index(i) som startar på 1, och som tar ut element från nyckeln 'answers'
            print(f"{i + 1}. {answer['answer']}")

        user_input = get_user_answer(len(question['answers']), ">>")

        answers = question['answers']

        selected_answer = answers[user_input - 1]

        if selected_answer['correct']:
            get_postapi_true(question)
            score = score + 1
            print("")
            print(f"Rätt svar! Du har {score} poäng.\n")
        else:
            get_postapi_false(question)
            print_correct_answers(question)
            correct_answer, your_answer = get_your_and_correct_answer(answers, i, selected_answer)
            wrong_questions_list.append((question['prompt'], your_answer, correct_answer))

    print(f"Du har sammanlagt fått {score} poäng av {a + 1}\n")
    if score < 10:
        print(f"Du svarade fel på dessa frågor: ")
    elif score == 10:
        print("Du hade rätt på alla frågor!")
    else:
        print("??")
    for item in wrong_questions_list:
        print(item[0])  # itererar igenom listan(wrong_questions_list) element 0 som är [q['prompt']
        print(f"Ditt svar: {item[1]}")
        print(f"Rätt svar: {item[2]}\n")


if __name__ == '__main__':
    main()
