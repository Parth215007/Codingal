import random
random_1 = (random.randint(0,5))
while True:
    input_1 = int(input("Enter a number from the given range(0-5): "))
    if input_1==random_1:
        print("Congratulations u have guessed the number correctly")
        break
    else:
        print("Your guess was wrong")
