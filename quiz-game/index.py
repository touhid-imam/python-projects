import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'


def ask_question(index, question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)

    return input('Your answer: ').upper().strip()


def run_quiz(quiz):

    # Shuffle the questions
    random.shuffle(quiz)
    score = 0

    # Loop over questions
    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])

        if answer == item['answer']:
            cprint('Correct!', 'green')
            score += 1
        else:
            cprint(f'Wrong! the correct answer is {item[ANSWER]}', 'red')

        print()

    print(f'Quiz Over! Your Final Score is {score} out of {len(quiz)}')


def main():
    # Define question, option and correct answer
    quiz = [
        {
            QUESTION: 'What is capital of Franch?',
            OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
            ANSWER: 'C'
        },
        {
            QUESTION: 'What is the largest planet in our solar system?',
            OPTIONS: ['A. Earth', 'B. Jupiter', 'C. Mars', 'D. Saturn'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'Who wrote the play "Romeo and Juliet"?',
            OPTIONS: ['A. William Shakespeare', 'B. Charles Dickens', 'C. J.K. Rowling', 'D. Mark Twain'],
            ANSWER: 'A'
        },
        {
            QUESTION: 'What is the capital city of Japan?',
            OPTIONS: ['A. Seoul', 'B. Tokyo', 'C. Beijing', 'D. Bangkok'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'Which ocean is the largest?',
            OPTIONS: ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Pacific Ocean', 'D. Arctic Ocean'],
            ANSWER: 'C'
        }
    ]

    run_quiz(quiz)


if __name__ == '__main__':
    main()
