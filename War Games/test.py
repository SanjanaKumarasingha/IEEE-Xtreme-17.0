# Read the number of games
n = int(input())

# Function to simulate the game and determine the winner
def play_game(player1_cards, player2_cards):
    while player1_cards and player2_cards:
        card1, card2 = player1_cards.pop(0), player2_cards.pop(0)
        if card1 > card2:
            player1_cards.extend([card2, card1])
        elif card1 < card2:
            player2_cards.extend([card1, card2])
        else:
            player1_cards.append(card1)
            player2_cards.append(card2)
    if not player1_cards and not player2_cards:
        return "draw"
    elif not player1_cards:
        return "player 2"
    else:
        return "player 1"

# Process each game
for _ in range(n):
    player1_cards = input().split()[1:]
    player2_cards = input().split()[1:]
    winner = play_game(player1_cards, player2_cards)
    print(winner)
