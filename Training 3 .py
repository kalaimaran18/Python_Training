
#Checking Back Account details using Encapsulation  (Problem 1)

class BankAccount:
    def __init__(self,owner,balance=0):
        self.__owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited:{amount},new balance:{self.__balance}")

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdraw:{amount} , New Balance:{self.__balance}")
    
    def get_bank(self):
        return self.__balance
    
s1=BankAccount("Kalaimaran",100)
s1.deposit(300)
s1.withdraw(200)
print(f"Final Balance:{s1.get_bank()}")


#Checking Authentification method using Encapsulation   (Problem 2)

class Authenticator:
    def __init__(self, username, password):
        # Private attributes (encapsulated)
        self.__username = username
        self.__password = password

    def authenticate(self, input_username, input_password):
        # Public method to check credentials
        if self.__username == input_username and self.__password == input_password:
            return True
        else:
            return False

# Main program
# Instantiate the class with the correct credentials
auth_checker = Authenticator("admin", "password123")

# Prompt the user for input
user_input_username = input("Enter username: ")
user_input_password = input("Enter password: ")

# Use the public method to authenticate
if auth_checker.authenticate(user_input_username, user_input_password):
    print("Authentication successful! ✅")
else:
    print("Authentication failed. ❌")
