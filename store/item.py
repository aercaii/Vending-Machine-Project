class Item:
    def __init__(self,name,price, quantity,code):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.code = code
    def __str__(self):
        return self.name
    def check_stock(self):
        if self.quantity == 0:
            print("Out Of Stock")
        elif self.quantity <0:
            print("ERR: Stock is under 0")
        else:
            print("In Stock")
    def return_stock(self):
        return self.quantity
    def purchase(self):
        if self.quantity == 0:
            
            print("ERR: Item is out of stock")
        else:
            self.quantity -= 1
        print(f"Sucessfully purchased: {self.name} \n Quantity: {self.quantity}")
        print("-"*40)
        
    
        
        
    