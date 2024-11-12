class Parrot:
    species = 'bird'
    def __init__(self,name,age):
        self.name = name
        self.age = age
ob = Parrot('Jake', 20)
ob_1 = Parrot('Tom', 21)
print("Jake is a ",Parrot.species)
print("Tom is also a ",Parrot.species)

print(ob.name,"is ", ob.age, "years old." )
print(ob_1.name,"is ", ob_1.age, "years old." )



        