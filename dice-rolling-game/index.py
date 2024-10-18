import random

counter = 1
dice_count = 0

while True:
    if counter <= 1:
        dice_count = int(input('How Many Time You Want to roll the Dice?:'))
    print(counter)
    print(dice_count)
    choice = input("Please Roll the dice! (y/n): ").lower()
    if choice == 'n' or counter == dice_count:
        print('Thanks for playing')
        break
    elif choice == 'y':
        counter += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    else:
        print('Invalid choice.')
