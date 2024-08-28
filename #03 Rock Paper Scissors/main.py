import random

player_wins = 0
computer_wins = 0

while True:
    Move = ["R", "P", "S", "Q"]
    Choice = input("\nChoose between R (Rock), P (Paper), S (Scissors) or Leave by Q: ").upper()
    
    if Choice == "R":
        print("\nYou have chosen Rock")
    elif Choice == "P":
        print("\nYou have chosen Paper")
    elif Choice == "S":
        print("\nYou have chosen Scissors")
    elif Choice == "Q":
        print("\nYou have chosen to quit. Goodbye!")
        break 
    else:
        print("\nInvalid choice, please try again.")
        continue 

    def Opponent():
        Moveset = ["rock", "paper", "scissors"]
        return random.choice(Moveset)

    Choice2 = Opponent()
    print(f"Computer chose: {Choice2}")

    def Winner(Choice, Choice2):
        Choice3 = {"R": "rock", "P": "paper", "S": "scissors"}[Choice]
        
        if Choice3 == Choice2:
            return "\nIt's a tie!"
        elif (Choice3 == "rock" and Choice2 == "scissors") or \
             (Choice3 == "paper" and Choice2 == "rock") or \
             (Choice3 == "scissors" and Choice2 == "paper"):
            return "\nYou win!"
        else:
            return "\nComputer wins!"

    result = Winner(Choice, Choice2)
    print(result)

    if result == "\nYou win!":
        player_wins += 1
    elif result == "\nComputer wins!":
        computer_wins += 1
    
    print(f"Score: Player {player_wins} - Computer {computer_wins}")


print(f"\nYou won: {player_wins} time(s)")
print(f"Computer won: {computer_wins} time(s)")
