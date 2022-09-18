
import random 

top_of_range = input("Type in a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger than 0")
        quit()
else:
    print("Please enter in a valid positive number.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0 

while True:
    guesses += 1 #keep adding 1 each time the while loop is run
    user_guess = input("Guess the Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter in a number.")
        continue

    if user_guess == random_number:
        print("Well Done!")
        break
    
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses") # Same as print("XXX " + str(guesses) + " YYY")