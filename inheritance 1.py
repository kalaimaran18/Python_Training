#inheritance vehicle()
# Vehicle System (Vehicle → Car/Truck/Motorcycle)
# Problem(1)

'''
Relationship: “is-a.” A car is a vehicle; a truck is a vehicle.
What shared: common capabilities such as starting, stopping, basic identification.
What customized: each subtype adds or overrides behavior (a truck can carry cargo; a motorcycle balances differently).
Key property: anywhere the system expects a “vehicle,” you should be able to plug in a car, truck, or motorcycle and it still works logically.
Why it matters: reuse shared logic, minimize duplication, and create a clean hierarchy of capabilities.

'''
class Vehicle:
    def __init__(self,name):
        self.name=name
       
    def start(self):
        print(f"{self.name} is started.")

    def stop(self):
        print(f"{self.name} is stopped.")

    def identify(self):
        print(f"{self.name} to identify.")

class car(Vehicle):
    def identify(self):
       print(f"{self.name} is 4 wheel")

class truck(Vehicle):
    def identify(self):
        print("A truck can carry cargo")

class motorcycle(Vehicle):
    def identify(self):
        print(f"{self.name} is a 2 wheeler")

s1=car(name='Toyoto')
s1.identify()
s1.start()
s1.stop()

d1=truck(name='mahindra')
d1.start()
d1.stop()
d1.identify()

motor=motorcycle(name='R15')
motor.start()
motor.stop()
motor.identify()


#Inheritance Using Employee Management (Employee → Manager/Developer/Tester)

# Problem (2)

class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def details(self):
        print(f" Name is {self.name}")
        print(f" Id is {self.id}")
        print(f" Salary is {self.salary}")

class manager(employee):
    def identify(self):
        print("He is workng monitoring role")
class Developer(manager):
    pass
class Tester(employee):
    pass

soft=manager(name='Vimal' , id='432' , salary='24500')
soft.details()
soft.identify()