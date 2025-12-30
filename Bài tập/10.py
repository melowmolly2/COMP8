class Animal:
    def __init__(self,name,age,legs):
        self.name=name
        self.age=age
        self.legs=legs
    def __str__(self):
        return self.name
    
class Fish(Animal):
    def __init__(self,name,age):
        super().__init__(name,age,0)

class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age,4)

cat=Cat("Dog",666)
print(cat)