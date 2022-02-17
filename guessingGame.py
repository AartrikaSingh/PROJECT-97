import random
chances=0
number=random.randint(1,9)
print("NUMBER GUESSING GAME")
print("Enter A Number Between 1 And 9")
while chances<5:
    guess=int(input("enter your guess:"))
    if guess==number:
        print("CONGRATULATIONS!!")
        break
    elif guess<number:
        print("Your Guess Was Too Low")
    else:
        print("Your Guess Was High")
    chances=chances+1
if not chances<5:
    print("GAME OVER")     


      