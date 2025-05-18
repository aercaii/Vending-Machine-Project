from store.vending import VendingMachine 
from store.item import Item
import time
import colorama
from colorama import Fore,Style,init

# items
item1 = Item("Coke", price=1.00,quantity=10)
item2 = Item("Protein Bar", price=1.50,quantity=10)
item3 = Item("Water", price=0.90,quantity=15)
# text color
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

'''print(f"{RED}This is a red line.{RESET}")
print(f"{GREEN}This is a green line.{RESET}")
print(f"{BLUE}This is a blue line.{RESET}")'''
# main function


def main_interaction():
    vm = VendingMachine() # ([]) needed to initialize a list
    vm.add_item(code="A1",item="Coke")
    vm.add_item(code="B2",item="Protein Bar")
    vm.add_item(code="C3",item="Water")
    print(vm.display_items())
    print(f"{GREEN}Welcome to the Vending Machine.{RESET}")
    print("-"*40)
    time.sleep(1.5)
    print(f"{BLUE}Availiable Items\n A1 {item1.name} ${item1.price:.2f} \n B2 {item2.name} ${item2.price:.2f} \n C3 {item3.name} $ {item3.price:.2f}")
    print(f"Enter a Code to buy or type {RED}'exit'{RESET} to exit the program")
    code_input =input(str(f"Please enter an code: "))
    print(code_input)
    print(vm.select_item(code=code_input))

if __name__ == "__main__":
    
    main_interaction()