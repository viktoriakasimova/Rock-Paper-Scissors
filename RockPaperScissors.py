from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    print(f"(Type 'q' or 'quit' to finish the game)\n")

    p_choice = input("Enter Player's Choice: ").lower()
    if p_choice == "quit" or p_choice == "q":
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"The computer plays {computer}")

    if p_choice not in ["rock", "paper", "scissors"]:
        print("Something went wrong.")
    elif p_choice == computer:
        print("TIE!\n")
    elif (p_choice == "paper" and computer == "rock") or (p_choice == "rock" and computer == "scissors")\
    or (p_choice == "scissors" and computer == "paper"):
        print("Player wins\n")
        player_wins += 1
    else:
        print("Computer wins\n")
        computer_wins += 1

if player_wins > computer_wins:
    print("CONGRATS! YOU WON!")
elif player_wins < computer_wins:
    print("SORRY, THE COMPUTER WON...")
else:
    print("IT'S A TIE")
print(f"FINAL SCORES... Player: {player_wins} Computer: {computer_wins}")