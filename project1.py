import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Get number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

# Game loop
while max(player_scores) < max_score:
    for player_i in range(players):
        print(f"\nPlayer {player_i + 1}'s turn has just started!")
        print("Your current score is:", player_scores[player_i], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over, no points this round.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}. Current turn score: {current_score}")

        # Update total score after the player's turn
        player_scores[player_i] += current_score
        print(f"Total score for Player {player_i + 1}: {player_scores[player_i]}")

        # Check for winner
        if player_scores[player_i] >= max_score:
            print(f"\n Player {player_i + 1} wins with a score of {player_scores[player_i]}! ")
            break

    if max(player_scores) >= max_score:
        break
