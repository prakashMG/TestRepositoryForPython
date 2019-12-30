secrete_Word = "my word"
guess = ""
guess_Count = 0
guess_Limit = 3
out_of_guesses = False
""" 
while guess != secrete_Word and not(out_of_Guesses):
    if guess_Count<guess_Limit:
        guess = input("enter guess again : ")
        guess_Count+=1
    else:
        out_of_Guesses=True
    """
while guess != secrete_Word and not(out_of_guesses) :

    if guess_Count<guess_Limit:
        guess=input("enter your guess : ")
        guess_Count+=1
    else:
        out_of_guesses=True


if out_of_guesses:
    print("you have lost the game : ")
else:
    print("you win ")
