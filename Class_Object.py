#Class and object 
#Create a class called kodaikanal and create all the possible values

class kodaikanal:

    location=input()                # Give input like Hill Station 

    def climate(self):
        print("Everyone Likes the Chill climate")

        print("Its Suitable place to summer vacation")

    def travel(self):
        print("The travel cost is too high")

    def special(self):
        print("In kodaikanal very famous in tea Estate")

ob=kodaikanal()
ob.climate()
ob.special()
ob.travel()
print(ob.location)



# Create a Class Student
# Problem 1

class student:
    def __init__(self):
        self.name="Kalai"
        self.reg=411522
    def display(self):
        print("Name:",self.name)
        print("reg:",self.reg)

T=student()
T.name="Kohli"
T.display()
