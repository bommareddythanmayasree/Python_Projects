import random

def high_low_game():
    print("Welcome to the Higher or Lower Game! ")
    print("Rules: You'll be shown a number (1-100).")
    print("Guess whether the next number will be HIGHER or LOWER!")
    print("Type 'h' for higher or 'l' for lower.\n")

    score = 0
    current_number = random.randint(1, 100)

    while True:
        print(f"Current number: {current_number}")
        guess = input("Will the next number be (h)igher or (l)ower? ").lower()

        if guess not in ["h", "l"]:
            print(" Invalid choice! Please enter 'h' or 'l'.")
            continue

        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")

        if (guess == "h" and next_number > current_number) or (guess == "l" and next_number < current_number):
            score += 1
            print(f"Correct! Your score is now {score}\n")
            current_number = next_number
        else:
            print(f" Wrong guess! Final score: {score}")
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    high_low_game()
