import random

print("Welcome. This is a simple game of ROCK PAPER SCISSORS. To  win \n" +
      "ROCK Vs PAPER >> PAPER wins \n" + "ROCK Vs SCISSORS >> ROCK wins\n" + "PAPER Vs SCISSORS >> SCISSORS wins")

while True:
    print("Enter your choice \n 1: Rock \n 2: Paper \n 3: Scissors ")

    try:
        choice = int(input(">>> "))
        while choice < 1 or choice > 3:
            choice = int(input("invalid input, enter a valid one: "))
    except:
        print('invalid input')
        continue

    if choice == 1:
        choice_user = 'Rock'
    if choice == 2:
        choice_user = 'Paper'
    if choice == 3:
        choice_user = 'Scissors'

    print(f"Your choice is: {choice_user}")
    print("It is now the Computer's turn")

    choice_comp = random.randint(1, 3)
    while choice_comp == choice:
        choice_comp = random.randint(1, 3)

    if choice_comp == 1:
        choice_comp_name = 'Rock'
    if choice_comp == 2:
        choice_comp_name = 'Paper'
    if choice_comp == 3:
        choice_comp_name = 'Scissors'

    print(f"The computer's choice is: {choice_comp_name}")
    print(" USER Vs COMPUTER \n")

    if((choice == 1 and choice_comp == 2) or (choice == 2 and choice_comp == 1)):
        print("Paper wins!!!")
        result = 'Paper'
    elif((choice == 1 and choice_comp == 3) or (choice == 3 and choice_comp == 1)):
        print("Rock wins!!!")
        result = "Rock"
    else:
        print("Scissors wins!!!")
        result = "Scissors"

    if result == choice_user:
        print("<==User wins==>")
    else:
        print("<==Computer wins==>")

    print('Do you want to play again?? (Y/N)')
    answer = input()
    if answer == 'n' or answer == "N":
        print("Thank you for your time :)")
        break
    elif answer == 'y' or answer == "Y":
        continue
    else:
        print("invalid input")

print("Thanks for playing my game")
