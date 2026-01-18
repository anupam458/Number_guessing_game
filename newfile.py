import random

secret_number = random.randint(1, 10)
count = 0

while True:
    try:
        guess = int(input("Guess the number between 1 to 10 = "))
        count += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Correct guess, you won 🎉")
            print("You took", count, "attempts")
            break
    except ValueError:
        print("Please enter a valid number.")