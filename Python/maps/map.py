list_1 = [1,4,5]
list_2 = [2,3,7]
#def addition(x,y):
#    return x+y
#result = map(addition,list_1, list_2)
result = map(lambda x,y:x+y,list_1, list_2 )
print(list(result))

list_3 = [1,2,3]
def sq(num):
    return num*num
result_2 = map(sq, list_3)
#result_2 = map(lambda num: num*num, list_3)
print(list(result_2))