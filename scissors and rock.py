import random
print("---------------------------------------------------")
print("Welcome to the rock ,paper scissors game have fun!")
print("----------------------------------------------------")
def play_round():
    #  Plays a single round of Rock-Paper-Scissors."""

    
    while True:
        user_choice = input("Do you go with rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid choice. Please choose  either rock, paper, or scissors.")

    #  random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    return user_choice, computer_choice

def main():
    #   Main function to run the Rock-Paper-Scissors game.

    user_score = 0
    computer_score = 0

    while True:
       
        user_choice, computer_choice = play_round()

        if user_choice == computer_choice:
            pass  
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            user_score += 1
        else:
            computer_score += 1

        # Display scores
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")

        # asking user to play again
        play_again = input("Wanna Play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("Thanks for playing!hope it was fun 🦖")
    print("-----------------------")

if __name__ == "__main__":
    main()
