"""Program 050: Hangman Word Guessing Game Engine."""
class HangmanGame:
    def __init__(self, secret_word: str, max_lives: int = 6):
        self.secret_word = secret_word.upper()
        self.max_lives = max_lives
        self.lives_left = max_lives
        self.guessed_letters = set()

    def guess(self, letter: str) -> str:
        letter = letter.upper()
        if letter in self.guessed_letters:
            return "Already guessed that letter."
        self.guessed_letters.add(letter)
        if letter in self.secret_word:
            if self.is_won():
                return f"Correct! You won! The word was {self.secret_word}."
            return f"Good guess! '{letter}' is in the word."
        else:
            self.lives_left -= 1
            if self.lives_left <= 0:
                return f"Game Over! The word was {self.secret_word}."
            return f"Wrong! Lives left: {self.lives_left}."

    def display_word(self) -> str:
        return " ".join([ch if ch in self.guessed_letters else "_" for ch in self.secret_word])

    def is_won(self) -> bool:
        return all(ch in self.guessed_letters for ch in self.secret_word)

if __name__ == "__main__":
    print("--- 050: Hangman Game Simulation ---")
    game = HangmanGame("PYTHON", max_lives=4)
    print("Word:", game.display_word())
    print(game.guess("P"))
    print(game.guess("Z"))
    print(game.guess("Y"))
    print("Word:", game.display_word())
