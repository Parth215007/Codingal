try:
    number_1 = int(input("Enter a number: "))
    print("The number entered is: ", number_1 )
except ValueError as ex:
    print("Error is: ", ex)
