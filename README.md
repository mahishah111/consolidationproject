# consolidationproject

This is a console-based two-player card game written in Python. The player competes against the computer in 16 rounds, hoping to win the most rounds by playing higher value cards that follow the lead suit

## instructions

- Each player will start with 8 cards.
- The deck chas of 48 cards (4 suits, 12 values).
- Card values range from Ace (1) to Queen (12).
- Players take turns leading a round the other must follow suit if possible.
- The higher card in the lead suit wins the round.
- After every round, a card from the deck is revealed, and both players draw 4 new cards 
- The game ends after 16 rounds or if an "early win" condition is met.

## Rules

- **Shoot the Moon**: If a player wins all 16 rounds (the other has 0), they automatically wins
- **Early Win**: If one player reaches 9+ points and the other has at least 1, the game ends early.

## Game Components

### Deck & Cards
- `create_deck()` – Generates and shuffles a 48-card deck.
- `card_name(card)` – Converts a card tuple into a human-readable format.

### Flow of the game
- `deal(deck, num)` – Deals `num` cards from the deck.
- `display(hand)` – Displays a player's hand with card indices.
- `choose_card(hand, lead_suit)` – Allows user input to select a card.
- `computer(hand, lead_suit)` – Computer chooses a legal card.
- `end_round(lead_card, follow_card, lead_suit)` – Determines round winner.
- `refill(deck, hand1, hand2)` – Replenishes player hands by 4 cards.
- `check_moon(score1, score2)` – Detects if a player "shot the moon."
- `early_win(score1, score2)` – Checks for early game termination.

### Loop
The main loop:
- Alternates leads
- Lets the player or computer select a card.
- Determines the round winner and updates the score.
- Continues until the end of the game or early win condition.

```

Follow the console prompts to play