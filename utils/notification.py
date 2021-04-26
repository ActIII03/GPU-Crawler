import json
import boto3
import csv
import re
import os
import logging

# Notification System
class NotificationSys:
    # Copy-Constructor
    def __init__(self):
        self.gpu_data = None
        self.in_stock = None
        self.file_name = '.aws/credentials'
        self.topicarn = None
        self.accesskey_id = None 
        self.secret_key = None 
        self.region = 'us-east-2a'
        self.aws_service = 'sns'
        self.count = 0
    # Open file and load into dictionary
    def readin_json(self):
        # Open json file
        with open('items.json', 'r') as json_file:
            try:
                self.gpu_data = json.load(json_file)
                json_file.close()
            except IOError:
                logging.exception('')
    # Check if in-stock
    def check_if_stock(self) -> "bool":
        flag = False
        for gpu_card in range(0, len(self.gpu_data) - 1):
            if(self.gpu_data[gpu_card]["in-stock"] == True):
                self.in_stock[self.count] = self.gpu_data[gpu_card]
                flag = True
                self.count += 1
        return flag
    # Send sms
    def send_msg(self, phone_number):
        # Get ENV var's w/in the running Docker instance for AWS's IAM credential verification process
        client = boto3.client(
                "sns",
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID').strip("\""),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY').strip("\""),
                region_name=os.getenv('AWS_REGION').strip("\""),
        )                
        # Publish SMS 
        message = "There are {0} GPU's instock".format(len(self.in_stock))
        client.publish(
                PhoneNumber=phone_number,
                Message=message,
        )
        return None
    # Readout in-stock GPUs' to text-file (.txt)
    def readout_instock(self) -> "None":
        # Open text file
        with open("instock_gpu.txt", "w") as instock_file:
            for item in self.in_stock:
                instock_file.write('%d) Item: %s; Price: %s; Add-to-cart: %s\n' % (
                     item,
                     self.in_stock[item]["title"],
                     self.in_stock[item]["price"],
                     self.in_stock[item]["sku"],
                     )
                )
        instock_file.close()
    # Core of notification sys (main driver)
    def run(self, phone_number):
        # Open file
        self.readin_json()
        # Check if GPU's are stocked
        stock_status = self.check_if_stock()
        # If stocked, then send to client: (i) text-message (ii) email of add-to-cart links
        if(stock_status == True):            
            sent = self.send_msg(phone_number)
            # Write in-stock GPU's to text file
            self.readout_instock()

