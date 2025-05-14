import random
#this will describe all the cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = list(range(1, 11)) + [11, 12]
faces = {1: "Ace", 11: "Jack", 12: "Queen"}

#displays card in a format easy to read (x, x)

def card_name(card):
    value = faces.get(card[1], str(card[1]))
    return f"{value} of {card[0]}"

#iterate though suit and value list to create deck then shuffle

def create_deck():
    deck = [(suit, value) for suit in suits for value in values]
    print(deck)
    random.shuffle(deck)
    return deck

#deals cards to respective hands either me or the computer

def deal(deck, num):
    hand = deck[:num]
    del deck[:num]
    return hand

#iterates though the players hand and prints each hand

def display(hand):
     print("\nYour hand:")
     for i, card in enumerate(hand):
        print(f"{i}: {card_name(card)}")

#determines which cards are playable and gives player card options

def choose_card(hand,lead_suit=None):
    options = list(range(len(hand)))
    if lead_suit:
        playable_cards = [card for card in hand if card[0] == lead_suit]
        if playable_cards:
            options = [i for i, card in enumerate(hand) if card[0] == lead_suit]
            print(f"You must follow suit: {lead_suit}")
    
    while True:
        try:
            idx = int(input(f"Choose card to play (index {options}): "))
            if idx in options:
                return hand.pop(idx)
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a valid number.")

#same thing but for computer, makes a random decsion as if it was another human
def computer(hand, lead_suit=None):
    if lead_suit:
        follow = [card for card in hand if card[0] == lead_suit]
        chosen = random.choice(follow) if follow else random.choice(hand)
    else:
        chosen = random.choice(hand)
    hand.remove(chosen)
    return chosen


#compares cards suits ad values to determine a winner

def end_round(lead_card, follow_card, lead_suit):
    if follow_card[0] == lead_suit and follow_card[1] > lead_card[1]:
        return "follower"
    return "leader"


#commit here- these finish code for the logic in the round

#counts card in hand and deck, if > than 8, randomly deals 4 more cards
def refill(deck, hand1, hand2):
    if len(hand1) == 4 and len(hand2) == 4 and len(deck) >= 8:
        hand1.extend(deal(deck, 4))
        hand2.extend(deal(deck, 4))
        print("\nBoth players drew 4 new cards.")


#16-0 either way
def check_moon(score1, score2):
    if score1 == 0 and score2 == 16:
        return "P1"
    elif score2 == 0 and score1 == 16:
        return "P2"
    return None


#if player hits 9 before game over

def early_win(score1, score2):
    return (score1 >= 9 and score2 >= 1) or (score2 >= 9 and score1 >= 1)

deck = create_deck()
p1_hand = deal(deck, 8)
p2_hand = deal(deck, 8)
scores = {"P1": 0, "P2": 0}
leader = random.choice(["P1", "P2"])
round_num = 0

print(f"{leader} will lead first.\n")

while round_num < 16 and not early_win(scores["P1"], scores["P2"]):
    round_num += 1
    print(f"--- Round {round_num} ---")
    print(f"{leader} leads.")

    if leader == "P1":
        display(p1_hand)
        lead_card = choose_card(p1_hand)
        follow_card = computer(p2_hand, lead_card[0])
    else:
        lead_card = computer(p2_hand)
        print(f"Computer plays: {card_name(lead_card)}")
        display(p1_hand)
        follow_card = choose_card(p1_hand, lead_card[0])

    print(f"You played: {card_name(lead_card) if leader == 'P1' else card_name(follow_card)}")
    print(f"Computer played: {card_name(follow_card) if leader == 'P1' else card_name(lead_card)}")

    winner = end_round(lead_card, follow_card, lead_card[0])
    if (leader == "P1" and winner == "leader") or (leader == "P2" and winner == "follower"):
        round_winner = "P1"
    else:
        round_winner = "P2"

    print(f"{round_winner} wins the round.\n")
    scores[round_winner] += 1
    leader = round_winner

    if deck:
        revealed = deck.pop(0)
        print(f"Revealed card from deck: {card_name(revealed)}\n")

    refill(deck, p1_hand, p2_hand)

moon_shooter = check_moon(scores["P1"], scores["P2"])
if moon_shooter:
    print(f"\n{moon_shooter} shot the moon and wins with 17 points!")
else:
    winner = "P1" if scores["P1"] > scores["P2"] else "P2"
    print(f"\nGame Over. {winner} wins!")
    print(f"Final Scores — You: {scores['P1']}, Computer: {scores['P2']}")
    
#commit- coding function after round stuff based on player conditions
