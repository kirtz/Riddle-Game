
import random 

top_of_range = input("Type in a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger than 0")
        quit()
else:
    print("Please enter in a number.")
    quit()

random_number = random.randint(0, top_of_range)

print(random_number)

while True:
    user_guess = input("Guess the Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

else:
    print("Please enter in a number.")