try:
    num1, num2 = eval(input("Enter 2 number seperated by a comma: "))
    result = (num1/num2)
    print("The result of num1/num2 is: ", result)
except ZeroDivisionError as zd:
    print("The error is: ", zd)
except SyntaxError as se:
    print("The error is: ", se)
except:    
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("End of try except block")           
