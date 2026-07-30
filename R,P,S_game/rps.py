import random

comp_score = 0
player_score = 0
welcome = ("Welcome to Rock, Paper, Scissors!")
menu = ("1. Rock,\n2. Paper,\n3. Scissors")
comp = ["Rock", "Paper", "Scissors"]

while True:
    print(welcome)
    print(menu)

    option = (int(input("What do you choose?: ")))
    if option not in [1, 2, 3]:
            print("Invalid Input")
            continue

    comp_op = random.randint(1,3)

    print("Computer chose:", comp[comp_op -1])
    
    if option == comp_op:
        print("Draw!")

    elif option == 1 and comp_op == 3:
        print("You Win!")
        player_score += 1

    elif option == 2 and comp_op == 1:
        print("You Win!")
        player_score += 1
    elif option == 3 and comp_op == 2:
        print("You Win!")
        player_score += 1
    else:
        print("Computer Wins")
        comp_score += 1
    
    play_again = input("Would you like to play again? (Y/N):\n ")
    if play_again.upper() == "Y":
        print("Player Score:",player_score, "Computer Score:", comp_score)

    else:
        print("Final Scores:")
        print("Player Score:", player_score)
        print("Computer Score:", comp_score)
        print("Thanks for playing")
        break
        
