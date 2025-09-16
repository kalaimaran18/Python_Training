class laptop:
    chargertype="Type B"

    def __init__(self):
        self.brand=" "
        self.price=45000

    def setPrice(self,price):
        self.price=price
        print(self.price)

    def getPrice(self):
        print(self.price)

    @classmethod
    def changechargertype(cls):
        cls.chargertype="C"
        print("chargertype is to be C")


l=laptop()
l.getPrice()
l.setPrice(23000)
l.changechargertype()
