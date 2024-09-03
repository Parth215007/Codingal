input_1 = int(input("Enter a number: "))
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*factorial(num-1)
print(input_1)    
        
    