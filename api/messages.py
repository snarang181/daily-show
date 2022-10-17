import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
meta_auth_token = 'Bearer ' + os.environ.get('meta_api_token')
def send_message(phone_num, phone_num_id, message):
    
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
    print(r.json())


    
    
    