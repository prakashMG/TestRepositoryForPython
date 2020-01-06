secrete_number = 2020
guess_number = ""
guess_Count = 0
guess_Limit = 3
out_of_guesses = False

while guess_number != secrete_number and not (out_of_guesses):
    guess_number = int(input("\nPlease enter a guess number : "))
    if guess_number > secrete_number:
        print("Entered number : " + str(guess_number) + " is greater than secrete number")
        guess_Count = +1
    elif guess_number < secrete_number:
        print("Entered number is :" + str(guess_number) + " is lesser than secrete number")
        guess_Count = +1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You have guessed secrete number")
else:
    print("You los the game ")
