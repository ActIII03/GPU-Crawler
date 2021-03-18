import json
import pdb
# from sms4 import send, nonblocking_send

class NotificationSys:
    # Copy-Constructor
    def __init__(self):
        self.gpu_data = None
    # Open file and load into dictionary
    def open_json(self):
        # Open json file
        with open('items.json', 'r') as json_file:
            self.gpu_data = json.load(json_file)
            breakpoint()
            json_file.close()
    # Check if in-stock <--- Come back to later
    # def check_if_stock(self):
        

    # Core of notification sys
    def run(self):
        # Open file
        self.open_json()
    

