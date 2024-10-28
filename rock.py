import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user and computer choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")

    while True:
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Scores: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
