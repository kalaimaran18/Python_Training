from abc import ABC , abstractmethod

#payment gateway to abstraction

class Payment:
    def __init__(self,card,branch):
  
        self.card=card
        self.branch=branch
        print(f"self.card:{card} ,self.branch:{branch}")

    @abstractmethod
    def settle(self):
        print("To settlement of the money")

class Gateway():
    def money(self):
        print("request for 1000 rupee")
    def resource(self):
        print("using credit card,upi payment")

    def get_money(self):
        print("Finally get the money 1000")

s1=Gateway()
s1.money()
s1.resource()
s1.get_money()

#abstraction Database Connection 

class database:
    def __init__(self):
        print("connect sql database")

    @abstractmethod
    def db(self,connect):
        print("link using db")

class sql_queries(database):
    def users(self):
        print("MAin method to sql")
        
d1=sql_queries()
d1.users()
