input_1 = int(input("Enter a number(for the range): "))
for i in range(input_1+1):
    if (i%20==0):
        print("Twist")
    elif (i%15==0):
        pass
    elif (i%5==0):
        print("Pandav")
    elif (i%3==0):
        print("buzz")
    else:
        print(i)            