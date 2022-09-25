import random

computer_number = random.randint(1, 100)

while True:
    human_number = input("Guess the number (1-100): ")

    if not human_number.isdigit():
        print("Wrong input! Please write a number, between 1 and 100: ")
        continue
    else:
        human_number = int(human_number)
        if human_number == computer_number:
            print("You guess it!")
            break
        elif human_number > computer_number:
            print("Too High!")
        else:
            print("Too Low!")
