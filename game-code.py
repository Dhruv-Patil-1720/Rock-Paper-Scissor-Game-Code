import random
user_choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors Game!")
print("Rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")

# Initialize Scores
player_score = 0
computer_score = 0

# Repeat Until the Player Decides to Exit
while True:
    #  Menu Options
    print("\nMenu Options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    #  User Input
    user_input = input("Enter your choice (1-4): ").lower()

    # If the Player chooses to Exit
    if user_input == "4":
        print("\nFinal Scores:")
        print(f"Player: {player_score}  Computer: {computer_score}")
        print("Thank You for playing. Goodbye!")
        break

    # If the Player Chose Rock, Paper, or Scissors
    elif user_input in ["1", "2", "3"]:
        #  Computer's Choice
        computer_choice = random.choice(user_choices)

        # Determine the Winner
        if user_choices[int(user_input) - 1] == computer_choice:
            result = "It's a Tie!"
        elif (
            (user_choices[int(user_input) - 1] == "rock" and computer_choice == "scissors")
            or (user_choices[int(user_input) - 1] == "paper" and computer_choice == "rock")
            or (user_choices[int(user_input) - 1] == "scissors" and computer_choice == "paper")
        ):
            result = "You Win!!"
            player_score += 1
        else:
            result = "Computer Wins!!!!"
            computer_score += 1

        # Results
        print(f"\nYour choice: {user_choices[int(user_input) - 1]}")
        print(f"Computer's choice: {computer_choice}")
        print(f"Result: {result}")

    # Current Scores
    print(f"\nCurrent Scores - Player: {player_score}  Computer: {computer_score}")
