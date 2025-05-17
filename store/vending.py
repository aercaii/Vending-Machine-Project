from item import Item

class VendingMachine:
    def __init__(self,item_codes, item_objects):
        self.item_codes = {}
        self.item_objects = item_objects
        ##self.coin_denominations = [0.1,0.5,0.25]
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
    
    def dispense_item(self,item):
        if self.deposited == 0:
            print("Insufficent Funds")
        print(f"Dispensing {item}")

    def calculate_change(self):
        d = 0.10
        p = 0.01
        q = 0.25
        dime_total = 0 
        penny_total = 0
        quarter_total = 0

        amount = self.deposited

        if amount >= 0.25:
            quarter_total = amount//q
            amount = round(quarter_total * q)
        if amount >= 0.10:
            dime_total = amount//d
            amount = round(dime_total * d)
        if amount >= 0.01:
            penny_total = amount//p
            amount = round(penny_total * p)
        
        return quarter_total,dime_total,penny_total
        
