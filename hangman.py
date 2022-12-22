import random

passage ="""The color of animals is by no means a matter of chance;
 it depends on many considerations, but in the majority of cases tends to protect."""

def rand_word():
    word_list = []
    for string in passage.split():
        word = "".join(x for x in string if x.isalpha())
        if len(word)>3:
            word_list.append(word)
            continue
    return random.choice(word_list).upper()

def print_ui(health, guessed, ans_ui):
    #total health is 7

    print("\n"+ " "*35 +  "HP : " +"0"*health + "-" * (7-health)+"\n")

    print(f"""
    Guessed letters:                                        Answer sheet:

    {guessed}                                               {ans_ui}""")

def ans_ui(word, seen_letters):
    for letter in word:
        if letter in seen_letters:
            continue
        else:
            word = word.replace(letter," * ")
    return word

def play():
    word = rand_word()
    letters = set (x for x in word)
    cur_health = 7
    seen = set({})

    while not letters.issubset(seen) and cur_health!= 0 :
        char = input("What is your letter of choice? \n").upper()
        seen.add(char)
        if char in word:
            print("Right guess")
        else:
            print("Wrong guess")
            cur_health -= 1

        print_ui(cur_health,seen,ans_ui(word,seen))


    if cur_health == 0 :
        print("You lost! Try again. ")
    
    else:
        print("Congratulations, you win!")

play()
        