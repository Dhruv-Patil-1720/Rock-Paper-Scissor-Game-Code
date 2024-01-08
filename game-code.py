import random
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors Game !!!!")
print("Rules:  Remember Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")

# Initialize Scores
player-score = 0
computer-score = 0

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
        print("\n Final Scores: " )
        print(f" Player: {player-score}  Computer: {computer-score} ")
        print(" Thank You for playing. Goodbye!! ")
        break

    # If the Player Chose Rock, Paper, or Scissors
    elif user_input in ["1", "2", "3"]:
        #  Computer's Choice
        computer_choice = random.choice(choices)

        # Determine the Winner
        if choices[int(user_input) - 1] == computer_choice:
            result = "It's a Tie!"
        elif (
            (choices[int(user_input) - 1] == "rock" and computer_choice == "scissors")
            or (choices[int(user_input) - 1] == "paper" and computer_choice == "rock")
            or (choices[int(user_input) - 1] == "scissors" and computer_choice == "paper")
        ):
            result = "You Win!!"
            player-score += 1
        else:
            result = "Computer Wins!!!!"
            computer-score += 1

        # Results
        print(f"\n Your choice: {choices[int(user_input) - 1]} ")
        print(f" Computer's choice: {computer_choice} ")
        print(f" Result: {result} ")

    # Current Scores
    print(f"\nCurrent Scores - Player: {player-score}  Computer: {computer-score}")
