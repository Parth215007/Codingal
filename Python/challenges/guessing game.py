import random
import time

number = random.randint(1,100)
name = input("Enter your name: ")

print("Hello", name, "try to guess the number between the range of 1-100")
if number%2==0:
    x = 'even'
else:
    x = 'odd'
print(f"This is an {x} number")
time.sleep(.5)
print("Start")

def picks():
    chances  = 0
    while chances<6:
        time.sleep(.25)
        guess_1 = input("Enter your guess: ")
        try:
            guess_2=int(guess_1)
            if guess_2<=100 and guess_2>=1:
                if chances<6:
                    if guess_2<number:
                        print("The number chosen is too low")

                    elif guess_2>number:
                        print("The number chosen is too high") 
                    if guess_2 != number:
                        time.sleep(.5)
                        print("Try again")
                    elif guess_2==number:
                        print("You have guessed right")
                        break
                    if guess_2>100 or guess_2<1:
                        print("Please enter the number in the correct range(1-100)")
        except:
            print("Please enter a number: ")
            if guess_2 != number:
                print("Invalid response. The correct number was ", number)
                time.sleep(.5)                
            if guess_2==number:
                print("U guessed the number in", chances, "chances")                
