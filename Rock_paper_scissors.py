import random


playlist = ["r", "p", "s"]
keys = { "r" : "rock", "p" : "paper", "s":"scissors"}
win = {"r": "s", "p":"r", "s":"p"}


def evaluate(user, pc ):
    print(f"PC plays {keys[pc]}")
    if win[user] == pc:
        print("you win")
    elif win[pc] == user:
        print("you lose")
    else:
        print("it is a draw")

def continuation():
    play_desire = input("Do you want to plyay again? y/n \n")
    if play_desire == "y":
        return 1
    else:
        return 0


status = 1
while (status) :
    user_play = input("Rock(r), paper(p) or scissors(s) ? \n ").lower()
    pc_play = random.choice(playlist)
    evaluate(user_play, pc_play)
    status = continuation()
