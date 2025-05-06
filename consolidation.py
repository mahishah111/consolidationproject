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
def refill():
    return


#16-0 either way
def check_moon():
    return


#if player hits 9 before game over

def early_win():
    return
    
#commit- coding function after round stuff based on player conditions
