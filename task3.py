import random

# Choices available
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score

    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

def main():
    global user_score, computer_score

    while True:
        print("\nRock, Paper, Scissors Game!")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Display scores
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        # Ask if user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Final Score -> You:", user_score, "| Computer:", computer_score)
            break

if __name__ == "__main__":
    main()
