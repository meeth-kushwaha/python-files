"""Program 051: Blackjack Card Game Engine."""
import random

def calculate_hand(cards: list[int]) -> int:
    total = sum(cards)
    aces = cards.count(11)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

class BlackjackGame:
    def __init__(self):
        deck_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(deck_cards)
        self.deck = deck_cards
        self.player = [self.deck.pop(), self.deck.pop()]
        self.dealer = [self.deck.pop(), self.deck.pop()]

    def play(self) -> str:
        while calculate_hand(self.player) < 17:
            self.player.append(self.deck.pop())
        player_score = calculate_hand(self.player)
        if player_score > 21:
            return f"Player busts with {player_score}! Dealer wins."

        while calculate_hand(self.dealer) < 17:
            self.dealer.append(self.deck.pop())
        dealer_score = calculate_hand(self.dealer)

        if dealer_score > 21:
            return f"Dealer busts with {dealer_score}! Player wins."
        elif player_score > dealer_score:
            return f"Player wins ({player_score} vs {dealer_score})!"
        elif player_score < dealer_score:
            return f"Dealer wins ({dealer_score} vs {player_score})!"
        return f"Push (Tie) at {player_score}!"

if __name__ == "__main__":
    print("--- 051: Blackjack Simulator ---")
    game = BlackjackGame()
    print(f"Player starting hand: {game.player}")
    print(f"Dealer upcard: {game.dealer[0]}")
    print(game.play())
