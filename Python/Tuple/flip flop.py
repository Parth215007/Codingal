def palindrome(a):
    s=0
    e=len(a)-1
    while (s>e):
        if a[s]!=a[e]:
            print("Not palindrome")
            return
        s = s+1
        e = e-1 
    print("Palindrome found")
    return


tuple_1 = (1,2,3,3,2,1)
palindrome(tuple_1)  

