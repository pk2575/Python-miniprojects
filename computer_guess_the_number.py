print("Let's first set the range of the numbers you will be choosing from,")
lower_limit, upper_limit = int(input("Lower limit : ")),int(input("Upper limit : "))

def user_check(value):
    return input(f"""Is {value} too high than(h), too low than(l) or 
equal to (e) your number? :""")

def do_guess():
    return (upper_limit + lower_limit)//2

guess = do_guess()

while (True) :
    feedback = input(f"""Is {guess} too high than(h), too low than(l) or 
equal to (e) your number? :""")

    if feedback == "h":
        upper_limit = guess - 1
        guess = do_guess()
    if feedback == "l":
        lower_limit = guess + 1
        guess = do_guess()

    if feedback == "e":
        print(f"The number is  {guess}")
        break
    
    else:
        print("wrong letter typed")    

        
    
