import random
import time



def display_menu():
    print("1. Start game")
    print("2. Rules")
    print("3. Exit")
    print("")
    handle_choice()


def handle_choice():
    chose = int(input("Choose a number between 1-3: "))
    print("")
    if chose == 1:
        start_game()
    elif chose == 2:
        show_rules()
    elif chose == 3:
        exit_game()

def start_game():
    list_of_options = ['Rock','Paper','Scissors']
    global list_choice
    list_choice = random.choice(list_of_options)
    player_choice()
    display_choices()
    determine_winner()

def player_choice():
    global last_pick 
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    gamer_pick = input("Enter a number between 1-3: ")
    print("")
    if gamer_pick.isdigit() and int(gamer_pick) in range(1,4):
        if gamer_pick == "1":
            last_pick = "Rock"
        elif gamer_pick == "2":
            last_pick = "Paper"
        elif gamer_pick == "3":
            last_pick = "Scissors"
    else:
        print("You must enter a digit number between 1-3")
        start_game()


def display_choices():
    print("Your pick: "+last_pick, end='')
    time.sleep(2)
    print("             |",end='')
    print("             ",end='')
    print("Oponent pick: "+str(list_choice))

def determine_winner():
    if last_pick == list_choice:
        print("                          Draw")
        display_menu()
    if (last_pick == "Rock" and list_choice == "Scissors") or \
    (last_pick == "Paper" and list_choice == "Rock") or \
    (last_pick == "Scissors" and list_choice == "Paper"):
        print("                          You win!!!")
        display_menu()
    else:
        print("                          You lost :(")
        display_menu()

def show_rules():
    text = """
    The user selects one of three options: rock, paper, or scissors.
    After the user's selection, the program waits for 2 seconds.
    The computer automatically chooses one of three options: rock, paper, or scissors.
    Compare the choices:
    Rock crushes scissors, so rock wins against scissors.
    Scissors cuts paper, so scissors wins against paper.
    Paper covers rock, so paper wins against rock.
    If both the user and the computer choose the same item, it's a tie.
    Declare the winner or if it's a tie.
    Allow for replaying the game.
    """
    print(text)

def exit_game():
    print("Application has been closed")
    exit()


display_menu()
