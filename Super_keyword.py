# Super Keyword using python 

class India():
    def __init__(self):
        print("Indian")

    def display(self):
        print("capital city New Dehli")

class America():
    def __init__(self):
        super().__init__()
        print("American")

    def display(self):
        print("capital city Washigton D.C")


class Austalia(America,India):
    def __init__(self):
        super().__init__()
        print("Austalian")

    def display(self):
        print("capital city Canberra")

ob1=Austalia()
ob1.display()