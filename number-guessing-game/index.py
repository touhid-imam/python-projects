import random

guess_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 to 100: "))

        if guess < guess_number:
            print('Too Low!')
        elif guess > guess_number:
            print('Too High!')
        else:
            print('Congratulations! You guessed the number.')
            break

    except ValueError:
        print("Please Enter a valid number.")
