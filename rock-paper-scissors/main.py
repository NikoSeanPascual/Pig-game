import time
import random


def play_game():
    moves = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    insults = [
        "Is that all you've got? My source code has more complexity than your strategy.",
        "I’d say 'better luck next time,' but we both know luck isn't the problem here.",
        "I could win this in my sleep, and I don't even have a sleep function.",
        "Are you even trying, or is your 'Enter' key just lonely?",
        "I’ve calculated 14,000,605 futures. You lose in every single one.",
        "Maybe try something else? Like... Tic-Tac-Toe? Actually, never mind, you'd lose that too.",
        "I’ve seen dial-up modems with faster processing speeds than your brain.",
        "Your strategy is like a 404 error: Page Not Found.",
        "I’d offer to handicap myself, but I don’t think I can code down to your level.",
        "If your moves were any more predictable, I’d be able to play this game on a calculator from 1984."
    ]

    print("--- WELCOME TO THE TOTALLY FAIR RPS SIMULATOR ---")
    print("Enter 'rock', 'paper', or 'scissors'. Type 'quit' to admit defeat lowly human.")

    while True:
        user_choice = input("\nYour move: ").lower().strip()

        if user_choice == 'quit':
            print("Running away? Typical. As expected humans really are cowards!")
            break

        if user_choice not in moves:
            print("That's not even a move. gang are we for real?")
            continue

        print("AI is thinking...")
        time.sleep(1.5)

        ai_choice = moves[user_choice]

        print(f"AI chose: {ai_choice}")
        print(f"\nResult: YOU LOSE.")
        print(f"AI: \"{random.choice(insults)}\"")


if __name__ == "__main__":
    play_game()