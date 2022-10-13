# coding=utf8
import requests


def get_questions_data():
    url = 'https://bjornkjellgren.se/quiz/v1/questions'
    results = requests.get(url)
    data = results.json()
    return data


def print_answers_loop(question):
    for i, answer in enumerate(question['answers'], start=1):
        print(f"{i}. {answer['answer']}")


def get_answers_data(question):
    answers = question['answers']
    return answers


def get_selected_answer(answers, user_input):
    selected_answer = answers[user_input - 1]
    return selected_answer


def score_plus_and_print_correct_answer(score):
    score = score + 1
    print("")
    print(f"Rätt svar! Du har {score} poäng.\n")
    return score


def get_correct_answer(answers, i):
    correct_answer = answers[i]['answer']
    return correct_answer


def score_plus_and_print_wrong_answer(correct_answer, score):
    print("")
    print(f"Fel! Rätt svar är: {correct_answer}")
    print(f"Du har {score} poäng.\n")
