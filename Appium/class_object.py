#classes and object

class Car:
    #self is for the current class, and then you have make and model
    def __init__(self, make = "2005", model = "Toyota"):
        self.model = model
        self.make = make
    
    def print(self):
        print("The make is ", self.make, "And the model is ", self.model)

car1 = Car()
car2 = Car("1971", "Carolla")

car1.print()
car2.print()
print(" ")

#Inheritance, creating a child class from a parent class

#Bracket means inheritance
class Toyta(Car):
    def __init__(self, make, model, color="black", hp=500):
        #Inheriting the parameters from parent
        super().__init__(make, model)
        self.color = color
        self.hp = hp

    def show(self):
        print(f"{self.make}, {self.model}, {self.color}, {self.hp}")

# When creating an instance of a child class, pass in the parent parameters first

my_toyota = Toyta("Toyoyo", "1972", "White", 750)
my_old = Toyta("Mazda", "2005")

print(my_old.show())
print(my_old.make)
print(my_toyota.show())
print(my_old.print())
print(my_toyota.print())

print(" ")
print("=============ENCAPSSULATION EXAMPLE==============")
print(" ")
#Encapsulation, only showing what needs to be shown
class Bank:
    def __init__(self, account, money):
        self.account = account
        self.__money = money # double __before means that is is private
    
    def show(self):
        print(f"The account is {self.account} and the money is {self.__money}")


hassaan = Bank(134234, "$560.85")

print(hassaan.account)
# print(hassaan.money)
hassaan.show()

#Polymorphism is when it takes priority over the chold method rather then the parent method
