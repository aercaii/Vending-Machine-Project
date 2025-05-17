class Item:
    def __init__(self,name,price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def check_stock(self):
        if self.quantity == 0:
            print("Out Of Stock")
        elif self.quantity <0:
            print("ERR: Stock is under 0")
        else:
            print("In Stock")
    def purchase(self):
        if self.quantity == 0:
            
            print("ERR: Item is out of stock")
        else:
            self.quantity -= 1
        print(f"Sucessfully purchaed: {self.name} \n Quantity: {self.quantity}")
        
    
        
        
    