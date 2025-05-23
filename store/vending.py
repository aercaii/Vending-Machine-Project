from store.item import Item

class VendingMachine:
    def __init__(self):
        self.item_codes = {}
        
        ##self.coin_denominations = [0.1,0.5,0.25]
        self.deposited = 0

    def __str__(self):
        return self.item_codes.items().name
    def add_item(self, code, item, quantity, price):
        
        self.item_codes[code] = Item(name=item, code=code, quantity=quantity, price=price)
   
        
        

    def display_items(self):
        
        output = f"Items in Vending Machine:\n"
        for code, item in self.item_codes.items():
            output += f"{code}: {item.name} | {item.quantity} in stock | ${item.price:.2f}\n"
        return output
    
    def insert_money(self,amount:float):
        self.deposited += amount

    def select_item(self, code):
        
        if code in self.item_codes:
            print(f"Item Found, you have selected {self.item_codes[code].name}")
            return 1
        elif code == 'exit':
            pass
    
        else:
            print("ERR | Item not found or wrong code entered")
            return 0
    
    def dispense_item(self, item):
        
        if self.deposited == 0:
            print("Insufficient Funds")
            return False
        if item.quantity == 0:
            return False
        item.purchase()  
        return True

    def calculate_change(self, item_price):
        
        # Define coin values
        QUARTER = 0.25
        DIME = 0.10
        PENNY = 0.01
        
        # Calculate change needed
        change = self.deposited - item_price
        if change < 0:
            return 0, 0, 0  # Not enough money inserted
        
        
        change_cents = int(round(change * 100))
        
       
        quarter_total = change_cents // int(QUARTER * 100)
        change_cents = change_cents % int(QUARTER * 100)
        
        dime_total = change_cents // int(DIME * 100)
        change_cents = change_cents % int(DIME * 100)
        
        penny_total = change_cents // int(PENNY * 100)
        
        return int(quarter_total), int(dime_total), int(penny_total)