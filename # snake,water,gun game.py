# snake,water,gun game
import random

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice (snake/water/gun): ")
    while choice not in ['snake', 'water', 'gun']:
        print("Invalid choice! Please enter either snake, water, or gun.")
        choice = input("Enter your choice (snake/water/gun): ")
    return choice

def check_win(user_choice, computer_choice):
    if user_choice == computer_choice: 
        return "It's a tie!"
    elif user_choice == 'snake':
        if computer_choice == 'water':
            return "You win! Snake drinks Water."
        else:
            return "You lose! Gun shoots Snake."
    elif user_choice == 'water':
        if computer_choice == 'gun':
            return "You win! Water drowns Gun."
        else:
            return "You lose! Snake drinks Water."
    elif user_choice == 'gun':
        if computer_choice == 'snake':
            return "You win! Gun shoots Snake."
        else:
            return "You lose! Water drowns Gun."

def play_game():
    print("Welcome to Snake-Water-Gun game!")
    print("You will be playing against the computer.")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = check_win(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again != 'yes':
            print("Thanks for playing!")
            break


play_game()
