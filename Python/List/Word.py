list = ['abc', 'cbc', 'xyz', 'aba', '1221']
count = 0
list_1 = []
for i in list:
    if len(i)>1 and i[0]==i[-1]:
        list_1.append(i)
        count = count+1
print(list_1)    