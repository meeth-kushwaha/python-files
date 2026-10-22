"""Program 052: Rock Paper Scissors Lizard Spock Game."""
import random

RULES = {
    "scissors": ["paper", "lizard"],
    "paper":    ["rock", "spock"],
    "rock":     ["lizard", "scissors"],
    "lizard":   ["spock", "paper"],
    "spock":    ["scissors", "rock"]
}

def play_round(user: str, computer: str) -> str:
    user, computer = user.lower(), computer.lower()
    if user == computer:
        return f"Tie! Both chose {user}."
    elif computer in RULES[user]:
        return f"You Win! {user.capitalize()} beats {computer}."
    else:
        return f"Computer Wins! {computer.capitalize()} beats {user}."

if __name__ == "__main__":
    print("--- 052: Rock Paper Scissors Lizard Spock ---")
    choices = list(RULES.keys())
    user_choice = "spock"
    cpu_choice = random.choice(choices)
    print(f"User: {user_choice}, Computer: {cpu_choice}")
    print(play_round(user_choice, cpu_choice))
