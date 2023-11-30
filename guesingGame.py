import random
print("Numer Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess the number between 1-9")
while chances < 5:
    guess=int(input("Enter your guess"))
    if guess == number:
        print("Congratulations you win!")
        break
    elif guess<number:
        print("Your guess was low.guess higher")
    else:
        print("Your gues was high.guess lower")
    chances+=1
if not chances<5:
    print("You lose!!!The number is",number)

    
