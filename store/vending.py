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
        
def test_calculate_change():
    # Placeholder for item_objects (modify based on your needs)
    item_objects = [
        {"name": "Soda", "price": 1.50},
        {"name": "Chips", "price": 1.00}
    ]
    
    # List of test cases: (deposited amount, expected result)
    test_cases = [
        (0.37, {"quarters": 1, "dimes": 1, "pennies": 2}),  # 37 cents
        (0.25, {"quarters": 1, "dimes": 0, "pennies": 0}),  # 25 cents
        (0.10, {"quarters": 0, "dimes": 1, "pennies": 0}),  # 10 cents
        (0.07, {"quarters": 0, "dimes": 0, "pennies": 7}),  # 7 cents
        (0.99, {"quarters": 3, "dimes": 2, "pennies": 4}),  # 99 cents
        (0.00, {"quarters": 0, "dimes": 0, "pennies": 0}),  # 0 cents
    ]
    
    for deposited, expected in test_cases:
        print(f"\nTesting deposited: ${deposited:.2f}")
        vm = VendingMachine(item_objects, deposited)
        result = vm.calculate_change()
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 40)
    
    # Test negative input
    print("\nTesting negative input: $-0.10")
    try:
        vm = VendingMachine(item_objects, -0.10)
        vm.calculate_change()
        print("Test failed: Negative input should raise an error")
    except ValueError:
        print("Test passed: Negative input correctly raised an error")
        print("-" * 40)

# Run the tests
if __name__ == "__main__":
    test_calculate_change()