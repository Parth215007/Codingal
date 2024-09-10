import random
element_1 = ["Rock", "Paper", "Scissors"]
choice_1 = random.choice(element_1)
input_1 = input("Enter your choice from the following(Rock,Paper,Scissors): ")
if input_1==choice_1:
    print("It is a draw")
elif input_1=="Rock":
    if choice_1=="Paper":
        print("You lost")
    else:
        print("You won")

elif input_1=="Paper":
    if choice_1=="Rock":
        print("You won")
    else:
        print("You lost")

elif input_1=="Scissors":
    if choice_1=="Rock":
        print("You lost")
    else:
        print("You won")                
       


           




