true_1 = True
while true_1:
    try:
        input_1 = int(input("Enter a number: "))
        while (input_1%2==0):
            print("Bye Bye")
        true_1 = False
    except ValueError as ex:
        print("The error is: ", ex)        
            

    
        