class laptop():
    laptop=warrenty=2
    def __init__(self,brand,model,ram,):
        self.brand=brand
        self.model=model
        self.ram=ram
        
    
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Ram:",self.ram)
        print("Warrenty:",self.warrenty)


l=laptop("DELL","i5",16)
l.display()

dl=laptop("dell","i3",8)
dl.display()
       