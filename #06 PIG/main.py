import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll
    
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4")
    else:
        print("Invalid, try again")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "'s turn has just started")
        print("Your total score is:", player_scores[player_idx] ,"\n")
        current_score = 0

        while True:
            roll_choice = input("Would you like to roll (y)? ")
            if roll_choice.lower() != "y":
                break

            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1, turn ended!")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                
            print("Your current score is", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nThe winner is player", winning_idx + 1,"with a score of", max_score)