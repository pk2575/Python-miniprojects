import random

lower,upper = int(input("what is the low limit of my secret? \n")), int(input("what is the upper limit of my secret? \n"))
secret_number = random.randint(lower, upper + 1)

while True :
    user_guess = int(input("what is my secret number? \n"))
    if user_guess == secret_number:
        print("That is right! \n My secret number is " + str(user_guess))
        break
    elif user_guess > secret_number:
        print("go little lower")
        continue

    elif user_guess < secret_number:
        print("go little higher")
        continue
    else:
        continue
