# Single level and Multiple level Inheritance in python

class IT_field:
    def HR(self):
        print("He organizining the company")

    def Manager(self):
        print("He is working under the HR")

class branch:
    def head_office(self):
        print("located in london")

class Chairman(IT_field,branch):

    def PA(self):
        print("Chairman have to a rights")

    def donate(self):
        print("He donate more money to people")

c=Chairman()
c.Manager()
c.head_office()