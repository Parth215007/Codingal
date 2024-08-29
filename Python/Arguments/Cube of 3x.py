input_cube = int(input("Enter a number: "))
def cube(number):
    return number*number*number
def cube_3(number):
    if(number%3==0):
        print(cube(number))
    else:
        print("The Number is not divisible by 3")
cube_3(input_cube)

      

