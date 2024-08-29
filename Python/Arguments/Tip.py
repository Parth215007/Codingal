def total_bill(bill_amount,tip_percent):
    total = (bill_amount * (tip_percent/100) + bill_amount )
    print("The total amount of the bill is: ",total)
input_1 = int(input("Enter the total bill amount: "))
input_2 = int(input("Enter the tip percent: "))
total_bill(input_1,input_2)

    