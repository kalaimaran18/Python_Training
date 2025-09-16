#Multilevel Inheritance

class Grandpa:

    def Land(self):
        print("Grandpa's Land")

class Father(Grandpa):
    def House(self):
        print("Father's House")

class Mother(Father):
    def Money(self):
        print("Mother's Money")

class son(Mother,Father):
    def Laptop(self):
        print("My Laptop")

kalai=son()
kalai.Laptop()
kalai.Money()
kalai.House()

yaso=Mother()
yaso.House()

Ram=Father()
Ram.Land()