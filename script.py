class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("Whoof Whoof")
    def greeting(self):
        print(f"I am {self.owner.name} and {self.name} is my dog")
class Owner:
    def __init__(self,name,address,contact,lst):
        self.name = name
        self.address = address
        self.contact = contact
        self.lst = lst
    def arraySort(self):
        return sorted(self.lst)


owner1 = Owner("Nithish","India","00-000",[5,1,5,3,5,6,7,8])
dog1 = Dog("Tom","BullDog",owner1)
dog1.greeting()
print("Sorted Array is: ",owner1.arraySort())