class College():
    def __init__(self):
        print("1st Year")
        super().__init__()

    def display(self):
        print("Junior")

class Department(College):
    def __init__(self):
        super().__init__()
        print("They are Toppers")

    def display(self):
        print("Computer Science and Engineering ")

ob1=Department()
