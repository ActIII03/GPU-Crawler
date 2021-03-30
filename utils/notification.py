import json
import boto3
import pdb
import csv
import re
import os
import logging

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
    # Open csv file for AWS's IAM credential
    # def readin_csv(self):
    #     try:
    #         csvfile = list(csv.reader(open(self.file_name, 'r'), delimiter='\n'))
    #         self.accesskey_id = re.sub('[\[\[\]\'<>]','',str(csvfile[1]))
    #         self.secret_key = re.sub('[\[\[\]\'<>]','',str(csvfile[2]))
    #     except IOError:
    #         logging.exception('')
    #     if(csvfile == None):
    #         raise ValueError('NO AWS IAM Cred.\'s\n Ensure AWS IAM Cred. (.csv) is located in ~/utils/ dir in order for docker env to see cred\'s')
    # Check if in-stock
    def check_if_stock(self) -> "bool":
        flag = False
        for gpu_card in range(0, len(self.gpu_data)):
            if(self.gpu_data[gpu_card]["in-stock"] == True):
                self.in_stock[self.count] = self.gpu_data[gpu_card]
                flag = True
                self.count += 1
        return flag
    # Send sms
    def send_msg(self, phone_number):
        # Get ENV var's for AWS's IAM credentials
        client = boto3.client(
                "sns",
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID').strip("\""),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY').strip("\""),
                region_name=os.getenv('AWS_REGION').strip("\""),
        )                
        # Publish SMS
        # text_message = ["index: "
        return None
    # Core of notification sys
    def run(self, phone_number):
        # Open file
        self.readin_json()
        stock_status = self.check_if_stock()
        # self.readin_csv()
        breakpoint()
        if(stock_status == True):            
            self.readin_csv()
            sent = self.send_msg(phone_number)

