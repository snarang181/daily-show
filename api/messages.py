import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
meta_auth_token = 'Bearer ' + os.environ.get('meta_api_token')

def format_cmd_msg(name): 
    cmd = 'Hi ' + name + '! Here are the commands you can use: \n\n'
    cmd = cmd + '\t \u2022 /help - Get a list of commands \n'
    cmd = cmd + '\t \u2022 /joke - Read a joke \n'
    cmd = cmd + '\t \u2022 /price - Get latest prices \n'
    cmd = cmd + '\t \u2022 /weather - Get weather forecast \n'
    return cmd

     
def send_cmd_msg(phone_num, phone_num_id, name):
    msg = format_cmd_msg(name)
    send_message(phone_num, phone_num_id, msg, name)
    return 


def send_message(phone_num, phone_num_id, message, name):
    global meta_auth_token    
    base_url = 'https://graph.facebook.com/v13.0/' + str(phone_num_id) + '/messages'
    headers = {'Authorization' : meta_auth_token, 'Content-Type': 'application/json'}
    body = {
        "messaging_product" : "whatsapp", "recipient_type" : "individual", "to" : str(phone_num) , "type" : "text" , "text" : {
            "preview_url" : False,
            "body" : str(message)
        }
    }
    r = requests.post(base_url, data=json.dumps(body), headers=headers)


    
    
    