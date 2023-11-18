import random

# Set up the deck of Uno cards
colors = ["Red", "Yellow", "Green", "Blue"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw 2"]
wilds = ["Wild", "Wild Draw 4"]
deck = []
for color in colors:
    for value in values:
        card_val = f"{color} {value}"
        deck.append(card_val)
    for wild in wilds:
        card_val = f"{wild}"
        deck.append(card_val)

# Shuffle the deck
random.shuffle(deck)

# Set up the players
num_players = int(input("How many players? "))
players = []
for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    players.append({"name": name, "hand": []})

# Deal 7 cards to each player
for i in range(7):
    for player in players:
        player["hand"].append(deck.pop())

# Set up the game
current_color = deck.pop().split()[0]
current_value = None
direction = 1
turn = 0
winner = None

# Play the game
while not winner:
    # Get the current player
    player = players[turn]
    print(f"\n{player['name']}'s turn!")
    print(f"Current color: {current_color}")
    print(f"Current value: {current_value}")
    print("Your hand:")
    for i, card in enumerate(player["hand"]):
        print(f"{i+1}. {card}")
    
    # Check for valid plays
    valid_plays = []
    for card in player["hand"]:
        card_color, card_value = card.split()
        if card_color == current_color or card_value == current_value or card_color == "Wild":
            valid_plays.append(card)
    if not valid_plays:
        # Player cannot make a valid play, draw a card
        player["hand"].append(deck.pop())
        print("No valid plays, drew a card.")
        continue
    
    # Ask the player which card to play
    while True:
        play_index = int(input("Enter the number of the card you want to play: ")) - 1
        if play_index < 0 or play_index >= len(player["hand"]):
            print("Invalid card number.")
        else:
            play_card = player["hand"].pop(play_index)
            break
    
    # Update the game state based on the card played
    play_color, play_value = play_card.split()
    if play_color == "Wild":
        # Wild card, ask player for color
        while True:
            wild_color = input("Enter the color you want to change to (Red, Yellow, Green, or Blue): ")
            if wild_color not in colors:
                print("Invalid color.")
            else:
                current_color = wild_color
                break
        if play_value == "Wild":
            # Wild Draw 4 card, draw 4 cards and skip next player's turn
            for i in range(4):
                players[(turn+1*direction)%len(players)]["hand"].append(deck.pop())
            print(f"Drew 4 cards and skipped {players[(turn+1*direction)%len(players)]['name']}'s turn!")
            turn = (turn+2*direction)%len(players)
        elif play_value == "Draw 2":
                    # Draw 2 card, next player draws 2 cards and is skipped
            players[(turn+1*direction)%len(players)]["hand"].append(deck.pop())
            players[(turn+1*direction)%len(players)]["hand"].append(deck.pop())
            print(f"{players[(turn+1*direction)%len(players)]['name']} drew 2 cards and was skipped!")
            turn = (turn+2*direction)%len(players)
        elif play_value == "Reverse":
            # Reverse card, reverse the direction of play
            direction = -direction
            print("Reversed direction of play!")
            turn = (turn+1*direction)%len(players)
        elif play_value == "Skip":
            # Skip card, skip the next player's turn
            print(f"Skipped {players[(turn+1*direction)%len(players)]['name']}'s turn!")
            turn = (turn+2*direction)%len(players)
    else:
        current_color = play_color
        current_value = play_value
        if play_value == "Reverse":
            # Reverse card, reverse the direction of play
            direction = -direction
            print("Reversed direction of play!")
        elif play_value == "Skip":
            # Skip card, skip the next player's turn
            print(f"Skipped {players[(turn+1*direction)%len(players)]['name']}'s turn!")
            turn = (turn+2*direction)%len(players)
        elif play_value == "Draw 2":
            # Draw 2 card, next player draws 2 cards
            players[(turn+1*direction)%len(players)]["hand"].append(deck.pop())
            players[(turn+1*direction)%len(players)]["hand"].append(deck.pop())
            print(f"{players[(turn+1*direction)%len(players)]['name']} drew 2 cards!")
            turn = (turn+1*direction)%len(players)
        else:
            # Normal card, move on to next player
            turn = (turn+1*direction)%len(players)

    # Check if current player has won
    if not player["hand"]:
        winner = player["name"]

print(f"\n{winner} wins!")