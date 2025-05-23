import mainpy
import datetime
from datetime import datetime

class Logging_file:
    def __init__(self,time,item,price,change):
        
        self.time = datetime.now()
        self.current_time_string = time.strftime("%Y-%m-%d %H:%M:%S")
        self.item = item
        self.price = price
        self.change = change
    
    def write_file(self):
        file = open(f"Purchase Receipt.text","w")
        file.write(f"You have purchased: {self.item} \n Change: {self.change} \n Price: {self.price}\n At: {self.current_time_string}")
        file.close()
