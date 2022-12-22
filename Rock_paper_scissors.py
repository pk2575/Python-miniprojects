import random

playlist = ["r", "p", "s"]
names = { "r" : "rock", "p" : "paper", "s":"scissors"}
keys = {"r": "s", "p":"r", "s":"p"}

def play():
    user_play = input("Rock(r), paper(p) or scissors(s) ? \n ").lower()
    pc_play = random.choice(playlist)
    print(f"PC plays {names[pc_play]}")

    if is_win(user_play,pc_play):
        return("You win")
    elif user_play == pc_play:
        return('It is a draw')
    else:
        return "You lose"

def is_win(player, opponent):
    if keys[player] == opponent:
        return True
    
def continuation():
    play_desire = input("Do you want to play again? y/n \n")
    if play_desire == "y":
        return True
    else:
        return False

online = True
while online:
    print(play())
    online = continuation() 
