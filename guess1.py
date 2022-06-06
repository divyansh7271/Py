import random

def guess(x):
        random_number = random.randint(1,x)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < random_number:
                print("Too low")
            elif guess > random_number:
                print("Too high")

        print(f"Good! You have guessed the number {random_number} correctly")

def user_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f"if {guess} too High (H), too low (L), or correct (c) ? : ")
        if feedback == 'H' or feedback == 'h':
            high = guess
        elif feedback == 'L' or feedback == 'l':
            low = guess

    print(f"Correct Answer! You were thinking of {guess}")


user_guess(10)                   


guess(10)                