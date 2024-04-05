import random

computer_options = ['Rock', 'Paper', 'Scissors']

def player_wins(computer_score):
    global Player_Score
    Player_Score += 1
    print(f'Player Score = {Player_Score} \nComputer Score = {computer_score}')
    
def computer_wins(player_score):
    global Computer_Score
    Computer_Score += 1
    print(f'Your Score = {player_score} \nComputer Score = {Computer_Score}')
    
def final_score(player_score, computer_score):
    if player_score > computer_score:
        print(f'Final score is \nPlayer = {player_score} \nComputer = {computer_score}')
        print('Congratulations! You Win!\n')
    elif computer_score > player_score:
        print(f'Final score is \nPlayer = {player_score} \nComputer = {computer_score}')
        print('Unlucky, Computer wins!\n')
    else:
        print(f'Final score is \nPlayer = {player_score} \nComputer = {computer_score}')
        print("It's a Tie!\n")

game_over = False
Computer_Score = 0
Player_Score = 0

while not game_over:
    player_choice = input('\nPlease choose rock, paper or scissors or q to quit: ')
    player_choice = player_choice.capitalize()
    computer_choice = random.choice(computer_options)
    
    if player_choice == computer_choice:
        print(f"You chose {player_choice} and computer chose {computer_choice}.\n")
        print(f"Both players selected {player_choice}. It's a tie!\n")
        
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print(f"You chose {player_choice} and computer chose {computer_choice}.\n")
            print("Rock beats Scissors -> You win!\n")
            player_wins(Computer_Score)
        else:
            print(f"You chose {player_choice} and computer chose {computer_choice}.\n")
            print("Paper beats Rock -> You lose.\n")
            computer_wins(Player_Score)
            
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print(f"You chose {player_choice} and computer chose {computer_choice}.\n")
            print("Paper beats Rock -> You win!\n")
            player_wins(Computer_Score)
        else:
            print(f"You chose {player_choice} and computer chose {computer_choice}.\n")
            print("Scissors beats Paper -> You lose.\n")
            computer_wins(Player_Score)
            
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print(f"You chose {player_choice} and computer chose {computer_choice}.\n")
            print("Scissors beats Paper -> You win!\n")
            player_wins(Computer_Score)
        else:
            print(f"You chose {player_choice} and computer chose {computer_choice}.\n")
            print("Rock beats Scissors -> You lose.\n")
            computer_wins(Player_Score)
    
    elif player_choice == 'Q':
        final_score(Player_Score, Computer_Score)
        break
    
    else:
        print('Error. Please select a valid option')
