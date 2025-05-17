from item import Item

class VendingMachine:
    def __init__(self,item_codes, item_objects):
        self.item_codes = {}
        self.item_objects = {}
        self.coin_denominations = [0.1,0.5,0.25]
        self.deposited = 0
    def add_item(self,code,item):
        self.item_codes[code] = item

    def display_items(self):
        for code,item in self.item_objects.items():
            print(f"{code} : {item}")
    def insert_money(self,amount:float):
        self.deposited += amount

    def select_item(self,code):
        item  = self.item_codes[code]
        return item
        

        
       

        