import random
while True:

    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r' , 'p', 's'])
    print(f"\nYou chose {user}, computer chose {computer}.\n")
    
    if user == computer:
       print(f"You and the computer have both chosen {user}. It's a tie.")

    elif user == 'r' :  
       if computer == 's':
           print("Rock smashes scissors! You win!")
       else:
           print("Paper covers rock! You lose.")
    elif user == 'p':
        if computer == 'r':
           print("Paper covers rock! You win")
        else:
           print("Scissors cuts paper! You lose")
    elif user == 's':
       if computer == 'paper':
           print("Scissors cuts paper! You win!")
       else:
           print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
      break
    
    
    
