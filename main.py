from store.vending import VendingMachine 
from store.item import Item
import time
import colorama
from colorama import Fore,Style,init


# items
item1 = Item("Coke", price=1.00,quantity=10,code="A1")
item2 = Item("Protein Bar", price=1.50,quantity=1,code="B2")
item3 = Item("Water", price=0.90,quantity=15, code="C3")
# text color
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

'''print(f"{RED}This is a red line.{RESET}")
print(f"{GREEN}This is a green line.{RESET}")
print(f"{BLUE}This is a blue line.{RESET}")'''
# main function
vm = VendingMachine() # ([]) needed to initialize a list
vm.add_item(code="A1",item=item1,quantity=10,price=1.00)
vm.add_item(code="B2",item=item2,quantity=1,price=1.50)
vm.add_item(code="C3",item=item3,quantity=15,price=0.90)
def main_interaction():
        
        
        print(f"{GREEN}Welcome to the Vending Machine.{RESET}")
        print("-"*40)
        time.sleep(1.5)
        print(vm.display_items())
        print(f"Enter a Code to buy [Case Sensitive] or type {RED}'exit'{RESET} to exit the program")
        code_input =input(str(f"Please enter an code: "))
        print(code_input)
        
        if (vm.select_item(code=code_input)) == 1: # if the function returns 1 (item found) 0 (item not found)
                item = vm.item_codes[code_input]
                
                amount = float(input("Enter an amount to purchase ($) : "))
                if amount <= 0:
                    print(f"{RED}Invalid amount entered. Please enter a positive amount.{RESET}")
                    time.sleep(2)
                    exit()
                        
                vm.insert_money(amount=amount)
                print(f"{GREEN}Inserted: ${amount:.2f}{RESET}")
                    
                # Calculate change using item price
                quarters, dimes, pennies = vm.calculate_change(item_price=item.price)
                if quarters == 0 and dimes == 0 and pennies == 0 and amount < item.price:
                    print(f"{RED}Insufficient funds. Please insert ${item.price - amount:.2f} more.{RESET}")
                    time.sleep(2)
                    exit()
                        
                    
                if item.quantity == 0: # item out of stock
                    print(f"{RED}Item out of stock.{RESET}")
                    time.sleep(1.5)
                    print(f"{GREEN}Returning your deposited amount: ${amount:.2f}{RESET}")
                    time.sleep(2)
                    exit()
                        
                
                print(f"{GREEN}Dispensing {item.name}...{RESET}")
                time.sleep(3)
                if vm.dispense_item(item=item):
                        
                    if quarters > 0 or dimes > 0 or pennies > 0:
                        print(f"Change returned: {quarters} quarter(s), {dimes} dime(s), {pennies} penny(ies)")
                        time.sleep(3)

                    else:
                        print(f"No change returned.")
                        time.sleep(3)
                else:
                    print(f"{RED}Failed to dispense item.{RESET}")
                    time.sleep(2)
                    exit()
        else:
             exit()

                
                
                
while True :
    
    main_interaction()