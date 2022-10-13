# coding=utf8
from getmethods import get_questions_data, print_answers_loop, get_answers_data, get_selected_answer, \
    score_plus_and_print_correct_answer, get_correct_answer, score_plus_and_print_wrong_answer


def main():
    data = get_questions_data()  # Tar ut informationen från url:en med hjälp av requests och gör om det till json() så att vi kan använda informationen.

    score = 0  # En variabel med värdet 0 int

    for a, question in enumerate(data['questions'], start=1): # En loop som tar datan från en lång lista med frågor
        print(f"Fråga {a}.") # printar ut Fråga. och index som har start 1
        print(question['prompt'])  # printar ut alla frågar var för sig i en loop

        print_answers_loop(question)  # Skriver ut svaren för varje enskild fråga

        user_input = int(input(">>>"))  # Variabeln user_input får det värde vi väljer att skriva in

        answers = get_answers_data(question)  # Tar ut all data i 'answer' nycklarna

        selected_answer = get_selected_answer(answers, user_input)  # Det vi skrev in i user_input variabeln konsollen. Det svaret du skrev in: (1,2,3 eller 4) minus ett i index

        if selected_answer['correct']:  # Om det svaret man gissade på har värdet True i 'correct' nycklarna så kör den koden nedan

            score = score_plus_and_print_correct_answer(score)  # Printar ut om man hade rätt samt poäng efter svaret

        else:
            for i, answer in enumerate(question['answers']):  # en loop som tar ut datan från nyckeln 'answers'

                correct_answer = get_correct_answer(answers, i)  # Tar ut alla nyckar från 'answer' som vi sedan använder i if satsen nedan

                if answers[i]['correct']:  # Loopar igenom varje 'correct' nyckel och printar bara ut det om värdet är True

                    score_plus_and_print_wrong_answer(correct_answer, score)  # Printar ut om man hade fel och vilket svar som var rätt samt vilket poäng man har efter svaret

    print(f"Du har sammanlagt fått {score} poäng av {a}. ")


if __name__ == '__main__':
    main()
